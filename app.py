import streamlit as st
import pandas as pd
import plotly_express as px

# Importando os dados
car_data = pd.read_csv('vehicles.csv')

# Limpeza e correção dos dados
car_data = car_data.dropna(
    subset=['model_year', 'cylinders', 'odometer', 'paint_color']).reset_index(drop=True)
car_data['is_4wd'] = car_data['is_4wd'].fillna(0)
car_data = car_data.drop_duplicates(subset=['model', 'model_year', 'odometer'])
car_data['model_year'] = car_data['model_year'].astype('int')
car_data['odometer'] = car_data['odometer'].astype('int')

# Adicionar o título
st.header("Análise Interativa do Mercado de Veículos")

# Adicionar uma figura
st.image("image.jpg")


# Conteúdo do Histograma do Ano dos carros
show_histogram = st.button('Ano dos carros a venda')
if show_histogram:
    st.write(
        'Histograma de distribuição do ano de fabricação dos carros')
    fig_hist = px.histogram(car_data, x="model_year")
    st.plotly_chart(fig_hist, use_container_width=True)

# Conteúdo do Gráfico de dispersão

show_scatter = st.button('Criar gráfico do preço dos carros baseado por ano')
if show_scatter:
    st.write(
        'Preço dos carros por ano')
    fig_scatter = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Conteúdo do Gráfico de dispersão

show_scatter = st.button(
    'Criar gráfico do preço dos carros baseado pelo odômetro')
if show_scatter:
    st.write(
        'Preço dos carros pelo odômetro')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Botões de seleção
opcao = st.selectbox("Selecione uma opção:", [
                     "Carros Mais Caros", "Carros Mais Baratos"])

# Número de carros a exibir
num_carros = 5

if opcao == "Carros Mais Caros":
    # Ordenar por preço decrescente e selecionar os 5 primeiros
    carros_caros = car_data.nlargest(
        num_carros, "price")
    # Exibir apenas modelo e preço
    st.table(
        carros_caros[["model", "price", "odometer", "model_year", "condition"]])

elif opcao == "Carros Mais Baratos":
    # Ordenar por preço crescente e selecionar os 5 primeiros
    carros_baratos = car_data.nsmallest(
        num_carros, "price")
    st.table(carros_baratos[["model", "price",
             "odometer", "model_year", "condition"]])
