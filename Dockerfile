# Dockerfile

FROM python:3.12

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Let docker-compose override the command
CMD ["streamlit", "run", "visualization.py", "--server.port=8501", "--server.address=0.0.0.0"]
