# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Upgrade pip
RUN pip3 install --no-cache-dir --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application's files into the container at /app
COPY . .

# Run the bot when the container launches
CMD ["python3", "main.py"]
