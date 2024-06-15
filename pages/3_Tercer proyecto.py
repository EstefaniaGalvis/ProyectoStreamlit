import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Tercer proyecto")

# Leer el archivo CSV
df = pd.read_csv('static/datasets/Online_retail_sales.csv')

# Renombrar la columna ' monthly_income ' para quitar espacios
df.rename(columns=lambda x: x.strip(), inplace=True)

# Asegurarse de que las columnas existen
expected_columns = ['monthly_income', 'Product', 'quantity', 'state', 'payment_method', 'Price']
missing_columns = [col for col in expected_columns if col not in df.columns]

if missing_columns:
    st.error(f"Las siguientes columnas están ausentes en el dataset: {', '.join(missing_columns)}")
else:
    df['payment_method'] = df['payment_method'].fillna("No comprado").astype(str)
    df['monthly_income'] = df['monthly_income'].replace('[\$,]', '', regex=True).astype(float)  # Convertir los ingresos a float
    df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)  # Convertir los precios a float

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

        estados = sorted(df['state'].unique())

        estado_seleccionado = st.selectbox("Selecciona un estado", estados)

        df_estado = df[df['state'] == estado_seleccionado]

        productos_estado = ["Todos los productos"] + sorted(df_estado['Product'].unique())

        productos_seleccionados = st.multiselect("Selecciona productos para comparar", productos_estado)

        if productos_seleccionados:
            if "Todos los productos" in productos_seleccionados:
                df_filtrado = df_estado
            else:
                df_filtrado = df_estado[df_estado['Product'].isin(productos_seleccionados)]

            productos_por_estado = df_filtrado.groupby('Product').agg({'quantity': 'sum', 'Price': 'sum'}).reset_index()

            fig = go.Figure(data=[
                go.Bar(name='Cantidad de Productos', x=productos_por_estado['Product'], y=productos_por_estado['quantity'])
            ])

            fig.update_layout(
                title=f"Cantidad de Productos Comprados en {estado_seleccionado}",
                xaxis_title="Producto",
                yaxis_title="Cantidad de Productos",
                barmode='group'
            )

            st.plotly_chart(fig, use_container_width=True)

            st.write(f"Detalle de productos comprados en {estado_seleccionado}")
            st.dataframe(productos_por_estado)
        else:
            st.write("Por favor selecciona al menos un producto.")

    def filtro3():
        st.write("Filtro para mostrar la cantidad de productos comprados y los ingresos por rango de ingresos mensuales")

        ingresos_rangos = {
            'Menos de $20,000': (0, 20000),
            '$20,000 - $40,000': (20000, 40000),
            '$40,000 - $60,000': (40000, 60000),
            'Más de $60,000': (60000, df['monthly_income'].max())
        }

        rango_seleccionado = st.selectbox("Selecciona un rango de ingresos", list(ingresos_rangos.keys()))

        if rango_seleccionado:
            min_ingreso, max_ingreso = ingresos_rangos[rango_seleccionado]

            df_filtrado = df[(df['monthly_income'] >= min_ingreso) & (df['monthly_income'] <= max_ingreso)]

            productos_por_ingreso = df_filtrado.groupby('Product').agg({'quantity': 'sum', 'Price': 'sum'}).reset_index()

            total_ingresos = productos_por_ingreso['Price'].sum()

            fig = go.Figure(data=[
                go.Bar(name='Cantidad de Productos', x=productos_por_ingreso['Product'], y=productos_por_ingreso['quantity']),
                go.Bar(name='Ingresos', x=productos_por_ingreso['Product'], y=productos_por_ingreso['Price'])
            ])

            fig.update_layout(
                title=f"Cantidad de Productos Comprados e Ingresos en el Rango de Ingresos {rango_seleccionado}",
                xaxis_title="Producto",
                yaxis_title="Cantidad de Productos / Ingresos",
                barmode='group'
            )

            st.plotly_chart(fig, use_container_width=True)

            st.write(f"Detalle de productos comprados e ingresos en el rango de ingresos {rango_seleccionado}")
            st.dataframe(productos_por_ingreso)

            st.metric(label=f"Total de Ingresos en el rango {rango_seleccionado}", value=total_ingresos)

        else:
            st.write("Por favor selecciona un rango de ingresos.")

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
        elif filtro_index == 2:
            filtro3()
