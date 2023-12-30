# Use the official Python 3.8 image as the base image
FROM python:3.8-slim-buster

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file from your local machine into the container's /app directory
COPY requirements.txt requirements.txt

# Install the Python dependencies listed in requirements.txt using pip
RUN pip3 install -r requirements.txt

# Copy all files from your local machine into the container's /app directory
COPY . .

# Set the default command to run when the container starts
CMD python3 main.py
