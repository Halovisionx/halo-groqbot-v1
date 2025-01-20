# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /workspace

# Copy the requirements file into the container
COPY requirements.txt .

# Create and activate a virtual environment
RUN python -m venv /workspace/venv

# Install dependencies with a longer timeout
RUN /workspace/venv/bin/pip install --no-cache-dir -r requirements.txt --default-timeout=100

# Install Streamlit
RUN /workspace/venv/bin/pip install streamlit

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["/workspace/venv/bin/streamlit", "run", "streamlit_app.py"]