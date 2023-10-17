# Use the official Python image as the base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install FastAPI and other dependencies
RUN pip install -r requirements.txt

COPY . /app/

# Expose the port your application will run on
EXPOSE 8000


