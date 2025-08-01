# Purpose
This interactive dashboard reads real-time data from MongoDB and displays trends and recent activity for each data category using Streamlit.

# What It Does
Connects to a MongoDB database (linq_database) and fetches data from the category_data collection.
Filters data from the last 1 hour only.
Allows the user to select a category from a dropdown menu.

# Displays:
The latest 50 data points for the selected category in a table.
A line chart showing the trend of values over the past hour.
Timestamps are human-readable (e.g., “5 minutes ago”).
Automatically refreshes every 5 seconds for live updates.

# Fields in Each Record
category: One of the predefined categories (e.g., Food, Health, Education, etc.)
value: A random numerical value (simulating activity or metric).
timestamp: The exact UTC time when the data point was created.

# How to View the Visualization
Step 1: Run the Streamlit app
In our terminal, navigate to the folder containing visualization.py and run:
`streamlit run visualization.py`
Step 2: Open the Dashboard
By default, it opens at http://localhost:8501

We'll see a live-updating dashboard with a category dropdown, a data table, and a line chart.

# Screenshot of the Dashboard
![Live Dashboard Screenshot](dashboard_with_timestamps.png)
