#!/usr/bin/env python3
"""
Simple script to test all API endpoints locally
Run this script to verify all 5 endpoints return 200 status
"""

import requests
import time
import subprocess
import os
import sys

def test_endpoints():
    """Test all API endpoints and verify they return 200 status"""
    base_url = "http://localhost:5000"
    endpoints = [
        ("/", "Home endpoint"),
        ("/health", "Health check endpoint"),
        ("/users", "Users endpoint"),
        ("/products", "Products endpoint"),
        ("/status", "Status endpoint")
    ]
    
    print("🚀 Testing Simple REST API Endpoints")
    print("=" * 50)
    
    all_passed = True
    
    for endpoint, description in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            status = "✅ PASS" if response.status_code == 200 else "❌ FAIL"
            print(f"{status} {endpoint:<12} - {description:<20} (Status: {response.status_code})")
            
            if response.status_code != 200:
                all_passed = False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ FAIL {endpoint:<12} - {description:<20} (Error: {str(e)})")
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("🎉 All 5 API endpoints are returning 200 status!")
        return True
    else:
        print("⚠️  Some endpoints failed. Check the API server.")
        return False

def main():
    """Main function to run the tests"""
    print("Starting API endpoint tests...")
    print("Make sure the Flask app is running on http://localhost:5000")
    print("Run: python app.py")
    print()
    
    # Wait a moment for user to start the server
    input("Press Enter when the Flask app is running...")
    
    success = test_endpoints()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
