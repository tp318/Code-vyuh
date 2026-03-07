# Logistics AI Application
# Main application file for logistics management system

from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os
from modules.delay_prediction import DelayPredictor
from modules.sustainability_engine import SustainabilityEngine
from modules.route_optimizer import RouteOptimizer

app = Flask(__name__)

# Initialize components
delay_predictor = None
sustainability_engine = None
route_optimizer = None

def initialize_models():
    """Initialize ML models and engines"""
    global delay_predictor, sustainability_engine, route_optimizer
    
    # Load delay prediction model
    model_path = 'models/delay_model.pkl'
    if os.path.exists(model_path):
        delay_predictor = DelayPredictor(model_path)
    
    # Initialize other engines
    sustainability_engine = SustainabilityEngine()
    route_optimizer = RouteOptimizer()

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Logistics AI API',
        'endpoints': {
            '/predict-delay': 'POST - Predict delivery delay',
            '/calculate-carbon': 'POST - Calculate carbon footprint',
            '/optimize-route': 'POST - Optimize delivery route',
            '/data/upload': 'POST - Upload logistics data'
        }
    })

@app.route('/predict-delay', methods=['POST'])
def predict_delay():
    """Predict delivery delay based on input features"""
    try:
        data = request.json
        
        if delay_predictor is None:
            return jsonify({'error': 'Delay model not loaded'}), 500
        
        prediction = delay_predictor.predict(data)
        
        return jsonify({
            'predicted_delay': prediction['delay'],
            'confidence': prediction['confidence'],
            'unit': 'minutes'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/calculate-carbon', methods=['POST'])
def calculate_carbon():
    """Calculate carbon footprint for a shipment"""
    try:
        data = request.json
        
        if sustainability_engine is None:
            return jsonify({'error': 'Sustainability engine not initialized'}), 500
        
        result = sustainability_engine.calculate(data)
        
        return jsonify({
            'carbon_footprint': result['carbon'],
            'unit': 'kg CO2e',
            'sustainability_score': result['score']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/optimize-route', methods=['POST'])
def optimize_route():
    """Optimize delivery route"""
    try:
        data = request.json
        
        if route_optimizer is None:
            return jsonify({'error': 'Route optimizer not initialized'}), 500
        
        result = route_optimizer.optimize(data)
        
        return jsonify({
            'optimized_route': result['route'],
            'total_distance': result['distance'],
            'estimated_time': result['time'],
            'fuel_savings': result['savings']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/data/upload', methods=['POST'])
def upload_data():
    """Upload logistics data"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Save uploaded file
        data_path = 'data/logistics_data.csv'
        file.save(data_path)
        
        return jsonify({
            'message': 'File uploaded successfully',
            'path': data_path
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    initialize_models()
    app.run(debug=True, host='0.0.0.0', port=5000)
