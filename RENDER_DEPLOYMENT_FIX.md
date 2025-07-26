# Fix Your Render Deployment - 502 Error

## The Problem
Your app is getting HTTP 502 error because Render can't start your Flask application properly.

## The Solution
You need to add these 3 files to your GitHub repository:

### 1. Create `requirements.txt` (exact filename)
```
Flask==3.0.3
pandas==2.1.4
numpy==1.26.4
scikit-learn==1.4.2
gunicorn==21.2.0
Werkzeug==3.0.3
```

### 2. Update your `main.py` to read PORT environment variable:
```python
import os
from app import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
```

### 3. Create `render.yaml` configuration:
```yaml
services:
  - type: web
    name: algerian-forest-fire-prediction
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn --bind 0.0.0.0:$PORT main:app
    plan: free
    region: oregon
    branch: main
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.4
```

## Steps to Fix:
1. Add these 3 files to your GitHub repository
2. In Render dashboard, go to your service settings
3. Set Build Command: `pip install -r requirements.txt`
4. Set Start Command: `gunicorn --bind 0.0.0.0:$PORT main:app`
5. Redeploy your service

Your app will work perfectly after these changes!