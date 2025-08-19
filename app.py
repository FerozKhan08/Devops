from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Home route
@app.route('/')
def home():
    return "Welcome to your first Flask App!"

# About route
@app.route('/about')
def about():
    return "This is the About Page."

# Health check endpoint
@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
