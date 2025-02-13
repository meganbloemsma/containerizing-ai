# Use a lightweight Python image as the base
FROM python:3.9-slim

# Install required dependencies for Azure Speech SDK to work with audio
RUN apt-get update && \
    apt-get install -y \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the application file (sending.py) into the container
COPY sending.py .

# Install the required Python dependencies
RUN pip install azure-cognitiveservices-speech
RUN pip install python-dotenv

# Set environment variables (these can also be passed through docker-compose)
ENV SPEECH_KEY=""
ENV SPEECH_REGION=""

# Command to run the Python script when the container starts
CMD ["python", "sending.py"]
