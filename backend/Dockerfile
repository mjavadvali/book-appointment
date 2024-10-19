FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements first to leverage Docker's layer caching
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose port 8000 for the Django app
EXPOSE 8000
