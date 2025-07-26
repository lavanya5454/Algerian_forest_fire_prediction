// Dashboard JavaScript for chart rendering and interactions

document.addEventListener('DOMContentLoaded', function() {
    // Check if dashboard data is available
    if (typeof dashboardData === 'undefined' || !dashboardData.stats) {
        console.warn('Dashboard data not available');
        return;
    }

    // Initialize all charts
    initializeMonthlyFireChart();
    initializeRiskDistributionChart();
    initializeTempFwiChart();
    initializeWeatherConditionsChart();
});

function initializeMonthlyFireChart() {
    const ctx = document.getElementById('monthlyFireChart');
    if (!ctx || !dashboardData.monthly_fires) return;

    const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    
    const data = [];
    const labels = [];
    
    for (let month = 6; month <= 9; month++) { // Data appears to be from June to September
        labels.push(monthNames[month - 1]);
        data.push(dashboardData.monthly_fires[month] || 0);
    }

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Fire Incidents',
                data: data,
                backgroundColor: 'rgba(255, 107, 53, 0.8)',
                borderColor: 'rgba(255, 107, 53, 1)',
                borderWidth: 2,
                borderRadius: 5
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            }
        }
    });
}

function initializeRiskDistributionChart() {
    const ctx = document.getElementById('riskDistributionChart');
    if (!ctx || !dashboardData.risk_distribution) return;

    const riskData = dashboardData.risk_distribution;
    const labels = Object.keys(riskData);
    const data = Object.values(riskData);
    
    const colors = {
        'Very Low': '#28a745',
        'Low': '#17a2b8',
        'Moderate': '#ffc107',
        'High': '#dc3545',
        'Very High': '#6f42c1'
    };

    const backgroundColors = labels.map(label => colors[label] || '#6c757d');

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: backgroundColors,
                borderWidth: 2,
                borderColor: '#fff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

function initializeTempFwiChart() {
    const ctx = document.getElementById('tempFwiChart');
    if (!ctx || !dashboardData.temp_fwi_correlation) return;

    const correlationData = dashboardData.temp_fwi_correlation.slice(0, 50); // Limit points for clarity

    new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Temperature vs FWI',
                data: correlationData.map(item => ({
                    x: item.Temperature,
                    y: item.FWI
                })),
                backgroundColor: 'rgba(255, 107, 53, 0.6)',
                borderColor: 'rgba(255, 107, 53, 1)',
                borderWidth: 1,
                pointRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Temperature (°C)'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Fire Weather Index'
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

function initializeWeatherConditionsChart() {
    const ctx = document.getElementById('weatherConditionsChart');
    if (!ctx || !dashboardData.weather_conditions) return;

    const weatherData = dashboardData.weather_conditions;
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['High Temp\n(>35°C)', 'Low Humidity\n(<30%)', 'High Wind\n(>20 km/h)', 'Rainy Days'],
            datasets: [{
                label: 'Days',
                data: [
                    weatherData.high_temp || 0,
                    weatherData.low_humidity || 0,
                    weatherData.high_wind || 0,
                    weatherData.rainy_days || 0
                ],
                backgroundColor: [
                    'rgba(255, 107, 53, 0.8)',  // High temp - orange
                    'rgba(135, 206, 235, 0.8)', // Low humidity - blue
                    'rgba(144, 238, 144, 0.8)', // High wind - green
                    'rgba(100, 149, 237, 0.8)'  // Rainy days - blue
                ],
                borderWidth: 2,
                borderRadius: 3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                },
                x: {
                    ticks: {
                        maxRotation: 0,
                        font: {
                            size: 10
                        }
                    }
                }
            }
        }
    });
}

// Add some interactivity for better user experience
function addChartInteractivity() {
    // Add smooth animations when charts come into view
    const observerOptions = {
        threshold: 0.3,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, observerOptions);

    // Observe all chart cards
    document.querySelectorAll('.chart-card').forEach(card => {
        observer.observe(card);
    });
}

// Initialize interactivity
addChartInteractivity();
