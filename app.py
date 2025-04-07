import streamlit as st
import pandas as pd
import plotly_express as px

vehicles = pd.read_csv('vehicles.csv')
st.header('Conjunto de dados de carros')
hist_button = st.button('Clique para criar o histograma')
if hist_button:
            st.write('Conjunto de dados de anúncios de vendas de carros')
            fig1 = px.histogram(vehicles, x="odometer")
            st.plotly_chart(fig1, use_container_width=True)
dispersion_button = st.button('Clique para criar um gráfico de dispersão')
if dispersion_button:
            fig2 = px.scatter(vehicles, x="odometer", y="price")
            st.plotly_chart(fig2, use_container_width=True)