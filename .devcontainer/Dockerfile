# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /workspace

# Copy requirements.txt first
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Streamlit
RUN pip install streamlit

# Copy the rest of the application code into the container at /workspace
COPY . .

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run streamlit_app.py when the container launches
CMD ["/workspace/venv/bin/streamlit", "run", "streamlit_app.py"]