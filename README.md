# oc-pipelines-project 
 
OpenShift Pipelines CI/CD project with Python, Tekton, and GitHub Actions 
 
## Project Name 
oc-pipelines-project 
 
## Description 
This project demonstrates a CI/CD pipeline using: 
- GitHub Actions with flake8 linting and nose tests 
- Tekton tasks for OpenShift pipelines 
- Python application with unit tests 
 
## Structure 
- `app/` - Python application code 
- `tests/` - Unit tests using nose 
- `.github/workflows/` - GitHub Actions workflow with flake8 and nose 
- `.tekton/` - Tekton tasks (cleanup and nose-test) 
