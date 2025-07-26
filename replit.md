# Algerian Forest Fire Prediction System

## Overview

This is a Flask-based web application that predicts forest fire risk using machine learning. The system uses the Fire Weather Index (FWI) to assess fire danger based on meteorological conditions in Algeria's Bejaia and Sidi-Bel-Abbes regions. The application employs a Ridge regression model trained on weather data to provide fire risk predictions.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: HTML templates with Bootstrap 5 for responsive design
- **Styling**: Custom CSS with forest fire theme using CSS variables
- **JavaScript**: Vanilla JavaScript for form validation, chart rendering (Chart.js), and interactive features
- **Template Engine**: Jinja2 (Flask's default templating engine)

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Structure**: Modular design with separate data processing component
- **Model Serving**: Pre-trained Ridge regression model loaded via pickle
- **Data Processing**: Dedicated DataProcessor class for handling dataset operations

### Key Technologies
- **Python**: Flask, pandas, numpy, scikit-learn
- **Frontend**: Bootstrap 5, Font Awesome icons, Chart.js
- **Machine Learning**: Ridge regression with StandardScaler for feature normalization
- **Data Format**: CSV dataset processing with pandas

## Key Components

### Core Application (`app.py`)
- Flask application setup with security configurations
- Route handlers for main pages (home, prediction, dashboard)
- Model and scaler loading with error handling
- Categorical mappings for regions and risk classes

### Data Processing (`data_processor.py`)
- DataProcessor class for dataset management
- Data cleaning and preprocessing functions
- Handles missing Algerian forest fires dataset with fallback sample data
- Numeric data type conversion and validation

### Machine Learning Pipeline
- **Model**: Ridge regression (stored as `Ridge_model.pkl`)
- **Preprocessing**: StandardScaler (stored as `scaler.pkl`)
- **Features**: Weather conditions (Temperature, RH, Ws, Rain) and fire indices (FFMC, DMC, DC, ISI, BUI, FWI)
- **Output**: Fire Weather Index prediction with risk level classification

### Frontend Components
- **Base Template**: Consistent navigation and layout structure
- **Home Page**: Hero section with system overview and feature highlights
- **Prediction Form**: Interactive form with real-time validation
- **Dashboard**: Analytics and visualization interface
- **Results Page**: Formatted prediction output with risk interpretation

## Data Flow

1. **User Input**: Weather conditions and fire indices entered through web form
2. **Validation**: Client-side JavaScript validation with server-side verification
3. **Preprocessing**: Input data scaled using pre-trained StandardScaler
4. **Prediction**: Ridge regression model generates FWI prediction
5. **Classification**: FWI value mapped to risk level (low, moderate, high, very high)
6. **Response**: Results displayed with risk interpretation and recommendations

### Input Parameters
- Temperature (°C)
- Relative Humidity (%)
- Wind Speed (km/h)
- Rainfall (mm)
- Fire Weather Indices: FFMC, DMC, DC, ISI, BUI, FWI

### Output Format
- Numerical FWI prediction
- Categorical risk level
- Risk interpretation and safety recommendations

## External Dependencies

### Python Packages
- **Flask**: Web framework and routing
- **pandas**: Data manipulation and CSV processing
- **numpy**: Numerical computations
- **scikit-learn**: Machine learning model and preprocessing
- **werkzeug**: WSGI utilities and middleware

### Frontend Libraries
- **Bootstrap 5**: CSS framework for responsive design
- **Font Awesome**: Icon library
- **Chart.js**: Data visualization for dashboard

### Data Dependencies
- Algerian forest fires dataset (CSV format)
- Pre-trained Ridge regression model (pickle file)
- StandardScaler for feature normalization (pickle file)

## Deployment Strategy

### Development Setup
- Flask development server with debug mode
- Host configuration: `0.0.0.0:5000`
- Environment-based secret key management
- Proxy fix middleware for deployment behind reverse proxy

### Production Considerations
- **WSGI Server**: Gunicorn specified in requirements
- **Security**: Environment-based secret key, proxy fix middleware
- **Error Handling**: Comprehensive logging and graceful fallbacks
- **Static Assets**: CSS and JavaScript served through Flask's static file handling

### File Structure
```
/
├── app.py                 # Main Flask application
├── main.py               # Application entry point
├── data_processor.py     # Data handling utilities
├── models/               # ML models and preprocessors
├── templates/            # HTML templates
├── static/               # CSS, JavaScript, images
└── attached_assets/      # Legacy/reference files
```

### Environment Requirements
- Python environment with scientific computing stack
- Model files must be present in `models/` directory
- Dataset file expected in root directory
- Static assets served from `static/` directory

The application is designed to be self-contained with fallback mechanisms for missing data files, making it suitable for various deployment scenarios from development to production environments.