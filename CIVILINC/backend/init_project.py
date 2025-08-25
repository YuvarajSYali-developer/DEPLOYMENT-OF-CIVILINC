"""
Script to initialize the project: create database and train initial model.
"""
import os
import sys
import subprocess
import importlib.util

def init_database():
    """
    Initialize the database.
    """
    print("Initializing database...")
    try:
        # Run the init_db.py script
        result = subprocess.run([sys.executable, "init_db.py"], 
                              cwd=os.path.dirname(os.path.abspath(__file__)),
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("Database initialized successfully")
        else:
            print(f"Database initialization failed: {result.stderr}")
    except Exception as e:
        print(f"Error initializing database: {str(e)}")

def train_model():
    """
    Train the initial model.
    """
    print("Training initial model...")
    try:
        # Run the train_budget_model.py script
        result = subprocess.run([sys.executable, "train_budget_model.py"], 
                              cwd=os.path.dirname(os.path.abspath(__file__)),
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("Model trained successfully")
            print(result.stdout)
        else:
            print(f"Model training failed: {result.stderr}")
    except Exception as e:
        print(f"Error training model: {str(e)}")

def check_dependencies():
    """
    Check if all required dependencies are installed.
    """
    print("Checking dependencies...")
    required_packages = [
        'fastapi',
        'uvicorn',
        'sqlalchemy',
        'pydantic',
        'joblib',
        'python-jose',
        'passlib',
        'python-multipart',
        'redis',
        'numpy',
        'pandas',
        'scikit-learn',
        'python-dotenv',
        'email-validator'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            importlib.util.find_spec(package.split('[')[0])  # Handle packages with extras like python-jose[cryptography]
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing packages: {', '.join(missing_packages)}")
        print("Please install them with: pip install -r requirements.txt")
        return False
    else:
        print("All dependencies are installed")
        return True

def main():
    """
    Main initialization function.
    """
    print("Initializing CivilInc Project")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        return False
    
    # Initialize database
    init_database()
    
    # Train model
    train_model()
    
    print("\nProject initialization completed!")
    print("You can now run the server with: uvicorn app.main:app --reload")

if __name__ == "__main__":
    main()