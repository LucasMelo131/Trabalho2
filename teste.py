"""
Trabalho 2
->Encontrar um arquivo CSV base
->Apresentar o conteúdo do arquivo
    ->Conteúdo
    ->Colunas
->Apresentar seus dados graficamente
"""

#mostra o conteudo do csv
import pandas as pd
#import matplotlib.pyplot as mp

#mostra o conteudo do csv
resultados = pd.read_csv('epl_results_2022-23.csv')
lista_colunas = list(resultados.columns)
print("Colunas : ",lista_colunas)
#print(resultados.to_string())

