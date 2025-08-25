# Running the CivilInc Project

This document provides instructions on how to run the CivilInc full-stack project, including the backend, frontend, and ML model components.

## Prerequisites

1. Python 3.8 or higher
2. Node.js and npm
3. Virtual environment tool (like venv or conda)

## Backend Setup

1. Navigate to the backend directory:
   ```
   cd CIVILINC/backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

5. Initialize the database:
   ```
   python init_db_properly.py
   ```

6. Start the backend server:
   ```
   python -m uvicorn app.main:app --reload
   ```

   The backend will be available at: http://localhost:8000

## Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd CIVILINC
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

3. Start the frontend development server:
   ```
   npm run serve
   ```

   The frontend will be available at: http://localhost:8081

## Default Login Credentials

After initializing the database, you can use the following credentials to log in:

- Email: admin@civilinc.com
- Password: admin123

## ML Model

The ML model is automatically loaded when the backend server starts. The model files are located in the `CIVILINC/backend/models` directory.

## API Documentation

Once the backend is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

- `CIVILINC/` - Frontend Vue.js application
- `CIVILINC/backend/` - Backend FastAPI application
- `CIVILINC/backend/models/` - ML model files
- `CIVILINC/backend/app.db` - SQLite database file

## Troubleshooting

1. If you encounter any database issues, try reinitializing the database:
   ```
   cd CIVILINC/backend
   python init_db_properly.py
   ```

2. If you encounter any dependency issues, make sure you have activated the virtual environment and installed all required packages.

3. If the frontend cannot connect to the backend, ensure both servers are running and check the CORS settings in `CIVILINC/backend/app/core/config.py`.