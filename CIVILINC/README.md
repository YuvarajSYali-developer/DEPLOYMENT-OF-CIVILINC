# CivilInc Frontend

This is the frontend for the CivilInc project, built with Vue.js.

## Features

- User authentication and authorization
- Project and complaint management
- Interactive map for location-based reporting
- Real-time updates with WebSocket
- Machine learning model integration for budget allocation predictions
- Responsive design for all devices

## Deployment

### Netlify Deployment

1. Create a new site on Netlify
2. Connect your GitHub repository
3. Set the following build settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
4. Set environment variables in Netlify:
   - `VUE_APP_API_URL`: Your backend API URL (e.g., https://civilinc-backend.up.railway.app)
   - `VUE_APP_WS_URL`: Your WebSocket URL (e.g., wss://civilinc-backend.up.railway.app)

## Development

### Installation

1. Install dependencies:
   ```bash
   npm install
   ```

2. Create environment files:
   - `.env.development` for local development
   - `.env.production` for production

3. Run the development server:
   ```bash
   npm run serve
   ```

4. Build for production:
   ```bash
   npm run build
   ```

## Project Structure

```
src/
├── assets/           # Static assets
├── components/       # Vue components
├── services/         # API services
├── store/            # Vuex store
├── views/            # Page components
├── App.vue           # Root component
├── main.js           # Entry point
└── router.js         # Vue Router configuration
```

## Environment Variables

Create `.env.development` and `.env.production` files with the following variables:

```
VUE_APP_API_URL=http://localhost:8000  # or your production API URL
VUE_APP_WS_URL=ws://localhost:8000     # or your production WebSocket URL
