# Use the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Copy the application code to the container
COPY ./ .env


# Expose the port that the FastAPI application listens on
EXPOSE 8000
EXPOSE 9009

# Define the startup command
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000", "--port", "9009"]

