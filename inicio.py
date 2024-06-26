import streamlit as st

st.image("./static/images/logo.png", width=200)

st.title("Proyecto integrador") 

st.write("Hecho por: Santiago Hernandez Espejo, Juan Camilo Ossa, Estefania Galvis Guainas")

st.subheader("Principal objetivo")

st.write("El principal objetivo de este proyecto de Streamlit es realizar diferentes filtros haciendo uso de Pandas y de la base de datos previamente realizada en Firebase")

st.subheader("CaracterÍsticas y detalles")

st.write("En las diferentes páginas se encuentras contextos y filtros diferentes, entre esas están:")

#Proyecto Integrador

st.write("1. PROYECTO INTEGRADOR: Esta página busca crear filtros para un dataset alojado en Firebase, con proyecto interador nos referimos a aquel proyecto del cual hemos trabajo en diferentes submodulos.")

st.header("Introducción a Replay: Portal de Entretenimiento")

st.image("./static/images/integrador.png", width=400)

st.write("En un panorama de entretenimiento digital en constante evolución, presentamos Replay, una plataforma revolucionaria diseñada para ofrecerte una experiencia de streaming única y personalizada. Con un enfoque en la excelencia tecnológica y la satisfacción del usuario, Replay redefine la forma en que disfrutas del contenido audiovisual y en el corazón de Replay se encuentra una base de datos alojada en Firebase, que actúa como el motor de nuestro servicio.")
st.write("Esta base de datos, alimentada por algoritmos inteligentes, permite una clasificación y organización meticulosa de un vasto catálogo de películas, series y documentales, brindándote acceso a una biblioteca diversa de contenido.")

#Simulador CESDE

st.write("2. SIMULADOR CESDE: Esta página viene como proyecto especifico del submodulo de Nuevas Tecnologias de la Programación, apartir de una base de datos proporionada por el profesor se busca realizar diferentes filtros; esta base de datos consta de diferentes notas de estudiantes de un curso de programación.")

st.image("./static/images/notas.png", width=400)

#Ventas de una tienda online

st.write("3. TERCER PROYECTO: Esta última página consta con un dataset extraído directamente de Kaggle, una plataforma con una amplia comunidad dedicada a ciencias de datos, desde esta plataforma buscamos también crear diferentes filtros que ayude a la buqueda de datos específicos; el dataset usado en este proyecto es de ventas de una tienda online.")

st.image("./static/images/productos.png", width=400)