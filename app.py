import os
import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from werkzeug.middleware.proxy_fix import ProxyFix
import logging
from data_processor import DataProcessor

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-for-forest-fire-prediction")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Initialize data processor
data_processor = DataProcessor()

# Load model and scaler
try:
    ridge_model = pickle.load(open("models/Ridge_model.pkl", "rb"))
    scaler = pickle.load(open("models/scaler.pkl", "rb"))
    logging.info("Model and scaler loaded successfully")
except Exception as e:
    logging.error(f"Error loading model or scaler: {e}")
    ridge_model = None
    scaler = None

# Categorical mappings
class_mapping = {
    "low": 0,
    "moderate": 1,
    "high": 2,
    "very high": 3
}

region_mapping = {
    "bejaia": 0,
    "sidi-bel-abbes": 1
}

@app.route("/")
def index():
    """Landing page with app information"""
    return render_template("index.html")

@app.route("/predict")
def predict_page():
    """Prediction form page"""
    return render_template("predict.html")

@app.route("/dashboard")
def dashboard():
    """Dashboard with data insights"""
    try:
        # Get dashboard data
        dashboard_data = data_processor.get_dashboard_data()
        return render_template("dashboard.html", data=dashboard_data)
    except Exception as e:
        logging.error(f"Error loading dashboard data: {e}")
        flash("Error loading dashboard data. Please try again.", "error")
        return render_template("dashboard.html", data=None)

@app.route("/predict", methods=['POST'])
def predict_datapoint():
    """Handle prediction requests"""
    if not ridge_model or not scaler:
        flash("Model not available. Please contact administrator.", "error")
        return redirect(url_for('predict_page'))
    
    try:
        # Extract form data
        temperature = float(request.form.get("Temperature"))
        rh = float(request.form.get("RH"))
        ws = float(request.form.get("Ws"))
        rain = float(request.form.get("Rain"))
        ffmc = float(request.form.get("FFMC"))
        dmc = float(request.form.get("DMC"))
        dc = float(request.form.get("DC"))
        isi = float(request.form.get("ISI"))
        bui = float(request.form.get("BUI"))
        
        # Handle categorical variables
        classes_str = request.form.get("Classes", "").lower()
        region_str = request.form.get("Region", "").lower()
        
        if classes_str not in class_mapping:
            flash("Invalid class selection", "error")
            return redirect(url_for('predict_page'))
        
        if region_str not in region_mapping:
            flash("Invalid region selection", "error")
            return redirect(url_for('predict_page'))
        
        classes = class_mapping[classes_str]
        region = region_mapping[region_str]
        
        # Prepare input data (matching the order expected by the model)
        input_data = np.array([[temperature, rh, ws, rain, ffmc, dmc, dc, isi, bui, classes, region]])
        
        # Scale the input data
        scaled_data = scaler.transform(input_data)
        
        # Make prediction
        prediction = ridge_model.predict(scaled_data)[0]
        
        # Determine risk level based on FWI value
        risk_level = data_processor.get_risk_level(prediction)
        
        # Prepare result data
        result_data = {
            'fwi_value': round(prediction, 2),
            'risk_level': risk_level,
            'input_data': {
                'temperature': temperature,
                'rh': rh,
                'ws': ws,
                'rain': rain,
                'ffmc': ffmc,
                'dmc': dmc,
                'dc': dc,
                'isi': isi,
                'bui': bui,
                'classes': classes_str.title(),
                'region': region_str.title()
            }
        }
        
        return render_template('results.html', result=result_data)
        
    except ValueError as e:
        flash("Please enter valid numeric values for all fields.", "error")
        return redirect(url_for('predict_page'))
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        flash("An error occurred during prediction. Please try again.", "error")
        return redirect(url_for('predict_page'))

@app.route("/api/dashboard-data")
def api_dashboard_data():
    """API endpoint for dashboard data"""
    try:
        dashboard_data = data_processor.get_dashboard_data()
        return jsonify(dashboard_data)
    except Exception as e:
        logging.error(f"API error: {e}")
        return jsonify({"error": "Unable to fetch dashboard data"}), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('base.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('base.html'), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
