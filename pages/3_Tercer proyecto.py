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

        # Obtener la lista de estados únicos
        estados = sorted(df['state'].unique())

        # Seleccionar estado
        estado_seleccionado = st.selectbox("Selecciona un estado", estados)

        # Filtrar datos por estado seleccionado
        df_estado = df[df['state'] == estado_seleccionado]

        # Obtener lista de productos únicos en el estado seleccionado y añadir "Todos los productos"
        productos_estado = ["Todos los productos"] + sorted(df_estado['Product'].unique())

        # Seleccionar productos (con selección múltiple)
        productos_seleccionados = st.multiselect("Selecciona productos para comparar", productos_estado)

        if productos_seleccionados:
            if "Todos los productos" in productos_seleccionados:
                # Si se selecciona "Todos los productos", mostrar todos los productos
                df_filtrado = df_estado
            else:
                # Filtrar datos por productos seleccionados
                df_filtrado = df_estado[df_estado['Product'].isin(productos_seleccionados)]

            # Agrupar los datos por producto y sumar la cantidad de productos comprados
            productos_por_estado = df_filtrado.groupby('Product').agg({'quantity': 'sum', 'Price': 'sum'}).reset_index()

            # Gráfico de barras para los productos seleccionados
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

            # Mostrar detalle de productos comprados en el estado seleccionado
            st.write(f"Detalle de productos comprados en {estado_seleccionado}")
            st.dataframe(productos_por_estado)
        else:
            st.write("Por favor selecciona al menos un producto.")

    def filtro3():
        st.write("Filtro para mostrar la cantidad de productos comprados y los ingresos por cada producto")

        # Obtener la lista de productos únicos
        productos = sorted(df['Product'].unique())

        # Seleccionar producto
        producto_seleccionado = st.selectbox("Selecciona un producto", productos)

        if producto_seleccionado:
            # Filtrar datos por producto seleccionado
            df_producto = df[df['Product'] == producto_seleccionado]

            # Agrupar los datos por producto y sumar la cantidad de productos comprados y los ingresos
            productos_comprados = df_producto['quantity'].sum()
            ingresos_totales = df_producto['Price'].sum()

            # Mostrar gráfico de barras y detalle de cantidad de productos comprados e ingresos
            fig = go.Figure(data=[
                go.Bar(name='Cantidad de Productos', x=[producto_seleccionado], y=[productos_comprados]),
                go.Bar(name='Ingresos Totales', x=[producto_seleccionado], y=[ingresos_totales])
            ])

            fig.update_layout(
                title=f"Cantidad de Productos Comprados e Ingresos para {producto_seleccionado}",
                xaxis_title="Producto",
                yaxis_title="Cantidad de Productos / Ingresos",
                barmode='group'
            )

            st.plotly_chart(fig, use_container_width=True)

            # Mostrar detalle de cantidad de productos comprados e ingresos
            st.write(f"Detalle de cantidad de productos comprados e ingresos para {producto_seleccionado}")
            detalle_df = pd.DataFrame({
                'Producto': [producto_seleccionado],
                'Cantidad de Productos Comprados': [productos_comprados],
                'Ingresos Totales': [ingresos_totales]
            })
            st.dataframe(detalle_df)

        else:
            st.write("Por favor selecciona un producto.")

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
