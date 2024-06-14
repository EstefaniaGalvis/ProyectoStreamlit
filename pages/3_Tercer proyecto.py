import streamlit as st
import pandas as pd

st.title("Tercer proyecto")

df = pd.read_csv('static/datasets/Online_retail_sales.csv') 

st.write("Dataset usado: Online retail sales")
# -----------------------------------------------------------------------------------






# -----------------------------------------------------------------------------------
filtros=[
    "Primer filtro",
    "Segundo filtro",
    "Tercer filtro"
]

filtro = st.selectbox("Filtros",filtros)

if filtro:
    filtro_index = filtros.index(filtro)

    