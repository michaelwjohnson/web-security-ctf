# Web Security CTF

A web security Capture The Flag (CTF) challenge implemented using Flask and Docker. This project is designed to help users learn and practice web security concepts in a controlled environment.

## Project Structure

- `flaskApp.py`: Main Flask application
- `Dockerfile`: Container configuration for the web application
- `docker-compose.yml`: Docker Compose configuration for easy deployment
- `requirements.txt`: Python dependencies
- `templates/`: HTML templates for the web interface
  - dashboard.html
  - index.html
  - login.html

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/michaelwjohnson/web-security-ctf.git
   cd web-security-ctf
   ```

2. Build and run with Docker Compose:

   ```bash
   docker-compose up --build
   ```

## Alternative Deployment Method

Alternatively, you can pull the pre-built Docker image from Docker Hub and run it directly.

1. Pull the Docker image from Docker Hub:

   ```bash
   docker pull michaelwjohnson/web-security-ctf
   ```

2. Run the Docker image:

   ```bash
   docker run -p 8080:8080 michaelwjohnson/web-security-ctf
   ```

This will start the CTF container and make it available on port <http://localhost:8080>

## Development

To run the application locally for development:

1. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python flaskApp.py
   ```

## Note

This is a CTF challenge environment. Please ensure you run it in a controlled environment and do not expose it to the public internet.
