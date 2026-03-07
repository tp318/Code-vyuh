# Delay Prediction Module
# This module handles delay prediction using ML models

import pandas as pd
import numpy as np
from typing import Dict
import joblib
import os

class DelayPredictor:
    """Delay prediction engine for logistics operations"""
    
    def __init__(self, model_path: str = None):
        """
        Initialize the delay predictor
        
        Args:
            model_path: Path to pre-trained model file
        """
        self.model_path = model_path
        self.model = None
        
        if model_path and os.path.exists(model_path):
            try:
                self.model = joblib.load(model_path)
            except Exception as e:
                print(f"Warning: Could not load model from {model_path}: {e}")
                self.model = self._create_default_model()
        else:
            self.model = self._create_default_model()
    
    def _create_default_model(self):
        """Create a simple rule-based model for delay prediction"""
        return None  # Using rule-based approach
    
    def predict(self, data: Dict) -> Dict:
        """
        Predict delivery delay based on input features
        
        Args:
            data: Dictionary containing features like distance, traffic, weather, etc.
            
        Returns:
            Dictionary with prediction results
        """
        # Extract features
        distance = data.get('distance', 100)  # km
        traffic_level = data.get('traffic', 'medium')  # low, medium, high
        weather_condition = data.get('weather', 'clear')  # clear, rain, snow, storm
        time_of_day = data.get('time_of_day', 'day')  # day, night, peak
        vehicle_type = data.get('vehicle_type', 'truck')  # truck, van, bike
        
        # Base delay calculation
        base_delay = distance * 0.5  # 0.5 minutes per km
        
        # Traffic adjustment
        traffic_multiplier = {
            'low': 1.0,
            'medium': 1.3,
            'high': 1.8
        }.get(traffic_level.lower(), 1.3)
        
        # Weather adjustment
        weather_adjustment = {
            'clear': 0,
            'rain': 15,
            'snow': 30,
            'storm': 45,
            'fog': 20
        }.get(weather_condition.lower(), 0)
        
        # Time of day adjustment
        time_adjustment = {
            'day': 0,
            'night': 10,
            'peak': 25
        }.get(time_of_day.lower(), 0)
        
        # Vehicle type adjustment
        vehicle_factor = {
            'truck': 1.2,
            'van': 1.0,
            'bike': 0.8
        }.get(vehicle_type.lower(), 1.0)
        
        # Calculate final delay
        predicted_delay = (base_delay * traffic_multiplier + weather_adjustment + time_adjustment) * vehicle_factor
        
        # Calculate confidence (simplified)
        confidence = min(0.95, 0.7 + (0.05 * len(data)))  # More features = higher confidence
        
        return {
            'delay': round(predicted_delay, 2),
            'confidence': round(confidence, 3)
        }
