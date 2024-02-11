# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application into the container
COPY . /app/

# Expose the port that FastAPI runs on
EXPOSE 8005:8005

# Command to run the FastAPI application
CMD ["sh", "./start_app.sh"]