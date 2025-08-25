# CivilInc Project - Deployment Instructions

## Backend Deployment (Railway)

### Prerequisites
1. Create a Railway account at https://railway.app/
2. Install the Railway CLI: `npm install -g @railway/cli`

### Steps

1. **Prepare the backend for deployment**:
   - Ensure all dependencies are listed in `requirements.txt`
   - Check that the `railway.json` file is properly configured

2. **Login to Railway CLI**:
   ```bash
   railway login
   ```

3. **Initialize Railway project**:
   ```bash
   cd CIVILINC/backend
   railway init
   ```

4. **Set environment variables**:
   - Go to your Railway project dashboard
   - Add the following environment variables:
     - `SECRET_KEY`: A secure random string
     - `DATABASE_URL`: Railway will automatically provide this for PostgreSQL
     - `REDIS_HOST`: If using Redis, set to your Redis host
     - `REDIS_PORT`: Redis port (usually 6379)

5. **Deploy to Railway**:
   ```bash
   railway up
   ```

6. **Run database migrations** (if needed):
   ```bash
   railway run python init_db_properly.py
   ```

## Frontend Deployment (Netlify)

### Prerequisites
1. Create a Netlify account at https://netlify.com/
2. Install the Netlify CLI: `npm install -g netlify-cli`

### Steps

1. **Build the production version**:
   ```bash
   cd CIVILINC
   npm run build
   ```

2. **Login to Netlify CLI**:
   ```bash
   netlify login
   ```

3. **Deploy to Netlify**:
   ```bash
   netlify deploy
   ```
   - Select "Create & configure a new site"
   - Choose your team
   - Enter a site name (or leave blank for auto-generated)
   - Set the publish directory to `dist`

4. **Deploy to production**:
   ```bash
   netlify deploy --prod
   ```

5. **Configure environment variables**:
   - Go to your Netlify site settings
   - Navigate to "Environment variables"
   - Add `VUE_APP_API_URL` with the URL of your deployed backend

## ML Model Deployment

### Options for ML Model Deployment

1. **Keep with Backend (Recommended for this project)**:
   - The ML model is already integrated with the backend
   - It will be deployed along with the backend on Railway
   - Ensure the model files are in the `models` directory

2. **Separate ML Service (Advanced)**:
   - Deploy as a separate service using platforms like:
     - AWS SageMaker
     - Google AI Platform
     - Azure Machine Learning
     - Heroku with Docker

### For this project, keeping the ML model with the backend is recommended because:
- The model is already integrated
- It simplifies deployment
- It reduces latency for model predictions
- It's cost-effective for the current scale

## Post-Deployment Configuration

### Update API URLs
1. After deploying the backend, update the frontend environment variable:
   - In Netlify, set `VUE_APP_API_URL` to your Railway backend URL

2. If you're using a custom domain:
   - Update CORS settings in `CIVILINC/backend/app/core/config.py` to include your domain

### Database Configuration
1. Railway automatically provides a PostgreSQL database
2. Update `CIVILINC/backend/app/core/config.py` to use PostgreSQL instead of SQLite:
   ```python
   DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
   ```

### Environment Variables Summary
- Backend (Railway):
  - `SECRET_KEY`: Your secret key
  - `DATABASE_URL`: Provided by Railway
  - `REDIS_HOST`: If using Redis

- Frontend (Netlify):
  - `VUE_APP_API_URL`: Your deployed backend URL

## Monitoring and Maintenance

1. **Backend Monitoring**:
   - Use Railway's built-in monitoring
   - Check logs with `railway logs`

2. **Frontend Monitoring**:
   - Use Netlify's analytics
   - Set up error tracking with services like Sentry

3. **Database Backups**:
   - Railway automatically handles database backups for PostgreSQL

4. **ML Model Updates**:
   - To update the ML model, retrain it locally and redeploy the backend
   - Consider implementing model versioning for production environments

## Troubleshooting Deployment Issues

1. **CORS Errors**:
   - Ensure your frontend domain is in the `BACKEND_CORS_ORIGINS` list in `config.py`

2. **Database Connection Issues**:
   - Verify the `DATABASE_URL` environment variable
   - Check that the database is properly initialized

3. **ML Model Loading Errors**:
   - Check the logs for any model loading errors
   - Ensure model files are included in the deployment

4. **Environment Variables Not Set**:
   - Double-check all required environment variables are set in both Railway and Netlify

## Cost Considerations

1. **Railway**:
   - Free tier includes $5 credit monthly
   - PostgreSQL database with 1GB storage
   - Sleeps after 12 hours of inactivity

2. **Netlify**:
   - Free tier includes 100GB bandwidth/month
   - 300 build minutes/month
   - Custom domains

3. **Scaling**:
   - Both platforms offer paid tiers for higher usage
   - Consider upgrading when you need more resources