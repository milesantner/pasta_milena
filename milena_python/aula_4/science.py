#pandas utilizado para datascience, machine learning, analise e estatistica
import pandas as pd
import matplotlib.pyplot as plt

#ler csv
df = pd.read_csv("aula_4/vendas_loja.csv")

#nome das colunas, criar coluna chamada receita
df["Receita"] = df["Quantidade"] * df["Preço_Unitario"]

total_receita = df["Receita"].sum() #soma, junta todas as linhas em uma só
total_receita2 = df["Receita"] #unitario
print(total_receita2)
print("Total de vendas R$", total_receita) #total de receita faturado

media_receita = df["Receita"].mean() #medial
print("Média da Receita R$", media_receita)

#produto mais vendido em quantidade
produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax() #indmax pega o valor mais alto
print("Produto mais vendido:", produto_mais_vendido)

categoria_maior_receita = df.groupby("Categoria")["Receita"].sum().idxmax()
print("Categoria com maior receita:", categoria_maior_receita)

#gráfico de barras - receita por categoria
df.groupby("Categoria").sum().plot(kind='bar', title='Receita por Categoria') #plt - gerar gráfico
plt.ylabel("Receita (R$)")
plt.tight_layout() #finalizar layout
plt.show() #exibir gráficos

#gráfico de linha - Receita por mês
#datatime
df["Data"] = pd.to_datetime(df["Data"])
df["Mes"] = df["Data"].dt.to_period("M") #capturando M - mês da data
df.groupby("Mes")["Receita"].sum().plot(kind='line', title='Receita Mensal') 
plt.ylabel("Receita R$")
plt.xlabel("Mês")
plt.tight_layout()
plt.show()