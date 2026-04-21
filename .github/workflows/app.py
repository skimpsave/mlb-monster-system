import streamlit as st
import pandas as pd
import sqlite3

st.title("🔥 MLB MONSTER DASHBOARD")

conn = sqlite3.connect("mlb_data.db")
df = pd.read_sql("SELECT * FROM results", conn)

st.subheader("DFS RANKINGS")
st.dataframe(df.sort_values("DFS_PROJ", ascending=False).head(20))

st.subheader("HR PICKS")
st.dataframe(df.sort_values("HR_PROB", ascending=False).head(15))

st.subheader("BETTING EDGES")
st.dataframe(df.sort_values("EV_EDGE", ascending=False).head(10))
