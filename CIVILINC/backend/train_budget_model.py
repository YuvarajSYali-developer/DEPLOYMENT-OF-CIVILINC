"""
Script to train and save the budget allocation model.
"""
import pandas as pd
import numpy as np
import os

try:
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.ensemble import RandomForestRegressor
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("Warning: scikit-learn not available. Model training will be skipped.")

def create_sample_data():
    """
    Create sample training data for the budget allocation model.
    In a real application, you would load this from a CSV file or database.
    """
    # Sample data
    data = {
        'project_type': ['Road Construction', 'Bridge Repair', 'Water Pipeline', 'Building Renovation', 
                         'Road Construction', 'Bridge Repair', 'Water Pipeline', 'Building Renovation',
                         'Road Construction', 'Bridge Repair', 'Water Pipeline', 'Building Renovation'],
        'location': ['Urban', 'Rural', 'Urban', 'Urban', 'Rural', 'Urban', 'Rural', 'Urban',
                     'Urban', 'Rural', 'Urban', 'Rural'],
        'severity': ['High', 'Medium', 'Low', 'High', 'Low', 'Medium', 'High', 'Low',
                     'Medium', 'High', 'Low', 'Medium'],
        'budget': [5000000, 3000000, 1500000, 4000000, 4500000, 2800000, 1200000, 3800000,
                   5200000, 3200000, 1300000, 3900000]
    }
    return pd.DataFrame(data)

def train_model():
    """
    Train the budget allocation model with sample data.
    """
    if not SKLEARN_AVAILABLE:
        print("Skipping model training because scikit-learn is not available.")
        return
    
    # Create sample data
    data = create_sample_data()
    
    # Save data to CSV for reference
    data.to_csv('sample_training_data.csv', index=False)
    print("Sample training data saved to 'sample_training_data.csv'")
    
    # Initialize model
    model_path = 'models/budget_model.pkl'
    
    # Train model (using the sample data directly)
    print("Training model with sample data...")
    
    # For this example, we'll manually train the model
    features = ['project_type', 'location', 'severity']
    target = 'budget'
    
    # Separate features and target
    X = data[features]
    y = data[target]
    
    # Create and fit encoder
    encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    X_encoded = encoder.fit_transform(X)
    
    # Store feature names
    feature_names = encoder.get_feature_names_out(features)
    
    # Create DataFrame with encoded features
    X_encoded_df = pd.DataFrame(X_encoded, columns=feature_names)
    
    # Split the data into training and testing sets
    X_train, _, y_train, _ = train_test_split(X_encoded_df, y, test_size=0.2, random_state=42)
    
    # Train the model
    regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    regressor.fit(X_train, y_train)
    
    # Save the trained model and encoder
    os.makedirs('models', exist_ok=True)
    model_data = {
        'model': regressor,
        'encoder': encoder,
        'feature_names': feature_names
    }
    
    import joblib
    joblib.dump(model_data, model_path)
    print(f"Model trained and saved to '{model_path}'")

def train_model_from_csv(csv_path):
    """
    Train the budget allocation model from a CSV file.
    """
    if not SKLEARN_AVAILABLE:
        print("Skipping model training because scikit-learn is not available.")
        return
    
    # Initialize model
    model_path = 'models/budget_model.pkl'
    
    # Train model with provided CSV
    print(f"Training model with data from {csv_path}...")
    
    # Load data
    data = pd.read_csv(csv_path)
    
    # Define features and target
    features = ['project_type', 'location', 'severity']
    target = 'budget'
    
    # Separate features and target
    X = data[features]
    y = data[target]
    
    # Create and fit encoder
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    X_encoded = encoder.fit_transform(X)
    
    # Store feature names
    feature_names = encoder.get_feature_names_out(features)
    
    # Create DataFrame with encoded features
    X_encoded_df = pd.DataFrame(X_encoded, columns=feature_names)
    
    # Split the data into training and testing sets
    X_train, _, y_train, _ = train_test_split(X_encoded_df, y, test_size=0.2, random_state=42)
    
    # Train the model
    regressor = RandomForestRegressor(n_estimators=100, random_state=42)
    regressor.fit(X_train, y_train)
    
    # Save the trained model and encoder
    os.makedirs('models', exist_ok=True)
    model_data = {
        'model': regressor,
        'encoder': encoder,
        'feature_names': feature_names
    }
    
    import joblib
    joblib.dump(model_data, model_path)
    print(f"Model trained and saved to '{model_path}'")

if __name__ == "__main__":
    train_model()