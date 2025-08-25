"""
Test script for the budget allocation model.
"""
import os
import sys
import numpy as np
from app.core.ml_model_logic import BudgetAllocationModel

def test_model():
    """
    Test the budget allocation model.
    """
    print("Testing Budget Allocation Model")
    print("=" * 40)
    
    # Initialize model
    model_path = 'models/budget_model.pkl'
    model = BudgetAllocationModel(model_path=model_path)
    
    # Check if model is loaded
    if model.model is None:
        print("Model not loaded. Training a new model...")
        # Train a simple model for testing
        model.train_sample_data()
    else:
        print("Model loaded successfully")
    
    # Test prediction
    test_data = {
        'project_type': 'Road Construction',
        'location': 'Urban',
        'severity': 'High'
    }
    
    try:
        prediction = model.predict(test_data)
        print(f"Prediction for test data: {prediction}")
        print("Test passed!")
        return True
    except Exception as e:
        print(f"Test failed with error: {str(e)}")
        return False

if __name__ == "__main__":
    # Add the app directory to the Python path
    sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
    
    success = test_model()
    sys.exit(0 if success else 1)