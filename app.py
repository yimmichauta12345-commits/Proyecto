import pandas as pd
import streamlit as st
import plotly.graph_objects as go

df = pd.read_csv('vehicles_us.csv')


st.header("Analisis exploratorio de datos de vehículos")

#Creando el boton
hist_button = st.checkbox("Construir histograma")

#Logica
if hist_button:
    st.write("Creación de un histrograma para el conjunto de datos de anuncios de venta de autos")

    fig = go.Figure(data=[go.Histogram(x=df["odometer"])])

    fig.update_layout(title_text="Distribución del odometro")

    st.plotly_chart(fig, use_container_width=True)

#Creando el segundo boton
disp_button = st.checkbox("Construir un grafico de dispersión")

#Logica
if disp_button:
    st.write("Creación de un grafico de dispersíon para el conjunto de datos de anuncios de venta de autos")

    fig_2 = go.Figure(data=[go.Scatter(x=df["odometer"], y=df["price"], mode="markers")])

    fig_2.update_layout(title_text="Relación entre odometro y precio",
                        xaxis_title="Kilometraje",
                        yaxis_title="Precio")

    st.plotly_chart(fig_2, use_container_width=True)

