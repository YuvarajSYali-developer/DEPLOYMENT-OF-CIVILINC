"""
Script to properly initialize the database with tables and initial data.
"""
import os
import sys

# Add the app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

def init_database():
    """
    Initialize the database with proper table creation and initial data.
    """
    try:
        # Import the database session and models
        from app.db.session import SessionLocal
        from app.db.init_db import init_db
        
        print("Initializing database...")
        init_db()
        print("Database initialized successfully")
        return True
    except Exception as e:
        print(f"Database initialization failed: {str(e)}")
        return False

def create_tables():
    """
    Create database tables if they don't exist.
    """
    try:
        # Import the database models and engine
        from app.db.session import Base, engine
        
        print("Creating database tables...")
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully")
        return True
    except Exception as e:
        print(f"Table creation failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("Initializing CivilInc Database")
    print("=" * 40)
    
    # Create tables first
    if create_tables():
        # Then initialize with data
        init_database()
    
    print("\nDatabase initialization completed!")