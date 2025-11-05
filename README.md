
## 🔄 CI/CD Pipeline

Continues Integration/ Continues Development

Basically its cover 3 major stage
1. Build
2. Test
3. Deploy

1. Build

   As per your project require.txt pipeline will create a virtual server and insatll all dependancy  & module that is known as build phase.

   If build phase complete it will go to next stage which is Testing & automation phase.

2. Testing Phase

   It cover your all testing like API giving 200 or not and expected result or not. 

   If this phase fully pass meaning all listed test cases passed it will go to deploy phase.

3. Deploye

   In this phase project is good to go on production branch. meaning it will install all module or requirment from project requeirment.txt into Server.

CICD is define in YML structure. on git hub we need to create .github folder and we can create as many as CICD files with extention .yml

Where to check pipeline is runing or its status?

   In github, select the repo, you will fine the 'Action' tab in this tab it will show status.

Added on ci-cd.yml for better understand..!

Basic creation of yml

Name: {name of the cicd template}

On: {This is phase where you need to mention on which branch change, you want to trigger the CICD}
example
On:  
   push:
      branches: [ main, develop ]
   pull_request:
      branches: [ main ]
Job: {this phase we declare test & deploye}


**WHEN YOU HAVE TIME I WILL SHOW YOU DEMO TOO..**


More overview;

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
