import os
import pandas as pd
import streamlit as st
from pymongo import MongoClient
from datetime import datetime, timedelta
import humanize
from streamlit_autorefresh import st_autorefresh

# Auto-refresh every 5 seconds
st_autorefresh(interval=5000, key="data_refresh")
st.set_page_config(page_title="Live Dashboard", layout="wide")
st.title("📊 Live Data Dashboard")

# MongoDB setup
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
df = pd.DataFrame(list(client["linq_database"]["category_data"].find()))

if df.empty or 'timestamp' not in df.columns:
    st.warning("No valid data available.")
    st.stop()

df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df[df['timestamp'] >= datetime.utcnow() - timedelta(hours=1)]

if df.empty:
    st.info("No data from the last hour.")
    st.stop()

df['relative_time'] = df['timestamp'].apply(lambda x: humanize.naturaltime(datetime.utcnow() - x))
category = st.selectbox("Select Category", df['category'].unique())
filtered = df[df['category'] == category].sort_values('timestamp', ascending=False).head(50)

if filtered.empty:
    st.info(f"No data for '{category}' in the last hour.")
    st.stop()

st.subheader("Latest Data (Last Hour)")
st.dataframe(filtered[['category', 'value', 'relative_time']].reset_index(drop=True))

st.subheader(f"📈 Trend for {category}")
trend = filtered[['timestamp', 'value']].sort_values('timestamp').set_index('timestamp')
st.line_chart(trend)
