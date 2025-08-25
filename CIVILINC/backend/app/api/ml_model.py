from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, Any
import time
from app.core.ml_service import MLService
from app.core.cache import Cache
from app.core.logging import Logger
from app.schemas.ml_model import MLModelInput, MLModelOutput
from app.core.auth import get_current_user

router = APIRouter()
ml_service = MLService()
cache = Cache()
logger = Logger()

@router.post("/run", response_model=MLModelOutput)
async def run_model(
    input_data: MLModelInput,
    current_user = Depends(get_current_user)
):
    try:
        # Check cache first
        cache_key = f"ml_model_{input_data.model_name}_{hash(str(input_data.input_data))}"
        cached_result = cache.get(cache_key)
        if cached_result:
            logger.info(f"Cache hit for model {input_data.model_name}")
            return cached_result

        # Special handling for budget allocation model
        if input_data.model_name == "budget_allocation":
            # For budget model, pass the input data directly as dict
            start_time = time.perf_counter()
            result = await ml_service.run_model(
                model_name=input_data.model_name,
                input_data=input_data.input_data
            )
            processing_time = time.perf_counter() - start_time
            
            # Map result to schema shape
            output_data: Dict[str, Any] = {
                "prediction": result.get("prediction"),
                "probability": result.get("probability"),
                "timestamp": result.get("timestamp"),
            }
            
            response: Dict[str, Any] = {
                "model_name": input_data.model_name,
                "output_data": output_data,
                "processing_time": float(processing_time),
                "confidence_score": None,
            }
            
            # Cache result
            cache.set(cache_key, response, ttl=3600)  # Cache for 1 hour
            
            return response
        else:
            # Preprocess input for other models
            preprocessed_data = ml_service.preprocess(input_data.input_data)
            
            # Run model
            start_time = time.perf_counter()
            result = await ml_service.run_model(
                model_name=input_data.model_name,
                input_data=preprocessed_data
            )
            processing_time = time.perf_counter() - start_time
            
            # Map result to schema shape
            output_data: Dict[str, Any] = {
                "prediction": result.get("prediction"),
                "probability": result.get("probability"),
                "timestamp": result.get("timestamp"),
            }
            probability = result.get("probability")
            confidence_score = None
            if probability is not None:
                try:
                    # probability may be nested like [[p0, p1, ...]]; choose max
                    flat_probs = probability[0] if isinstance(probability, list) and len(probability) > 0 else probability
                    if isinstance(flat_probs, list) and len(flat_probs) > 0:
                        confidence_score = float(max(flat_probs))
                except Exception:
                    confidence_score = None
            
            response: Dict[str, Any] = {
                "model_name": input_data.model_name,
                "output_data": output_data,
                "processing_time": float(processing_time),
                "confidence_score": confidence_score,
            }
            
            # Cache result
            cache.set(cache_key, response, ttl=3600)  # Cache for 1 hour
            
            return response
    except Exception as e:
        logger.error(f"Model execution failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models")
async def list_models(current_user = Depends(get_current_user)):
    try:
        return ml_service.list_available_models()
    except Exception as e:
        logger.error(f"Failed to list models: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    try:
        return ml_service.check_health()
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))