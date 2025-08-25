# CivilInc Project - Fixes and Instructions

## Issues Fixed

1. **Double API Prefix Issue**: 
   - Problem: The frontend was making requests to `/api/v1/api/v1/login` instead of `/api/v1/login`
   - Fix: Corrected the endpoint in `CIVILINC/src/views/page-02.vue` from `/api/v1/login` to `/login` since the axios instance already includes `/api/v1` in the baseURL

2. **Register Function Issue**:
   - Problem: The register function in `auth.js` was also using a double prefix
   - Fix: Corrected the endpoint in `CIVILINC/src/services/auth.js` from `/api/v1/register` to `/register`

## How to Test the Login

1. Make sure both backend and frontend servers are running:
   - Backend: `cd CIVILINC/backend && python -m uvicorn app.main:app --reload`
   - Frontend: `cd CIVILINC && npm run serve`

2. Open your browser and go to: http://localhost:8081

3. Navigate to the login page and use the following credentials:
   - Email: admin@civilinc.com
   - Password: admin123

4. Alternatively, you can use the test file we created:
   - Open `CIVILINC/test-login.html` in your browser
   - Click the "Login" button
   - You should see a success message with a token

## API Endpoints

- Login: POST http://localhost:8000/api/v1/login
- Register: POST http://localhost:8000/api/v1/register
- API Documentation: http://localhost:8000/docs

## ML Model

The ML model is automatically loaded when the backend starts. You can check the logs in `CIVILINC/backend/app.log` to verify it's loaded correctly.

## Troubleshooting

1. If you get a 404 error:
   - Make sure you're using the correct endpoint (without double prefix)
   - Check that both backend and frontend servers are running

2. If login fails with "Invalid credentials":
   - Make sure you've initialized the database with `python init_db_properly.py`
   - Verify the default user exists in the database

3. If you get CORS errors:
   - Check the CORS settings in `CIVILINC/backend/app/core/config.py`
   - Make sure the frontend URL (http://localhost:8081) is in the allowed origins list

4. If the favicon.ico error appears:
   - This is a minor issue and doesn't affect functionality
   - You can add a favicon.ico file to the public folder if needed