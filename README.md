# Análise Interativa da Venda de Veículos
Este projeto Streamlit oferece uma análise visual e interativa de um conjunto de dados de vendas de veículos, permitindo explorar tendências de preços, distribuição de anos de fabricação e outros insights importantes.

## Funcionalidades
Histogramas: Visualize a distribuição do ano de fabricação dos carros à venda.
Gráficos de Dispersão: Explore a relação entre preço e ano de fabricação, e entre preço e odômetro.
Tabelas Dinâmicas: Liste os carros mais caros ou mais baratos, com informações detalhadas sobre cada veículo.

## Como Executar
Clone o Repositório:

```bash
git clone https://github.com/seu-usuario/analise-venda-veiculos.git
cd analise-venda-veiculos
```
## Instale as Dependências:

```bash
pip install -r requirements.txt
```
## Execute o Aplicativo:

```bash
streamlit run app.py
```
Acesse no Navegador: Abra seu navegador e acesse http://localhost:8501.

## Estrutura do Código
* import streamlit as st: Importa a biblioteca Streamlit para criar a interface do usuário.
* import pandas as pd: Importa a biblioteca Pandas para manipulação e análise de dados.
* import plotly_express as px: Importa a biblioteca Plotly Express para criar gráficos interativos.

O código realiza as seguintes etapas:

1. Importação e Limpeza dos Dados: Carrega os dados do arquivo CSV vehicles.csv, trata valores ausentes e duplicados, e converte tipos de dados para garantir a consistência.

2. **Interface do Usuário**:

* Cria um cabeçalho e exibe uma imagem.
* Adiciona botões para exibir histogramas e gráficos de dispersão.
* Cria um menu suspenso para selecionar entre carros mais caros e mais baratos.
* Exibe tabelas com os carros selecionados.

3. **Visualizações**:

* Utiliza Plotly Express para criar histogramas e gráficos de dispersão interativos.

4. **Interatividade**:

* Permite ao usuário controlar quais visualizações e tabelas são exibidas.

## Considerações Finais
Este projeto demonstra como o Streamlit pode ser utilizado para criar aplicativos de análise de dados poderosos e fáceis de usar. Sinta-se à vontade para explorar o código, adaptá-lo às suas necessidades e contribuir com melhorias!

**Observação**: Certifique-se de ter o arquivo vehicles.csv na mesma pasta do seu script Python e de ter as bibliotecas streamlit, pandas e plotly_express instaladas.

**Site para Render**: https://python-web-deploy.onrender.com/
