# CONTRIBUTING

## How to run the Dockerfile locally

### if there is new requriement, stop the prev container and rebuild : docker build -t flask-smorest-api .

### if already built , run : docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run --host 0.0.0.0"
