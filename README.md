# Algerian Forest Fire Prediction System

A comprehensive machine learning web application for predicting forest fire risk using the Fire Weather Index (FWI) based on meteorological conditions in Algeria's Bejaia and Sidi-Bel-Abbes regions.

## 🔥 Features

- **Machine Learning Model**: Ridge regression with 98.45% accuracy
- **Interactive Web Interface**: Professional UI built with Flask and Bootstrap
- **Real-time Predictions**: Input weather conditions and get instant FWI predictions
- **Analytics Dashboard**: Comprehensive data visualizations and insights
- **Risk Assessment**: Categorizes predictions from Very Low to Very High risk
- **Regional Support**: Covers Bejaia and Sidi-Bel-Abbes regions of Algeria

## 🚀 Demo

The application provides:
- **Home Page**: Overview of the system and Fire Weather Index explanation
- **Prediction Form**: Interactive form for weather data input
- **Results Page**: Detailed prediction results with risk interpretation
- **Dashboard**: Analytics with charts showing fire incidents, risk distribution, and regional comparisons

## 📊 Model Performance

- **Test Accuracy**: 98.45% R² score
- **Training Accuracy**: 97.36% R² score
- **Dataset**: 243 real records from Algerian forest fire data (2012)
- **Algorithm**: Ridge Regression with L2 regularization
- **Features**: Temperature, Humidity, Wind Speed, Rainfall, FFMC, DMC, DC, ISI, BUI

## 🛠️ Technologies Used

### Backend
- **Python 3.11**
- **Flask** - Web framework
- **scikit-learn** - Machine learning
- **pandas** - Data processing
- **numpy** - Numerical computing
- **pickle** - Model serialization

### Frontend
- **Bootstrap 5** - CSS framework
- **Chart.js** - Data visualization
- **Font Awesome** - Icons
- **Custom CSS** - Forest fire theme

### Deployment
- **Render**
## 📁 Project Structure

```
├── app.py                  # Main Flask application
├── main.py                 # Application entry point
├── data_processor.py       # Data handling utilities
├── train_model.py         # Model training script
├── models/                # ML models and preprocessors
│   ├── Ridge_model.pkl    # Trained Ridge regression model
│   └── scaler.pkl         # Feature scaler
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── predict.html      # Prediction form
│   ├── results.html      # Results page
│   └── dashboard.html    # Analytics dashboard
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Custom styling
│   └── js/
│       ├── dashboard.js  # Dashboard charts
│       └── predictions.js # Form validation
└── Algerian_forest_fires_dataset_UPDATE_1753524208988.csv
```

## 🚦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd algerian-forest-fire-prediction
   ```

2. **Install dependencies**
   ```bash
   pip install flask pandas numpy scikit-learn gunicorn werkzeug
   ```

3. **Train the model** (optional - models are pre-trained)
   ```bash
   python train_model.py
   ```

4. **Run the application**
   ```bash
   # Development
   python main.py
   
   # Production
   gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
   ```

5. **Access the application**
   - Open your browser to `http://localhost:5000`

## 📝 Usage

### Making Predictions

1. Navigate to the **Predict** page
2. Enter weather conditions:
   - Temperature (°C)
   - Relative Humidity (%)
   - Wind Speed (km/h)
   - Rainfall (mm)

3. Enter fire weather components:
   - FFMC (Fine Fuel Moisture Code)
   - DMC (Duff Moisture Code)
   - DC (Drought Code)
   - ISI (Initial Spread Index)
   - BUI (Buildup Index)

4. Select region (Bejaia or Sidi-Bel-Abbes)
5. Choose initial risk class
6. Click **Calculate Fire Weather Index**

### Understanding Results

The system provides:
- **FWI Value**: Numerical Fire Weather Index
- **Risk Level**: Categorized risk (Very Low to Very High)
- **Risk Interpretation**: Detailed explanation and recommendations
- **Input Summary**: Review of entered parameters

## 📈 Fire Weather Index (FWI) System

The FWI system combines weather observations and fuel moisture codes:

- **FFMC**: Moisture content of fine fuels
- **DMC**: Moisture content of moderate depth organic layers
- **DC**: Moisture content of deep organic layers
- **ISI**: Expected rate of fire spread
- **BUI**: Total amount of fuel available

### Risk Levels
- **Very Low (0-1)**: Minimal fire danger
- **Low (1-4)**: Low fire danger
- **Moderate (4-10)**: Moderate fire danger
- **High (10-17)**: High fire danger
- **Very High (17+)**: Extreme fire danger

## 🔧 Configuration

### Environment Variables
- `SESSION_SECRET`: Flask session secret key (auto-generated if not set)

### Model Files
- Models are automatically loaded from the `models/` directory
- If models are missing, the system will use fallback sample data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Algerian forest fire dataset from research institutions
- Fire Weather Index system from Canadian Forest Service
- Bootstrap and Chart.js communities
- Flask and scikit-learn developers

**Built with ❤️ for forest fire prevention and environmental protection**
