import pandas as pd
import streamlit as st

st.Title("Welcome to Streamlit")
st.write("Here is our first data frame")

st.write(pd.DataFrame{"Nama":["Arief","Maulana"],"Pacar":["Quynh", "Hoa"]}