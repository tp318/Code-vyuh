# Sustainability Engine Module
# This module handles sustainability calculations and carbon footprint tracking

import pandas as pd
import numpy as np
from typing import Dict

class SustainabilityEngine:
    """Sustainability calculation engine for logistics operations"""
    
    def __init__(self):
        """Initialize the sustainability engine"""
        # Carbon emission factors (kg CO2e per km)
        self.emission_factors = {
            'truck': 0.1,      # Heavy goods vehicle
            'van': 0.06,       # Light commercial vehicle
            'bike': 0.0,       # Electric bike
            'electric_van': 0.02,  # Electric vehicle (grid emissions)
            'train': 0.04,     # Rail freight
            'ship': 0.03       # Sea freight
        }
        
        # Fuel efficiency factors (liters per 100km)
        self.fuel_efficiency = {
            'truck': 35.0,
            'van': 12.0,
            'bike': 0.0,
            'electric_van': 0.0,
            'train': 0.0,
            'ship': 0.0
        }
    
    def calculate(self, data: Dict) -> Dict:
        """
        Calculate carbon footprint for a shipment
        
        Args:
            data: Dictionary containing shipment details
            
        Returns:
            Dictionary with carbon footprint and sustainability score
        """
        # Extract parameters
        distance = data.get('distance', 100)  # km
        vehicle_type = data.get('vehicle_type', 'truck').lower()
        weight = data.get('weight', 1000)  # kg
        packaging_type = data.get('packaging', 'standard')  # standard, eco_friendly, minimal
        
        # Get emission factor for vehicle type
        emission_factor = self.emission_factors.get(vehicle_type, 0.1)
        
        # Calculate base carbon emissions
        base_carbon = distance * emission_factor
        
        # Weight adjustment (heavier loads = more emissions)
        weight_factor = 1.0 + (weight / 10000)  # Additional emissions per ton
        
        # Packaging impact
        packaging_impact = {
            'standard': 1.0,
            'eco_friendly': 0.7,
            'minimal': 0.8,
            'excessive': 1.3
        }.get(packaging_type.lower(), 1.0)
        
        # Calculate total carbon footprint
        total_carbon = base_carbon * weight_factor * packaging_impact
        
        # Calculate sustainability score (0-100)
        sustainability_score = self._calculate_sustainability_score(
            total_carbon, distance, vehicle_type, packaging_type
        )
        
        return {
            'carbon': round(total_carbon, 3),
            'score': round(sustainability_score, 2),
            'vehicle_emission_factor': emission_factor,
            'weight_factor': weight_factor
        }
    
    def _calculate_sustainability_score(self, carbon: float, distance: float, 
                                      vehicle_type: str, packaging_type: str) -> float:
        """
        Calculate overall sustainability score
        
        Args:
            carbon: Total carbon emissions in kg CO2e
            distance: Distance traveled in km
            vehicle_type: Type of vehicle used
            packaging_type: Type of packaging used
            
        Returns:
            Sustainability score from 0 to 100
        """
        # Start with base score
        score = 100.0
        
        # Deduct points based on carbon emissions per km
        carbon_per_km = carbon / distance if distance > 0 else carbon
        score -= min(40, carbon_per_km * 100)  # Max 40 point deduction
        
        # Bonus for eco-friendly vehicles
        vehicle_bonus = {
            'bike': 20,
            'electric_van': 15,
            'train': 10,
            'ship': 5,
            'van': 5,
            'truck': 0
        }.get(vehicle_type.lower(), 0)
        score += vehicle_bonus
        
        # Bonus for eco-friendly packaging
        packaging_bonus = {
            'eco_friendly': 15,
            'minimal': 10,
            'standard': 0,
            'excessive': -10
        }.get(packaging_type.lower(), 0)
        score += packaging_bonus
        
        # Ensure score is between 0 and 100
        return max(0, min(100, score))
