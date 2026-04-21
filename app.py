
import streamlit as st
import pandas as pd

st.title("🔥 MLB MONSTER SYSTEM")

DFS_URL = "https://docs.google.com/spreadsheets/d/1LQmI3YBA_oOVQUSXiWsN2JbtP2mgf5YNOCEof0MUFrY/edit?gid=0#gid=0"
HR_URL = "https://docs.google.com/spreadsheets/d/1LQmI3YBA_oOVQUSXiWsN2JbtP2mgf5YNOCEof0MUFrY/edit?gid=0#gid=0"
BETS_URL = "https://docs.google.com/spreadsheets/d/1LQmI3YBA_oOVQUSXiWsN2JbtP2mgf5YNOCEof0MUFrY/edit?gid=0#gid=0"
STACKS_URL = "https://docs.google.com/spreadsheets/d/1LQmI3YBA_oOVQUSXiWsN2JbtP2mgf5YNOCEof0MUFrY/edit?gid=0#gid=0"

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
