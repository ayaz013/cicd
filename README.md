# Simple REST API with CI/CD Pipeline

A simple Python Flask REST API with 5 endpoints that return 200 responses, complete with automated CI/CD pipeline using GitHub Actions.

## 🚀 Features

- **5 REST API Endpoints** that return 200 status codes
- **Automated Testing** with pytest
- **CI/CD Pipeline** using GitHub Actions
- **Code Quality Checks** with flake8 linting
- **Automated Deployment** simulation

## 📋 API Endpoints

| Endpoint | Method | Description | Response |
|----------|--------|-------------|----------|
| `/` | GET | Home endpoint with welcome message | 200 |
| `/health` | GET | Health check endpoint | 200 |
| `/users` | GET | Get list of users | 200 |
| `/products` | GET | Get list of products | 200 |
| `/status` | GET | API status information | 200 |

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd CICD
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Test the API**
   ```bash
   # Test individual endpoints
   curl http://localhost:5000/
   curl http://localhost:5000/health
   curl http://localhost:5000/users
   curl http://localhost:5000/products
   curl http://localhost:5000/status
   
   # Run automated tests
   python -m pytest test_api.py -v
   ```

## 🧪 Testing

The project includes comprehensive tests to verify all 5 API endpoints return 200 status codes:

```bash
# Run all tests
python -m pytest test_api.py -v

# Run with coverage
python -m pytest test_api.py --cov=app
```

### Test Coverage
- ✅ Home endpoint (`/`) - 200 status
- ✅ Health endpoint (`/health`) - 200 status  
- ✅ Users endpoint (`/users`) - 200 status
- ✅ Products endpoint (`/products`) - 200 status
- ✅ Status endpoint (`/status`) - 200 status

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:

### Pipeline Stages

1. **Code Quality Check**
   - Python syntax validation
   - Flake8 linting
   - Code complexity analysis

2. **Testing**
   - Automated pytest execution
   - Individual endpoint testing with curl
   - Verification of 200 status codes

3. **Deployment** (on main branch)
   - Production deployment simulation
   - Success notification

### Workflow Triggers
- Push to `main` or `develop` branches
- Pull requests to `main` branch

## 📁 Project Structure

```
CICD/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions workflow
├── app.py                     # Main Flask application
├── test_api.py               # Test suite for API endpoints
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🔧 Configuration

### Environment Variables
- `PORT`: Server port (default: 5000)
- `ENVIRONMENT`: Environment name (default: development)

### Dependencies
- **Flask 2.3.3**: Web framework
- **pytest 7.4.3**: Testing framework
- **pytest-flask 1.2.0**: Flask testing utilities
- **requests 2.31.0**: HTTP library for testing

## 🚀 Deployment

The CI/CD pipeline automatically:
1. Runs tests on every push/PR
2. Validates code quality
3. Deploys to production (simulated) when tests pass on main branch

## 📊 Monitoring

All endpoints include health check capabilities:
- `/health` - Basic health status
- `/status` - Detailed API status and environment info

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/your-username/CICD/issues) page
2. Create a new issue with detailed description
3. Include steps to reproduce the problem

---

**Happy Coding! 🎉**