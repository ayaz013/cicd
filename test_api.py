import pytest
import requests
import time
import subprocess
import os
from threading import Thread

class TestAPIEndpoints:
    """Test class to verify all API endpoints return 200 status"""
    
    @classmethod
    def setup_class(cls):
        """Start the Flask app in a separate thread for testing"""
        cls.app_process = None
        cls.base_url = "http://localhost:5000"
        
        # Start the Flask app
        def run_app():
            os.system("python app.py")
        
        cls.app_thread = Thread(target=run_app, daemon=True)
        cls.app_thread.start()
        
        # Wait for the app to start
        time.sleep(3)
    
    @classmethod
    def teardown_class(cls):
        """Clean up after tests"""
        if cls.app_process:
            cls.app_process.terminate()
    
    def test_home_endpoint(self):
        """Test the home endpoint returns 200"""
        response = requests.get(f"{self.base_url}/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "Welcome to Simple REST API" in data["message"]
    
    def test_health_endpoint(self):
        """Test the health endpoint returns 200"""
        response = requests.get(f"{self.base_url}/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "simple-api"
    
    def test_users_endpoint(self):
        """Test the users endpoint returns 200"""
        response = requests.get(f"{self.base_url}/users")
        assert response.status_code == 200
        data = response.json()
        assert "users" in data
        assert "count" in data
        assert data["count"] == 2
        assert len(data["users"]) == 2
    
    def test_products_endpoint(self):
        """Test the products endpoint returns 200"""
        response = requests.get(f"{self.base_url}/products")
        assert response.status_code == 200
        data = response.json()
        assert "products" in data
        assert "count" in data
        assert data["count"] == 2
        assert len(data["products"]) == 2
    
    def test_status_endpoint(self):
        """Test the status endpoint returns 200"""
        response = requests.get(f"{self.base_url}/status")
        assert response.status_code == 200
        data = response.json()
        assert data["api_status"] == "running"
        assert data["uptime"] == "active"
        assert "environment" in data

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
