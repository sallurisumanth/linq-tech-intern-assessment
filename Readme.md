# Linq Technology Intern Take-Home Project
Welcome to my submission for the Linq Technology Intern Take-Home Assessment! This project demonstrates how we can collect, process, and visualize live data using Python, MongoDB, and Streamlit.

# What This Project Does
-Simulates real-time data for 6 different categories like Food, Health, Travel, etc.
-Stores the data in a MongoDB database using an automated ingestion script.
-Displays a live dashboard that auto-refreshes every 5 seconds to show the latest stats.
-Visualizes trends of selected categories from the last 1 hour.

# Technologies Used
Python 
MongoDB (via Docker) 
Streamlit (for dashboard) 
Docker & Docker Compose 

# Project Structure
File	                                             Description
data_ingest.py ->           Script that generates and inserts mock data into MongoDB.
visualization.py ->      	Streamlit app that shows live visual analytics.
docker-compose.yml ->        Sets up MongoDB and runs both scripts in containers.
datastore-setup.md ->        Explains how MongoDB is set up using Docker.
data-ingestion.md	->       Explains how data is created and stored.
visualization.md ->          Describes how the dashboard works and what it shows.
dashboard.png ->            Screenshot of the live dashboard UI.

# How to Run It
Make sure Docker is installed, then run:
`docker-compose up`
Our dashboard will be available at:
http://localhost:8501

# Submission Info
GitHub Repo shared with:
patrick@linqapp.com
careers@linqapp.com

# Subject: Technology Intern Take-Home Submission