# Use official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /streamlit_app

# Copy project files
COPY . /streamlit_app

# Install dependencies
RUN pip install --no-cache-dir streamlit assemblyai audio-recorder-streamlit  

# Expose Streamlit's default port
EXPOSE 8501

# Set Streamlit configuration (to allow it to run inside Docker)
ENV STREAMLIT_SERVER_PORT 8501
ENV STREAMLIT_SERVER_ADDRESS 0.0.0.0
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS false

# Command to run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
