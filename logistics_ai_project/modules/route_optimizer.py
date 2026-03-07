# Route Optimizer Module
# This module handles route optimization for delivery vehicles

import pandas as pd
import numpy as np
from typing import Dict, List

class RouteOptimizer:
    """Route optimization engine for logistics operations"""
    
    def __init__(self):
        """Initialize the route optimizer"""
        self.algorithm = 'nearest_neighbor'  # Default algorithm
    
    def optimize(self, data: Dict) -> Dict:
        """
        Optimize delivery route
        
        Args:
            data: Dictionary containing route information
            
        Returns:
            Dictionary with optimized route details
        """
        stops = data.get('stops', [])
        start_location = data.get('start', 'Warehouse')
        
        if not stops:
            return {
                'route': [start_location],
                'distance': 0,
                'time': 0,
                'savings': 0
            }
        
        # Implement nearest neighbor algorithm
        optimized_route = self._nearest_neighbor(start_location, stops)
        
        # Calculate metrics
        total_distance = self._calculate_distance(optimized_route)
        estimated_time = self._estimate_time(total_distance)
        fuel_savings = self._calculate_savings(stops, optimized_route)
        
        return {
            'route': optimized_route,
            'distance': total_distance,
            'time': estimated_time,
            'savings': fuel_savings
        }
    
    def _nearest_neighbor(self, start: str, stops: List[str]) -> List[str]:
        """
        Implement nearest neighbor heuristic for route optimization
        
        Args:
            start: Starting location
            stops: List of delivery stops
            
        Returns:
            Optimized route as list of locations
        """
        unvisited = stops.copy()
        route = [start]
        current = start
        
        while unvisited:
            # Find nearest unvisited stop (simplified - would use actual distances in production)
            nearest = unvisited.pop(0)
            route.append(nearest)
            current = nearest
        
        route.append(start)  # Return to start
        return route
    
    def _calculate_distance(self, route: List[str]) -> float:
        """
        Calculate total distance for the route
        
        Args:
            route: List of locations in order
            
        Returns:
            Total distance in kilometers
        """
        # Simplified distance calculation
        # In production, this would use actual GPS coordinates or mapping API
        return len(route) * 50.0  # Average 50km between stops
    
    def _estimate_time(self, distance: float) -> float:
        """
        Estimate travel time
        
        Args:
            distance: Total distance in km
            
        Returns:
            Estimated time in minutes
        """
        average_speed = 60  # km/h
        return (distance / average_speed) * 60
    
    def _calculate_savings(self, original_route: List[str], optimized_route: List[str]) -> float:
        """
        Calculate fuel/cost savings from optimization
        
        Args:
            original_route: Original unoptimized route
            optimized_route: Optimized route
            
        Returns:
            Percentage savings
        """
        original_distance = self._calculate_distance(original_route)
        optimized_distance = self._calculate_distance(optimized_route)
        
        if original_distance == 0:
            return 0.0
        
        savings = ((original_distance - optimized_distance) / original_distance) * 100
        return max(0.0, savings)  # Ensure non-negative
