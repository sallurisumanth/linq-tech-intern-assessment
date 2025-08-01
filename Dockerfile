# Dockerfile

FROM python:3.12

# Sets working directory
WORKDIR /app

# Copies project files into the container
COPY . /app

# Installs dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exposes Streamlit default port
EXPOSE 8501

CMD ["streamlit", "run", "visualization.py", "--server.port=8501", "--server.address=0.0.0.0"]
