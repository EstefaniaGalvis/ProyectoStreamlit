import streamlit as st
import pandas as pd
from df import df

#------------------------------------------------------------------------------

st.header("Peliculas con mayor nota entre las fechas seleccionadas")

FechaInicial = st.date_input("Ingrese la fecha inicial",value=None)

FechaFinal = st.date_input("Ingrese la fecha Final",value=None)

#------------------------------------------------------------------------------

st.header("Peliculas con mayor puntuación segun la categoría seleccionada")

def categorias_peliculas():
    CategoriasP = df['Categoria'].unique()
    opcion = st.selectbox("Categorias", CategoriasP)
    opcion_seleccionada = df[df['Categoria']==opcion]
    st.table(opcion_seleccionada)

    data = opcion_seleccionada[['Titulo','Puntuacion']]
    df_grafico = pd.DataFrame(data)
    st.bar_chart(df_grafico.set_index('Titulo'))

categorias_peliculas()