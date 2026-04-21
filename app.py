
import streamlit as st
import pandas as pd

st.title("🔥 MLB MONSTER SYSTEM")

DFS_URL = "YOUR_DFS_CSV_LINK"
HR_URL = "YOUR_HR_CSV_LINK"
BETS_URL = "YOUR_BETS_CSV_LINK"
STACKS_URL = "YOUR_STACKS_CSV_LINK"

def load(url):
    return pd.read_csv(url)

dfs = load(DFS_URL)
hr = load(HR_URL)
bets = load(BETS_URL)
stacks = load(STACKS_URL)

st.subheader("DFS")
st.dataframe(dfs)

st.subheader("HR PICKS")
st.dataframe(hr)

st.subheader("BETTING")
st.dataframe(bets)

st.subheader("STACKS")
st.dataframe(stacks)
