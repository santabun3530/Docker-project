FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirement file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything from the project into the container
COPY . .

# Set PYTHONPATH to allow module resolution
ENV PYTHONPATH="/app"

# Expose the port Flask runs on
EXPOSE 5000
#without port expose on docker

# Run the app
CMD ["python", "app/main.py"]
