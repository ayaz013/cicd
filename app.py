from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    """Home endpoint - returns welcome message"""
    return jsonify({
        "message": "Welcome to Simple REST API",
        "status": "success",
        "version": "1.0.0"
    }), 200

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "simple-api"
    }), 500

@app.route('/users')
def get_users():
    """Get users endpoint"""
    users = [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
    ]
    return jsonify({
        "users": users,
        "count": len(users)
    }), 200

@app.route('/products')
def get_products():
    """Get products endpoint"""
    products = [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Mouse", "price": 29.99}
    ]
    return jsonify({
        "products": products,
        "count": len(products)
    }), 200

@app.route('/status')
def get_status():
    """Status endpoint"""
    return jsonify({
        "api_status": "running",
        "uptime": "active",
        "environment": os.getenv("ENVIRONMENT", "development")
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
