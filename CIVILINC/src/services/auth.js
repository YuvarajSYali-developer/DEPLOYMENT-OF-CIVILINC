import axios from 'axios';
import api from './api';

export const authService = {
  async login(email, password) {
    try {
      // Make API call to login endpoint with URL-encoded form data
      const params = new URLSearchParams();
      params.append('username', email);
      params.append('password', password);
      
      // Use a separate axios instance for login to handle form data
      const baseURL = process.env.VUE_APP_API_URL || 'http://localhost:8000';
      const response = await axios.post(
        `${baseURL}/api/v1/login`,
        params.toString(),
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
          },
          withCredentials: true
        }
      );
      
      // Store token in localStorage
      if (response.data.access_token) {
        localStorage.setItem('token', response.data.access_token);
      }
      
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  },

  async register(email, password) {
    try {
      const response = await api.post('/register', {
        email: email,
        password: password
      });
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  },

  logout() {
    // Remove token from localStorage
    localStorage.removeItem('token');
  },

  isAuthenticated() {
    // Check if token exists and is valid
    const token = localStorage.getItem('token');
    return !!token;
  },

  // Handle API errors
  handleError(error) {
    if (error.response) {
      // Server responded with error
      const message = error.response.data.detail || 'An error occurred';
      return new Error(message);
    } else if (error.request) {
      // Request made but no response
      return new Error('No response from server');
    } else {
      // Other errors
      return new Error('An unexpected error occurred');
    }
  }
};