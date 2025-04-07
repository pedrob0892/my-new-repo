import streamlit as st
import pandas as pd
import plotly_express as px

vehicles = pd.read_csv('vehicles.csv')
st.header('Conjunto de dados de carros')
hist_button = st.button('Criar histograma')
if hist_button:
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            fig1 = px.histogram(vehicles, x="odometer")
            st.plotly_chart(fig1, use_container_width=True)
fig2 = px.scatter(vehicles, x="odometer", y="price")
fig2.show()
fig2.plot()