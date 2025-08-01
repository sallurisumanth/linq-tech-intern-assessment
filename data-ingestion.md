# Data Ingestion - Category-Based Analytics
# Purpose
This script adds mock data to the MongoDB database to simulate different categories of data for analysis and visualization.

# What It Does
Connects to a local MongoDB database called linq_database.
Targets the collection named category_data.
Defines 6 categories: Food, Health, Education, Travel, Entertainment, and Shopping.
Creates **6 new records** (1 per category) with:
    - A random value between `200` and `1000`
    - The current UTC timestamp
    - Inserts all new records into the MongoDB collection.

# Fields in Each Record
category: The category name (one of the 6 listed above).
value: A random number between 200 and 1000 representing the data point.
timestamp: The exact time when the record was created.

## MongoDB Collection Info
Database: `linq_database`
Collection: `category_data`


## Requirements
Make sure we have:
- Python installed
- MongoDB running locally or remotely
- `pymongo` installed  
