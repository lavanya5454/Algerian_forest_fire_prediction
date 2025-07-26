import pandas as pd
import numpy as np
import os
import logging

class DataProcessor:
    def __init__(self):
        self.data = None
        self.load_data()
    
    def load_data(self):
        """Load and process the Algerian forest fires dataset"""
        try:
            # Try to load the dataset
            data_path = "Algerian_forest_fires_dataset_UPDATE_1753524208988.csv"
            if not os.path.exists(data_path):
                logging.warning(f"Dataset file not found at {data_path}")
                self.create_sample_data()
                return
            
            # Read the dataset
            self.data = pd.read_csv(data_path, header=1)
            
            # Clean the data
            self.clean_data()
            
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            self.create_sample_data()
    
    def clean_data(self):
        """Clean and preprocess the dataset"""
        if self.data is None:
            return
        
        # Clean column names first
        self.data.columns = self.data.columns.str.strip()
        
        # Remove header rows that might be mixed in data
        self.data = self.data[self.data['day'] != 'Sidi-Bel Abbes Region Dataset']
        self.data = self.data[self.data['day'] != 'day']
        
        # Drop rows with missing values
        self.data = self.data.dropna()
        
        # Convert numeric columns
        numeric_columns = ['day', 'month', 'year', 'Temperature', 'RH', 'Ws', 'Rain', 
                          'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI']
        
        for col in numeric_columns:
            if col in self.data.columns:
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
        
        # Create region column based on row index (first half Bejaia, second half Sidi-Bel-Abbes)
        mid_point = len(self.data) // 2
        self.data['region'] = ['Bejaia' if i < mid_point else 'Sidi-Bel-Abbes' 
                              for i in range(len(self.data))]
        
        # Clean the Classes column
        if 'Classes' in self.data.columns:
            self.data['Classes'] = self.data['Classes'].str.strip()
        
        # Reset index
        self.data = self.data.reset_index(drop=True)
        
        logging.info(f"Data cleaned. Shape: {self.data.shape}")
    
    def create_sample_data(self):
        """Create sample data for demonstration if dataset not available"""
        logging.warning("Creating sample data for demonstration")
        
        # This is just for fallback - in production, real data should be used
        sample_data = {
            'day': list(range(1, 31)) * 8,
            'month': [6] * 120 + [7] * 120,
            'year': [2012] * 240,
            'Temperature': np.random.randint(20, 45, 240),
            'RH': np.random.randint(20, 90, 240),
            'Ws': np.random.randint(5, 25, 240),
            'Rain': np.random.uniform(0, 15, 240),
            'FFMC': np.random.uniform(20, 95, 240),
            'DMC': np.random.uniform(0, 60, 240),
            'DC': np.random.uniform(0, 200, 240),
            'ISI': np.random.uniform(0, 20, 240),
            'BUI': np.random.uniform(0, 70, 240),
            'FWI': np.random.uniform(0, 30, 240),
            'Classes': np.random.choice(['fire', 'not fire'], 240),
            'region': ['Bejaia'] * 120 + ['Sidi-Bel-Abbes'] * 120
        }
        
        self.data = pd.DataFrame(sample_data)
    
    def get_dashboard_data(self):
        """Prepare data for dashboard visualizations"""
        if self.data is None:
            return {}
        
        try:
            # Basic statistics
            stats = {
                'total_records': len(self.data),
                'fire_incidents': len(self.data[self.data['Classes'] == 'fire']),
                'no_fire_incidents': len(self.data[self.data['Classes'] == 'not fire']),
                'avg_temperature': round(self.data['Temperature'].mean(), 1),
                'avg_humidity': round(self.data['RH'].mean(), 1),
                'avg_fwi': round(self.data['FWI'].mean(), 2)
            }
            
            # Monthly fire incidents
            monthly_fires = self.data[self.data['Classes'] == 'fire'].groupby('month').size().to_dict()
            
            # Temperature vs FWI correlation
            temp_fwi = self.data[['Temperature', 'FWI']].to_dict('records')
            
            # Regional comparison
            regional_stats = self.data.groupby('region').agg({
                'FWI': 'mean',
                'Temperature': 'mean',
                'RH': 'mean'
            }).round(2).to_dict('index')
            
            # Risk distribution
            risk_dist = {}
            for _, row in self.data.iterrows():
                risk = self.get_risk_level(row['FWI'])
                risk_dist[risk] = risk_dist.get(risk, 0) + 1
            
            # Weather conditions distribution
            weather_conditions = {
                'high_temp': len(self.data[self.data['Temperature'] > 35]),
                'low_humidity': len(self.data[self.data['RH'] < 30]),
                'high_wind': len(self.data[self.data['Ws'] > 20]),
                'rainy_days': len(self.data[self.data['Rain'] > 0])
            }
            
            return {
                'stats': stats,
                'monthly_fires': monthly_fires,
                'temp_fwi_correlation': temp_fwi,
                'regional_stats': regional_stats,
                'risk_distribution': risk_dist,
                'weather_conditions': weather_conditions
            }
            
        except Exception as e:
            logging.error(f"Error preparing dashboard data: {e}")
            return {}
    
    def get_risk_level(self, fwi_value):
        """Determine risk level based on FWI value"""
        if fwi_value < 1:
            return "Very Low"
        elif fwi_value < 4:
            return "Low"
        elif fwi_value < 10:
            return "Moderate"
        elif fwi_value < 17:
            return "High"
        else:
            return "Very High"
