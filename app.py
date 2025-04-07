import streamlit as st
import pandas as pd
import plotly_express as px

vehicles = pd.read_csv('vehicles.csv')
st.header('Conjunto de dados de carros')
hist_button = st.button('Clique para criar o histograma')
if hist_button:
            st.write('Número de carros por quilometragem')
            fig1 = px.histogram(vehicles, x="odometer", labels={'odometer': 'quilometragem', 'count': 'Número de carros'})
            st.plotly_chart(fig1, use_container_width=True)
dispersion_button = st.button('Clique para criar um gráfico de dispersão')
if dispersion_button:
            st.write('Preço dos carros por quilometragem')
            fig2 = px.scatter(vehicles, x="odometer", y="price", labels={'odometer': 'quilometragem', 'price': 'preço'})
            st.plotly_chart(fig2, use_container_width=True)