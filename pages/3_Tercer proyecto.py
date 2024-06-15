import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Tercer proyecto")

# Leer el archivo CSV
df = pd.read_csv('static/datasets/Online_retail_sales.csv') 
df['payment_method'] = df['payment_method'].fillna("No comprado").astype(str)

st.write("Dataset usado: Online retail sales")

# -----------------------------------------------------------------------------------
ProductosO = sorted(df['Product'].unique())

def filtro1():
    st.write("Filtro para saber los métodos de pago usados en diferentes productos")

    listaProductos = st.selectbox("Productos", ProductosO)
    
    dfFiltrado = df[df['Product'] == listaProductos]

    metodoPagoCount = dfFiltrado['payment_method'].value_counts().reset_index()
    metodoPagoCount.columns = ['payment_method', 'count']
    
    # Gráfico de barras
    fig = go.Figure(data=[
        go.Bar(name='Métodos de Pago', x=metodoPagoCount['payment_method'], y=metodoPagoCount['count'])
    ])

    fig.update_layout(
        title=f"Métodos de Pago Usados para {listaProductos}",
        xaxis_title="Método de Pago",
        yaxis_title="Cantidad de Usos",
        barmode='group'
    )

    totalComprado = dfFiltrado['quantity'].sum()
    st.metric(label=f"Total comprado de {listaProductos}", value=totalComprado)

    st.plotly_chart(fig, use_container_width=True)

def filtro2():
    st.write("Filtro para mostrar la cantidad de productos comprados por estado")

    # Agrupar los datos por estado y sumar la cantidad de productos comprados
    productos_por_estado = df.groupby('state')['quantity'].sum().reset_index()

    # Gráfico de barras
    fig = go.Figure(data=[
        go.Bar(name='Cantidad de Productos', x=productos_por_estado['state'], y=productos_por_estado['quantity'])
    ])

    fig.update_layout(
        title="Cantidad de Productos Comprados por Estado",
        xaxis_title="Estado",
        yaxis_title="Cantidad de Productos",
        barmode='group'
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------------------------------
filtros = [
    "Primer filtro",
    "Segundo filtro",
    "Tercer filtro"
]

filtro = st.selectbox("Filtros", filtros)

if filtro:
    filtro_index = filtros.index(filtro)
    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()
