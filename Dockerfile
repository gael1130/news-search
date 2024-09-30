# Step 1: Use an official Python runtime as a base image
FROM python:3.11-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y git

# Step 4: Copy requirements.txt to the container
COPY requirements.txt /app/requirements.txt

# Step 5: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the rest of the application code to the container
COPY . /app

# Step 7: Create the `results` directory
RUN mkdir -p /app/results

# Step 7: Define the command to run the application
CMD ["python", "main.py"]
