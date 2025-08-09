import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('tabela_analise.csv')
df['Receita'] = df['Quantidade'] * df['Preço']
df['Data'] = pd.to_datetime(df['Data'])
df['Mês'] = df['Data'].dt.to_period('M').astype(str)
df['Ano'] = df['Data'].dt.year

st.title('Dashboard de Vendas')

categorias = df['Categoria'].unique()
categoria_selecionada = st.selectbox('Selecione a categoria', categorias)
df_filtrado = df[df['Categoria'] == categoria_selecionada]

st.subheader('Total de Vendas por Mês')
receita_mensal = df_filtrado.groupby('Mês')['Receita'].sum().reset_index()
fig1 = px.line(receita_mensal, x='Mês', y='Receita', markers=True, title=f'Receita Mensal - {categoria_selecionada}')
st.plotly_chart(fig1, use_container_width=True)

st.subheader('Produto Mais Vendido')
quantidade_produto = df_filtrado.groupby('Produto')['Quantidade'].sum().reset_index().sort_values(by='Quantidade', ascending=False)
fig2 = px.bar(quantidade_produto, x='Produto', y='Quantidade', title=f'Produtos Vendidos - {categoria_selecionada}', text_auto=True)
st.plotly_chart(fig2, use_container_width=True)

st.subheader('Receita Total por Categoria')
receita_produto = df_filtrado.groupby('Produto')['Receita'].sum().reset_index().sort_values(by='Receita', ascending=False)
fig3 = px.bar(receita_produto, x='Produto', y='Receita', title=f'Receita por Produto - {categoria_selecionada}', text_auto=True)
st.plotly_chart(fig3, use_container_width=True)

st.subheader('Qauntidade Total de Vendas por Produtos')
fig4 = px.pie(quantidade_produto, names='Produto', values='Quantidade',title=f'Participação dos Produtos Vendidos - {categoria_selecionada}')
st.plotly_chart(fig4, use_container_width=True)