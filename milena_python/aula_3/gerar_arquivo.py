#csv - comma separated values, arquivo separado por ;
#os - operational system, criar arquivos e gerenciar pastas
#matplotlib - biblioteca de gráficos

import csv
import os
import matplotlib.pyplot as plt
import pandas as pd


#nome do arquivo
ARQUIVO_CSV = 'dados_senai.csv'

#verificar se o arquivo existe
#arquivo -> true || false
arquivo_existe = os.path.exists(ARQUIVO_CSV)

#salvar arquivo
#a, acrescimo, adcionar novo valor
#newline, tira linhas vazias
#encoding, codificações caracteres pt
def salvar_em_csv (nome, idade, email): 
    with open(ARQUIVO_CSV, mode = 'a', newline = '', encoding = 'utf-8') as arquivo:
        escritor = csv.writer(arquivo) #escritor para reescrever o arquivo

        if not arquivo: #se o arquivo não existir, criar uma nova linha, writerow
            escritor.writerow(['nome', 'idade', 'email'])

        escritor.writerow([nome, idade, email])

#queremos identificar a faixa etária dos usuários do sistema
def mostrar_graficos():
    faixas = {
        '0-17': 0,
        '18-30': 0,
        '31-45': 0,
        '46-60': 0,
        '60+': 0
    }

    #mode r, leitura
    with open(ARQUIVO_CSV, mode = 'r', encoding = 'utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        #percorre enquanto tiver linha
        for linha in leitor: 
            try:
                idade = int(linha['idade'])
                if idade <= 17:
                    faixas['0-17'] += 1
                elif idade <= 30:
                    faixas['18-30'] += 1
                elif idade <= 45:
                    faixas['31-45'] += 1
                elif idade <= 60:
                    faixas['46-60'] += 1
                else:
                    faixas['60+'] += 1

            except ValueError:
                continue

        plt.bar(faixas.keys(), faixas.values(), color = 'skyblue')
        plt.title('Distribuição por Faixa Etária')
        plt.xlabel('Faixa Etária')
        plt.ylabel('Quantidade de Pessoas')
        plt.grid(True, linestyle = '--', alpha = 0.5)
        plt.tight_layout() #ajusta layout e gráficos internos
        plt.show()

#função principal
#repetir infinitamente
def main():
    while True:
        print('\n Digite os dados do usuário:')
        nome = input('Nome:')
        idade = input('Idade:')
        email = input('Email:')

        salvar_em_csv(nome, idade, email) #chamando a função para salvar no arquivo csv
        print('Dados salvos com sucesso!')

        continuar = input('Deseja adicionar outro? s/n')
        if continuar != 's':
            break

    mostrar_graficos()

if __name__ == '__main__':
    main()