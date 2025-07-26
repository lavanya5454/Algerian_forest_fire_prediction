# Files to Download for GitHub Repository

## Core Application Files (Required)
1. **app.py** - Main Flask application
2. **main.py** - Application entry point  
3. **data_processor.py** - Data handling utilities
4. **train_model.py** - Model training script

## Dataset (Required)
5. **Algerian_forest_fires_dataset_UPDATE_1753524208988.csv** - Original dataset

## Pre-trained Models (Required)
6. **models/Ridge_model.pkl** - Trained Ridge regression model
7. **models/scaler.pkl** - Feature scaling model

## Templates (Required)
8. **templates/base.html** - Base template with navigation
9. **templates/index.html** - Home page
10. **templates/predict.html** - Prediction form
11. **templates/results.html** - Results display
12. **templates/dashboard.html** - Analytics dashboard

## Static Assets (Required)
13. **static/css/style.css** - Custom styling
14. **static/js/dashboard.js** - Dashboard charts
15. **static/js/predictions.js** - Form validation

## GitHub Repository Files (Required)
16. **README.md** - Project documentation
17. **.gitignore** - Git ignore rules
18. **LICENSE** - MIT license
19. **github_requirements.txt** - Dependencies (rename to requirements.txt)

## Download Instructions

### Step 1: Download All Files
In Replit, select all these files and download them as a ZIP file.

### Step 2: After Download
1. Extract the ZIP file
2. Rename `github_requirements.txt` to `requirements.txt`
3. Make sure the folder structure looks like:
```
your-project/
├── app.py
├── main.py
├── data_processor.py
├── train_model.py
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── Algerian_forest_fires_dataset_UPDATE_1753524208988.csv
├── models/
│   ├── Ridge_model.pkl
│   └── scaler.pkl
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── predict.html
│   ├── results.html
│   └── dashboard.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        ├── dashboard.js
        └── predictions.js
```

### Step 3: Upload to GitHub
1. Create new repository on GitHub
2. Upload all files maintaining the folder structure
3. Commit with message: "Initial commit: Algerian Forest Fire Prediction System"

## What NOT to Include
- `pyproject.toml` (Replit specific)
- `uv.lock` (Replit specific)  
- `.replit` (Replit specific)
- `__pycache__/` folders
- Any `.pyc` files

Your repository will be complete and ready for others to use!