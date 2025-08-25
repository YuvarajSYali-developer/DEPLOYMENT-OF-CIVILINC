import api from './api';

export const authService = {
  async login(email, password) {
    try {
      // Make API call to login endpoint with form data
      const formData = new FormData();
      formData.append('username', email);
      formData.append('password', password);
      
      const response = await api.post('/api/v1/login', formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      });
      
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
      const response = await api.post('/api/v1/register', {
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