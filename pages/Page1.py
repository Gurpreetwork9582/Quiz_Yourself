import streamlit as st
import pandas as pd


File = st.file_uploader("Uplaod", type="csv")

if File:
    df = pd.read_csv(File)


    st.write(df)