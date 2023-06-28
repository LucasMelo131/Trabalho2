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
import matplotlib.pyplot as mp

#mostra o conteudo do csv
df = pd.read_csv('epl_results_2022-23.csv')
print(df.to_string())

df.plot.scatter(x = 'HY',y = 'HF')
mp.show()

"""
for d in df:
    print(d[15]); print(d[17])
    #mp.plot(d[15],d[17])
    #mp.show()
"""
