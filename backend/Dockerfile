# ==============================
# KitchenOS Backend Dockerfile
# ==============================

# Base Image
FROM python:3.13-slim

# Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working Directory
WORKDIR /app

# Install System Dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy Requirements
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install Python Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Files
COPY . .

# Expose FastAPI Port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]