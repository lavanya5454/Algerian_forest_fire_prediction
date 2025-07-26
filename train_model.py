#!/usr/bin/env python3
"""
Train Ridge regression model for Algerian Forest Fire prediction
This script creates the model and scaler files needed by the Flask app
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import os

def load_and_clean_data():
    """Load and clean the Algerian forest fires dataset"""
    print("Loading dataset...")
    
    # Load dataset
    data = pd.read_csv('Algerian_forest_fires_dataset_UPDATE_1753524208988.csv', header=1)
    
    # Remove header rows that might be mixed in data
    data = data[data['day'] != 'Sidi-Bel Abbes Region Dataset']
    data = data[data['day'] != 'day']
    
    # Drop rows with missing values
    data = data.dropna()
    
    # Convert numeric columns
    numeric_columns = ['day', 'month', 'year', 'Temperature', 'RH', 'Ws', 'Rain', 
                      'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI']
    
    for col in numeric_columns:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')
    
    # Create region column (0 for Bejaia, 1 for Sidi-Bel-Abbes)
    mid_point = len(data) // 2
    data['region'] = [0 if i < mid_point else 1 for i in range(len(data))]
    
    # Clean column names first
    data.columns = data.columns.str.strip()
    
    # Create classes mapping (fire = 1, not fire = 0)
    data['classes_numeric'] = data['Classes'].apply(lambda x: 1 if 'fire' in str(x).lower() and 'not' not in str(x).lower() else 0)
    
    # Clean the Classes column
    data['Classes'] = data['Classes'].str.strip()
    
    # Reset index
    data = data.reset_index(drop=True)
    
    print(f"Dataset loaded and cleaned. Shape: {data.shape}")
    return data

def prepare_features_target(data):
    """Prepare features and target variable"""
    
    # Features for prediction (matching the app's expected input)
    feature_columns = ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'classes_numeric', 'region']
    
    X = data[feature_columns].copy()
    y = data['FWI'].copy()  # Target is Fire Weather Index
    
    # Remove any rows with NaN values
    mask = ~(X.isna().any(axis=1) | y.isna())
    X = X[mask]
    y = y[mask]
    
    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")
    print(f"Feature columns: {list(X.columns)}")
    
    return X, y

def train_model():
    """Train the Ridge regression model"""
    print("Starting model training...")
    
    # Load and prepare data
    data = load_and_clean_data()
    X, y = prepare_features_target(data)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Ridge regression model
    ridge_model = Ridge(alpha=1.0, random_state=42)
    ridge_model.fit(X_train_scaled, y_train)
    
    # Evaluate model
    y_pred_train = ridge_model.predict(X_train_scaled)
    y_pred_test = ridge_model.predict(X_test_scaled)
    
    train_mse = mean_squared_error(y_train, y_pred_train)
    test_mse = mean_squared_error(y_test, y_pred_test)
    train_r2 = r2_score(y_train, y_pred_train)
    test_r2 = r2_score(y_test, y_pred_test)
    
    print(f"Training MSE: {train_mse:.4f}")
    print(f"Test MSE: {test_mse:.4f}")
    print(f"Training R²: {train_r2:.4f}")
    print(f"Test R²: {test_r2:.4f}")
    
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Save model and scaler
    with open('models/Ridge_model.pkl', 'wb') as f:
        pickle.dump(ridge_model, f)
    print("Ridge model saved to models/Ridge_model.pkl")
    
    with open('models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    print("Scaler saved to models/scaler.pkl")
    
    # Test loading the saved models
    print("\nTesting saved models...")
    with open('models/Ridge_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    
    with open('models/scaler.pkl', 'rb') as f:
        loaded_scaler = pickle.load(f)
    
    # Test prediction with loaded models
    sample_input = X_test.iloc[0:1].values
    scaled_input = loaded_scaler.transform(sample_input)
    prediction = loaded_model.predict(scaled_input)
    
    print(f"Sample prediction test: {prediction[0]:.2f}")
    print("Models successfully saved and tested!")
    
    return ridge_model, scaler

if __name__ == "__main__":
    train_model()