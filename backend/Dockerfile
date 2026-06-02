# Lightweight Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure real-time stdout/stderr output
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy requirements first for Docker layer caching
COPY requirements.txt /app/

# Update pip and install project dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# 8. Exponemos el puerto 5000 (que es donde corre tu Flask)
EXPOSE 5000

# Start the application
CMD ["python", "run.py"]