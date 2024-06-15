import streamlit as st
import pandas as pd
from datetime import datetime

data = pd.read_csv('./static/datasets/integrador.csv')
df = pd.DataFrame(data)

st.title("Proyecto Integrador")

def filtro1():
    fecha_minima = df['FechaEstreno'].min()
    fecha_maxima = df['FechaEstreno'].max()

    FechaInicial = st.date_input("Ingrese la fecha inicial", value=datetime.strptime(fecha_minima, '%Y-%m-%d').date())
    FechaFinal = st.date_input("Ingrese la fecha Final", value=datetime.strptime(fecha_maxima, '%Y-%m-%d').date())

    fecha_inicial_str = FechaInicial.strftime('%Y-%m-%d')
    fecha_final_str = FechaFinal.strftime('%Y-%m-%d')

    opcion_seleccionada = df[(df['FechaEstreno'] >= fecha_inicial_str) & (df['FechaEstreno'] <= fecha_final_str)]

    st.table(opcion_seleccionada)

    data = opcion_seleccionada[['Titulo', 'Puntuacion']]
    df_grafico = pd.DataFrame(data)

    st.bar_chart(df_grafico.set_index('Titulo'))

def filtro2():
    CategoriasP = df['Categoria'].unique()

    opcion = st.selectbox("Categorias", CategoriasP)

    opcion_seleccionada = df[df['Categoria'] == opcion]

    st.table(opcion_seleccionada)

    data = opcion_seleccionada[['Titulo', 'Puntuacion']]
    df_grafico = pd.DataFrame(data)

    st.bar_chart(df_grafico.set_index('Titulo'))

filtros = [
    "Peliculas con mayor puntuación entre las fechas seleccionadas",
    "Peliculas mostradas según la categoría seleccionada"
]

filtro = st.selectbox("Filtros", filtros)

if filtro:
    filtro_index = filtros.index(filtro)

    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()
