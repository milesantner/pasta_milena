import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Dashboard Escolar', layout='wide')
st.title('Dashboard de Desempenho Escolar')

#upload de arquivo
arquivo = st.file_uploader('Envie o arquivo CSV com notas', type=['csv'])

if arquivo:
    try:
        df = pd.read_csv(arquivo)
        df['Data_Prova'] = pd.to_datetime(df['Data_Prova'])
        df['Mês'] = df['Data_Prova'].dt.to_period('M').astype(str)

        #KPI - indicador chave de desempenho
        media_geral = df['Nota'].mean()
        melhor_disciplina = df.groupby('Disciplina')['Nota'].mean().idxmax()
        pior_aluno = df.groupby('Aluno')['Nota'].mean().idxmin()

        #colunas
        col1, col2, col3 = st.columns(3)
        col1.metric('Média Geral', f'{media_geral:.2}')
        col2.metric('Melhor Disciplina', f'{melhor_disciplina}')
        col3.metric('Aluno com menor média', f'{pior_aluno}')

        #filtros
        aluno_sel = st.selectbox('Filtrar por Alunos:', df['Aluno'].unique())
        df_filtrado = df[df['Aluno'] == aluno_sel]

        #gráfico de notas por disciplina do aluno
        st.subheader(f'Notas de {aluno_sel} por disciplina') 
        fig_bar = px.bar(df_filtrado, x='Disciplina', y='Nota', color='Disciplina', text_auto=True) #configurando gráficos de barras
        st.plotly_chart(fig_bar, use_container_width=True) #exibindo gráficos

        #gráfico de linha - evolução das notas do aluno
        st.subheader('Evolução de Notas por Mês')
        fig_linha = px.line(df, x='Mês', y='Nota', color='Aluno', markers=True, title='Notas ao logo do tempo')
        st.plotly_chart(fig_linha, use_container_width=True)

    except Exception as e:
        st.error(f'Error ao processar o arquivo: {e}')
else:
    st.info('Envie um arquivo com as colunas: Aluno, Disciplina, Data_Prova, Nota')