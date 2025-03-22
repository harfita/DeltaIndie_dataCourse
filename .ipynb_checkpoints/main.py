import streamlit as st
import pandas as pd

df= pd.read_csv("data_penjualan-checkpoint.csv")

st.title("Perkenalan")
st.write("Perkenalkan nama saya Laily")
st.text_input("Masukan Nama")
st.number_input("Masuk Umur")



