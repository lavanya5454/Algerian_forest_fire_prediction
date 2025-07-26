// Predictions form JavaScript for validation and user experience

document.addEventListener('DOMContentLoaded', function() {
    initializeFormValidation();
    addFormInteractivity();
    addTooltips();
});

function initializeFormValidation() {
    const form = document.querySelector('form.needs-validation');
    if (!form) return;

    // Add custom validation
    form.addEventListener('submit', function(event) {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        
        form.classList.add('was-validated');
    });

    // Add real-time validation for specific fields
    addRealTimeValidation();
}

function addRealTimeValidation() {
    // Temperature validation (typical range 20-45°C)
    const tempInput = document.getElementById('Temperature');
    if (tempInput) {
        tempInput.addEventListener('input', function() {
            const value = parseFloat(this.value);
            if (value < 15 || value > 50) {
                this.setCustomValidity('Temperature should typically be between 15-50°C');
            } else {
                this.setCustomValidity('');
            }
        });
    }

    // Humidity validation (0-100%)
    const rhInput = document.getElementById('RH');
    if (rhInput) {
        rhInput.addEventListener('input', function() {
            const value = parseFloat(this.value);
            if (value < 0 || value > 100) {
                this.setCustomValidity('Humidity must be between 0-100%');
            } else {
                this.setCustomValidity('');
            }
        });
    }

    // Wind speed validation (reasonable range)
    const wsInput = document.getElementById('Ws');
    if (wsInput) {
        wsInput.addEventListener('input', function() {
            const value = parseFloat(this.value);
            if (value < 0 || value > 100) {
                this.setCustomValidity('Wind speed should be between 0-100 km/h');
            } else {
                this.setCustomValidity('');
            }
        });
    }

    // FFMC validation (0-101 range)
    const ffmcInput = document.getElementById('FFMC');
    if (ffmcInput) {
        ffmcInput.addEventListener('input', function() {
            const value = parseFloat(this.value);
            if (value < 0 || value > 101) {
                this.setCustomValidity('FFMC should be between 0-101');
            } else {
                this.setCustomValidity('');
            }
        });
    }
}

function addFormInteractivity() {
    // Add loading state to submit button
    const form = document.querySelector('form');
    const submitBtn = document.querySelector('button[type="submit"]');
    
    if (form && submitBtn) {
        form.addEventListener('submit', function() {
            if (form.checkValidity()) {
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Calculating...';
                submitBtn.disabled = true;
            }
        });
    }

    // Add smooth focus effects
    const inputs = document.querySelectorAll('input, select');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
    });

    // Add input suggestions based on typical values
    addInputSuggestions();
}

function addInputSuggestions() {
    const suggestions = {
        'Temperature': { min: 20, max: 40, typical: 32 },
        'RH': { min: 20, max: 90, typical: 65 },
        'Ws': { min: 5, max: 25, typical: 15 },
        'Rain': { min: 0, max: 20, typical: 0 },
        'FFMC': { min: 30, max: 95, typical: 85 },
        'DMC': { min: 0, max: 50, typical: 15 },
        'DC': { min: 0, max: 200, typical: 50 },
        'ISI': { min: 0, max: 20, typical: 8 },
        'BUI': { min: 0, max: 70, typical: 20 }
    };

    Object.keys(suggestions).forEach(fieldName => {
        const input = document.getElementById(fieldName);
        if (input) {
            const suggestion = suggestions[fieldName];
            const helpText = input.parentElement.querySelector('.form-text');
            if (helpText) {
                helpText.innerHTML += ` <small class="text-muted">(Typical: ${suggestion.typical})</small>`;
            }
        }
    });
}

function addTooltips() {
    // Add informative tooltips for fire weather components
    const tooltips = {
        'FFMC': 'Fine Fuel Moisture Code: Represents moisture content of litter and fine fuels. Higher values indicate drier conditions.',
        'DMC': 'Duff Moisture Code: Represents moisture content of loosely compacted organic layers. Indicates medium-term drought effects.',
        'DC': 'Drought Code: Represents moisture content of deep organic layers. Indicates long-term drought effects.',
        'ISI': 'Initial Spread Index: Combines wind speed and FFMC to indicate expected rate of fire spread.',
        'BUI': 'Buildup Index: Combines DMC and DC to indicate total amount of fuel available for combustion.'
    };

    Object.keys(tooltips).forEach(fieldName => {
        const label = document.querySelector(`label[for="${fieldName}"]`);
        if (label) {
            label.setAttribute('title', tooltips[fieldName]);
            label.style.cursor = 'help';
            
            // Add a small info icon
            const infoIcon = document.createElement('i');
            infoIcon.className = 'fas fa-info-circle text-muted ms-1';
            infoIcon.style.fontSize = '0.8rem';
            infoIcon.setAttribute('title', tooltips[fieldName]);
            label.appendChild(infoIcon);
        }
    });
}

// Form data persistence (optional - saves form data in localStorage)
function enableFormPersistence() {
    const form = document.querySelector('form');
    if (!form) return;

    // Load saved data on page load
    loadFormData();

    // Save form data on input change
    form.addEventListener('input', function(e) {
        if (e.target.type !== 'submit') {
            localStorage.setItem(`fire_prediction_${e.target.name}`, e.target.value);
        }
    });

    // Clear saved data on successful submission
    form.addEventListener('submit', function() {
        if (form.checkValidity()) {
            clearFormData();
        }
    });
}

function loadFormData() {
    const inputs = document.querySelectorAll('input, select');
    inputs.forEach(input => {
        const savedValue = localStorage.getItem(`fire_prediction_${input.name}`);
        if (savedValue && input.type !== 'submit') {
            input.value = savedValue;
        }
    });
}

function clearFormData() {
    const inputs = document.querySelectorAll('input, select');
    inputs.forEach(input => {
        localStorage.removeItem(`fire_prediction_${input.name}`);
    });
}

// Add sample data button for testing
function addSampleDataButton() {
    const form = document.querySelector('form');
    if (!form) return;

    const sampleBtn = document.createElement('button');
    sampleBtn.type = 'button';
    sampleBtn.className = 'btn btn-outline-secondary btn-sm mb-3';
    sampleBtn.innerHTML = '<i class="fas fa-magic"></i> Fill Sample Data';
    
    sampleBtn.addEventListener('click', fillSampleData);
    
    const firstSection = document.querySelector('.form-section');
    if (firstSection) {
        firstSection.insertBefore(sampleBtn, firstSection.firstChild.nextSibling);
    }
}

function fillSampleData() {
    const sampleData = {
        'Temperature': 35,
        'RH': 60,
        'Ws': 15,
        'Rain': 0.1,
        'FFMC': 85.5,
        'DMC': 15.2,
        'DC': 45.8,
        'ISI': 8.5,
        'BUI': 18.7,
        'Region': 'bejaia',
        'Classes': 'moderate'
    };

    Object.keys(sampleData).forEach(fieldName => {
        const input = document.getElementById(fieldName);
        if (input) {
            input.value = sampleData[fieldName];
            input.dispatchEvent(new Event('input', { bubbles: true }));
        }
    });
}

// Initialize optional features
enableFormPersistence();
addSampleDataButton();
