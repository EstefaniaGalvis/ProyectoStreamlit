import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
# Set the page title and header
st.title("Simulador CESDE Bello")

df = pd.read_csv('static/datasets/cesde.csv')

gruposU = sorted(df['GRUPO'].unique())
nivelesU = sorted(df['NIVEL'].unique())
jornadasU =  sorted(df['JORNADA'].unique())
horarioU =  sorted(df['HORARIO'].unique())
submodulosU =  sorted(df['SUBMODULO'].unique())
docentesU =  sorted(df['DOCENTE'].unique())
momentosU =  sorted(df['MOMENTO'].unique())

# -----------------------------------------------------------------------------------
def filtro1():    
    col1, col2 = st.columns(2)
    with col1:
        grupo = st.selectbox("Grupo",gruposU)
    with col2:
        momento = st.selectbox("Momento",momentosU)
    resultado = df[(df['GRUPO']==grupo)&(df['MOMENTO']==momento)]
   
    resultado= resultado.reset_index(drop=True) 
    # Grafico de barras
    estudiante=resultado['NOMBRE']
    fig = go.Figure(data=[
        go.Bar(name='CONOCIMIENTO', x=estudiante, y=resultado['CONOCIMIENTO']),
        go.Bar(name='DESEMPEÑO', x=estudiante, y=resultado['DESEMPEÑO']),
        go.Bar(name='PRODUCTO', x=estudiante, y=resultado['PRODUCTO'])
    ])   
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    # Tabla
    st.table(resultado[["NOMBRE","CONOCIMIENTO","DESEMPEÑO","PRODUCTO"]])
    
# -----------------------------------------------------------------------------------
def filtro2():
    col1, col2, col3 = st.columns(3)
    with col1:
        grupo = st.selectbox("Grupo",gruposU)
    with col2:
        nombres = df[df['GRUPO']==grupo]
        nombre = st.selectbox("Estudiante",nombres["NOMBRE"])
    with col3:
        momentosU.append("Todos")
        momento = st.selectbox("Momento",momentosU)   

    if momento == "Todos":
        resultado = df[(df['GRUPO']==grupo)&(df['NOMBRE']==nombre)]
        # Grafico de barras
        momentos=sorted(df['MOMENTO'].unique())
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=momentos, y=resultado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=momentos, y=resultado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=momentos, y=resultado['PRODUCTO'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado= resultado.reset_index(drop=True) 
        m1 = resultado.loc[0,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        m2 = resultado.loc[1,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        m3 = resultado.loc[2,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        tm = pd.Series([m1.mean(),m2.mean(),m3.mean()])       
        st.subheader("Promedio")
        st.subheader(round(tm.mean(),1)) 
    else :   
        resultado = df[(df['GRUPO']==grupo)&(df['MOMENTO']==momento)&(df['NOMBRE']==nombre)]
        # Grafico de barras
        estudiante=resultado['NOMBRE']
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=estudiante, y=resultado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=estudiante, y=resultado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=estudiante, y=resultado['PRODUCTO'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado= resultado.reset_index(drop=True) 
        conocimiento = resultado.loc[0,['CONOCIMIENTO','DESEMPEÑO','PRODUCTO']]
        st.subheader("Promedio")
        st.subheader(round(conocimiento.mean(),1)) 
  
# -----------------------------------------------------------------------------------

def filtro3(): 
    submodulo = st.selectbox('Selecciona el submódulo', submodulosU)
    momentos = st.selectbox('Selecciona el momento', momentosU)
    
    colM, colN, colMT, colT = st.columns(4)
    with colM:
        mañana = st.checkbox('Mañana')
    with colN:
        noche = st.checkbox('Noche')
    with colMT:
        mañanaTarde = st.checkbox('Mañana-Tarde')
    with colT:
        tarde = st.checkbox('Tarde')
    
    seleccionadas = sum([mañana, noche, mañanaTarde, tarde]) 

    if seleccionadas > 1:
        st.error('Por favor solo selecciona una jornada.')

    elif mañana:
        df_filtrado = df[(df['ESTADO'] == 'FORMACIÓN') & (df['JORNADA'] == 'MAÑANA') & (df['SUBMODULO'] == submodulo) & (df['BECADO'] == 'SI')&(df['MOMENTO']==momentos)]
         
    
        estudiante=df_filtrado['NOMBRE']
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=estudiante, y=df_filtrado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=estudiante, y=df_filtrado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=estudiante, y=df_filtrado['PRODUCTO'])
        ])

        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        st.table(df_filtrado[['NOMBRE', 'CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']].head(20))
    
    elif mañanaTarde:
        df_filtrado = df[(df['ESTADO'] == 'FORMACIÓN') & (df['JORNADA'] == 'MAÑANA-TARDE') & (df['SUBMODULO'] == submodulo) & (df['BECADO'] == 'SI')&(df['MOMENTO']==momentos)]
        
    
        estudiante=df_filtrado['NOMBRE']
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=estudiante, y=df_filtrado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=estudiante, y=df_filtrado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=estudiante, y=df_filtrado['PRODUCTO'])
        ])

        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        st.table(df_filtrado[['NOMBRE', 'CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']].head(20))
    
    elif tarde: 
        df_filtrado = df[(df['ESTADO'] == 'FORMACIÓN') & (df['JORNADA'] == 'MAÑANA-TARDE') & (df['SUBMODULO'] == submodulo) & (df['BECADO'] == 'SI')&(df['MOMENTO']==momentos)]
        df_filtrado= df_filtrado.reset_index(drop=True) 
    
        estudiante=df_filtrado['NOMBRE']
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=estudiante, y=df_filtrado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=estudiante, y=df_filtrado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=estudiante, y=df_filtrado['PRODUCTO'])
        ])

        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        st.table(df_filtrado[['NOMBRE', 'CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']].head(20))

    elif noche:
        df_filtrado = df[(df['ESTADO'] == 'FORMACIÓN') & (df['JORNADA'] == 'MAÑANA-TARDE') & (df['SUBMODULO'] == submodulo) & (df['BECADO'] == 'SI')&(df['MOMENTO']==momentos)]
        tabla1 = (df_filtrado[['NOMBRE', 'CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']].head(20))
        
        estudiante=df_filtrado['NOMBRE']
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=estudiante, y=df_filtrado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=estudiante, y=df_filtrado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=estudiante, y=df_filtrado['PRODUCTO'])
        ]) 
        
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning('Por favor selecciona una jornada.')

        

filtros =[
    "Notas por grupo",
    "Notas por estudiante",
    "Notas según jornada y beca"
]

filtro = st.selectbox("Filtros",filtros)

if filtro:
    filtro_index = filtros.index(filtro)

    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()
    elif filtro_index == 2:
        filtro3()
