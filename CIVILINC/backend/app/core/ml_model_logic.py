import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import joblib
import os
import numpy as np
from typing import Dict, Any

class BudgetAllocationModel:
    """
    A machine learning model to predict budget allocation for civil projects.
    """
    def __init__(self, model_path='models/budget_model.pkl'):
        """
        Initializes the model.

        Args:
            model_path (str): The path to the saved model file.
        """
        self.model_path = model_path
        self.model = None
        self.encoder = None
        self.feature_names = None
        self.load_model()

    def load_model(self):
        """
        Loads the trained model from the specified path.
        """
        if os.path.exists(self.model_path):
            # Load both model and encoder
            model_data = joblib.load(self.model_path)
            self.model = model_data['model']
            self.encoder = model_data['encoder']
            self.feature_names = model_data['feature_names']
        else:
            # If no model is found, we'll create a new one.
            # In a real-world scenario, you would train this model with your data.
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def train(self, data_path):
        """
        Trains the model on the given dataset.

        Args:
            data_path (str): The path to the training data (CSV file).
        """
        # Load the dataset
        data = pd.read_csv(data_path)

        # Define features and target
        features = ['project_type', 'location', 'severity']
        target = 'budget'

        # Separate features and target
        X = data[features]
        y = data[target]

        # Create and fit encoder
        self.encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        X_encoded = self.encoder.fit_transform(X)
        
        # Store feature names
        self.feature_names = self.encoder.get_feature_names_out(features)
        
        # Create DataFrame with encoded features
        X_encoded_df = pd.DataFrame(X_encoded, columns=self.feature_names)

        # Split the data into training and testing sets
        X_train, _, y_train, _ = train_test_split(X_encoded_df, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Save the trained model and encoder
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        model_data = {
            'model': self.model,
            'encoder': self.encoder,
            'feature_names': self.feature_names
        }
        joblib.dump(model_data, self.model_path)

    def predict(self, project_data: Dict[str, Any]) -> float:
        """
        Makes a budget prediction for a new project.

        Args:
            project_data (dict): A dictionary containing the project's features.

        Returns:
            float: The predicted budget.
        """
        if self.model is None or self.encoder is None:
            raise Exception("Model not loaded. Please train the model first.")

        # Create a DataFrame from the input data
        data = pd.DataFrame([project_data])
        
        # Apply the same encoding as used during training
        try:
            data_encoded = self.encoder.transform(data)
        except ValueError as e:
            # Handle unknown categories by using the encoder's handle_unknown='ignore' setting
            # This will create zero-columns for unknown categories
            raise Exception(f"Error encoding input data: {str(e)}")

        # Create DataFrame with encoded features
        data_encoded_df = pd.DataFrame(data_encoded, columns=self.feature_names)

        # Make a prediction
        prediction = self.model.predict(data_encoded_df)
        return prediction[0]

    def get_feature_names(self):
        """
        Returns the feature names used by the model.
        """
        return self.feature_names