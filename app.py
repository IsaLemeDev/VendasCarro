import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles.csv')

st.header('Dashboard de Vendas de Carros') 

st.write('Bem-vindo ao dashboard de vendas de carros! Explore os dados de anúncios de vendas')
hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: 
           
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
              
    fig = px.histogram(car_data, x="odometer")
        
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão') # criar um botão    

if scatter_button:
    st.write('Criando um gráfico de dispersão: Quilometragem vs Preço')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)  
