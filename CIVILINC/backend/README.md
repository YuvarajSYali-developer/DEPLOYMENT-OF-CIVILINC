# CivilInc Backend

This is the backend API for the CivilInc project, built with FastAPI.

## Features

- User authentication and authorization
- Project and complaint management
- Machine learning model integration for budget allocation predictions
- Real-time updates with WebSocket
- Caching with Redis
- Database management with SQLAlchemy

## Deployment

### Railway Deployment

1. Create a new project on Railway
2. Connect your GitHub repository
3. Set the following environment variables:
   - `SECRET_KEY`: A secure secret key for JWT tokens
   - `DATABASE_URL`: Your database connection string (Railway provides this automatically)
   - `REDIS_HOST`: Redis host (if using Redis add-on)
   - `REDIS_PORT`: Redis port (if using Redis add-on)
4. Railway will automatically detect the build and start commands from `railway.json`

### Environment Variables

Create a `.env` file in the backend directory with the following variables:

```
SECRET_KEY=your-secret-key-change-in-production
DATABASE_URL=sqlite:///./app.db
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
MODEL_DIR=models
ML_MODEL_PATH=models
LOG_LEVEL=INFO
LOG_FILE=app.log
```

### Training the ML Model

To train the budget allocation model:

1. Run the training script:
   ```bash
   python train_budget_model.py
   ```

2. This will create a `models/budget_model.pkl` file that will be loaded by the application.

## API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Development

### Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python init_db.py
   ```

4. Train the ML model:
   ```bash
   python train_budget_model.py
   ```

5. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Project Structure

```
backend/
├── app/
│   ├── api/          # API endpoints
│   ├── core/         # Core business logic
│   ├── db/           # Database models and initialization
│   ├── models/       # Pydantic models
│   ├── schemas/      # Data schemas
│   └── services/     # Business services
├── models/           # Trained ML models
├── alembic/          # Database migrations
├── requirements.txt  # Python dependencies
├── railway.json      # Railway deployment configuration
└── README.md         # This file