import streamlit as st
import pandas as pd
from df import df

st.title("Proyecto Integrador")
#------------------------------------------------------------------------------

def filtro1():
    FechaInicial = st.date_input("Ingrese la fecha inicial",value=None)

    FechaFinal = st.date_input("Ingrese la fecha Final",value=None)

#------------------------------------------------------------------------------

def filtro2():
    CategoriasP = df['Categoria'].unique()
    opcion = st.selectbox("Categorias", CategoriasP)
    opcion_seleccionada = df[df['Categoria']==opcion]
    st.table(opcion_seleccionada)

    data = opcion_seleccionada[['Titulo','Puntuacion']]
    df_grafico = pd.DataFrame(data)
    st.bar_chart(df_grafico.set_index('Titulo'))


filtros =[
    "Peliculas con mayor puntuación entre las fechas seleccionadas",
    "Peliculas con mayor puntuación segun la categoría seleccionada",
    ""
]

filtro = st.selectbox("Filtros",filtros)

if filtro:
    filtro_index = filtros.index(filtro)

    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()