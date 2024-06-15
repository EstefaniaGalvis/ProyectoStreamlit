import streamlit as st
import pandas as pd
from datetime import datetime

# Cargar los datos
data = pd.read_csv('./static/datasets/integrador.csv')
df = pd.DataFrame(data)

# Título de la aplicación
st.title("Proyecto Integrador")

# Función para el primer filtro por fechas
def filtro1():
    # Obtener fechas mínima y máxima del DataFrame
    fecha_minima = df['FechaEstreno'].min()
    fecha_maxima = df['FechaEstreno'].max()

    # Interfaz para ingresar fechas
    FechaInicial = st.date_input("Ingrese la fecha inicial", value=datetime.strptime(fecha_minima, '%Y-%m-%d').date())
    FechaFinal = st.date_input("Ingrese la fecha Final", value=datetime.strptime(fecha_maxima, '%Y-%m-%d').date())

    # Convertir fechas a formato compatible
    fecha_inicial_str = FechaInicial.strftime('%Y-%m-%d')
    fecha_final_str = FechaFinal.strftime('%Y-%m-%d')

    # Filtrar el DataFrame por las fechas seleccionadas
    opcion_seleccionada = df[(df['FechaEstreno'] >= fecha_inicial_str) & (df['FechaEstreno'] <= fecha_final_str)]

    # Mostrar los resultados en una tabla
    st.table(opcion_seleccionada)

    # Preparar datos para el gráfico
    data = opcion_seleccionada[['Titulo', 'Puntuacion']]
    df_grafico = pd.DataFrame(data)

    # Mostrar gráfico de barras
    st.bar_chart(df_grafico.set_index('Titulo'))

# Función para el segundo filtro por categoría
def filtro2():
    # Obtener las categorías únicas
    CategoriasP = df['Categoria'].unique()

    # Interfaz para seleccionar categoría
    opcion = st.selectbox("Categorias", CategoriasP)

    # Filtrar por la categoría seleccionada
    opcion_seleccionada = df[df['Categoria'] == opcion]

    # Mostrar resultados en tabla
    st.table(opcion_seleccionada)

    # Preparar datos para el gráfico
    data = opcion_seleccionada[['Titulo', 'Puntuacion']]
    df_grafico = pd.DataFrame(data)

    # Mostrar gráfico de barras
    st.bar_chart(df_grafico.set_index('Titulo'))

# Opciones de filtro disponibles
filtros = [
    "Peliculas con mayor puntuación entre las fechas seleccionadas",
    "Peliculas mostradas según la categoría seleccionada"
]

# Selector de filtros
filtro = st.selectbox("Filtros", filtros)

# Aplicar el filtro seleccionado
if filtro:
    filtro_index = filtros.index(filtro)

    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()
