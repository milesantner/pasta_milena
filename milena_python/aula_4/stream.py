#biblioteca para criação de dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#carregar dados
df = pd.read_csv('vendas_loja.csv')
df['Receita'] = df['Quantidade'] * df['Preço_Unitario']
df['Data'] = pd.to_datetime(df['Data'])
df['Mês']  = df['Data'].dt.to_period('M')

st.title('Dashboard de Vendas')

#principais informações
#f "R$ {}" - format (string)
st.metric("Total de Vendas", f"R$ {df['Receita'].sum():,.2f}")
st.metric("Média por Venda", f"R$ {df['Receita'].mean():,.2f}")

#filtro por categoria
categorias = df['Categoria'].unique() #categoria é única
categoria_selecionada = st.selectbox('Selecione a categoria', categorias)
df_filtrado = df[df['Categoria'] == categoria_selecionada]

#gráfico por produto
st.subheader('Recetita por Produto')
fig1, ax1 = plt.subplots() #criar uma figura que será o gráfico
df_filtrado.groupby('Produto')['Receita'].sum().plot(kind='bar', ax=ax1)
st.pyplot(fig1)

#gráfico por mês
st.subheader('Receita Mensal')
fig2, ax2 = plt.subplots()
df.groupby('Mês')['Receita'].sum().plot(ax=ax2)
st.pyplot(fig2)