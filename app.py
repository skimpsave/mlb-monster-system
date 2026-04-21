import streamlit as st
import pandas as pd
import sqlite3
import os

st.title("🔥 MLB MONSTER DASHBOARD")

# -----------------------
# CREATE DB IF NOT EXISTS
# -----------------------
if not os.path.exists("mlb_data.db"):
    st.warning("Database not found. Running model...")

    import model_hr
    import model_dfs
    import betting_model

# -----------------------
# CONNECT DB
# -----------------------
conn = sqlite3.connect("mlb_data.db")

# -----------------------
# LOAD DATA SAFELY
# -----------------------
try:
    df = pd.read_sql("SELECT * FROM results", conn)
except:
    st.error("No data found yet. Model may not have run.")
    st.stop()

# -----------------------
# DISPLAY
# -----------------------
st.subheader("DFS RANKINGS")
st.dataframe(df.sort_values("DFS_PROJ", ascending=False).head(20))

st.subheader("HR PICKS")
st.dataframe(df.sort_values("HR_PROB", ascending=False).head(15))

st.subheader("BETTING EDGES")
st.dataframe(df.sort_values("EV_EDGE", ascending=False).head(10))
