<<<<<<< HEAD
"""
Trabalho 2
->Encontrar um arquivo CSV base
->Apresentar o conteúdo do arquivo
    ->Conteúdo
    ->Colunas
->Apresentar seus dados graficamente

Alunos: Gabriel Moura, Lucas Melo
"""

import pandas as pd
import matplotlib.pyplot as plt

#leitura do csv
ARQ = "epl_results_2022-23.csv"
dfpl = pd.read_csv(ARQ)
lista_colunas = list(dfpl.columns)
dfpl.head(400)

#exibição das colunas
print("colunas: ",lista_colunas)

# Calcular a média de faltas por equipe (em casa e fora)
faltas_por_equipe = dfpl.groupby('HomeTeam')['HF'].sum().reset_index()
faltas_por_equipe.columns = ['Equipe', 'Faltas Casa']

faltas_por_equipe_away = dfpl.groupby('AwayTeam')['AF'].sum().reset_index()
faltas_por_equipe_away.columns = ['Equipe', 'Faltas Fora']

# Calcular a média de cartões amarelos por equipe (em casa e fora)
cartoes_amarelos_por_equipe = dfpl.groupby('HomeTeam')['HY'].sum().reset_index()
cartoes_amarelos_por_equipe.columns = ['Equipe', 'Cartões Amarelos Casa']

cartoes_amarelos_por_equipe_away = dfpl.groupby('AwayTeam')['AY'].sum().reset_index()
cartoes_amarelos_por_equipe_away.columns = ['Equipe', 'Cartões Amarelos Fora']

# Juntar os DataFrames das médias de faltas e cartões amarelos por equipe (apenas em casa)
resultadohome = pd.merge(faltas_por_equipe, cartoes_amarelos_por_equipe, on='Equipe')

#Juntar os DataFrames das médias de faltas e cartões amarelos por equipe (apenas fora de casa)
resultadoaway = pd.merge(faltas_por_equipe_away, cartoes_amarelos_por_equipe_away, on='Equipe')

# juntar os 2 dataframes com as estatísticas em casa e fora por equipe
df_final = pd.merge(resultadohome, resultadoaway, on='Equipe')

# cálculo e criação de colunas com a média de faltas e média de cartões amarelos por equipe
total_faltas = lambda x: x['Faltas Casa'] + x['Faltas Fora']
total_cartao = lambda x: x['Cartões Amarelos Casa'] + x['Cartões Amarelos Fora']
media_falta = lambda x: round(x['Faltas']/38,2)
media_cartao = lambda x: round((x['Cartão Amarelo'])/38,2)
df_final['Faltas'] = df_final.apply(total_faltas,axis = 1)
df_final['Cartão Amarelo'] = df_final.apply(total_cartao,axis = 1)
df_final['Média Falta'] = df_final.apply(media_falta,axis = 1)
df_final['Média Cartão Amarelo'] = df_final.apply(media_cartao,axis = 1)
df_final = df_final.drop(['Faltas Casa','Faltas Fora','Cartões Amarelos Casa'
                          ,'Cartões Amarelos Fora'],axis=1)

df_ord_faltas = df_final.sort_values(by='Média Falta')
df_ord_cartoes = df_final.sort_values(by='Cartão Amarelo')
print(df_ord_cartoes.head(20))

equipes = df_ord_faltas["Equipe"].tolist()
m_falta = df_ord_faltas["Média Falta"].tolist()
equipes2 = df_ord_cartoes["Equipe"].tolist()
m_cartao = df_ord_cartoes["Cartão Amarelo"].tolist()

fig = plt.subplots(figsize=(12, 8))

plt.subplot(2,1,1)
plt.barh(equipes,m_falta, color="green")
plt.ylabel("Equipes")
plt.xlabel("Média de Faltas")
plt.subplot(2,1,2)
plt.barh(equipes2,m_cartao, color="yellow")
plt.ylabel("Equipes")
plt.xlabel("Cartões Amarelos")
plt.show()
=======
import pandas as pd
import matplotlib.pyplot as plt

#leitura do csv
url = "epl_results_2022-23.csv"
dfpl = pd.read_csv(url)
lista_colunas = list(dfpl.columns)
dfpl.head(400)

#exibição das colunas
#print("colunas: ",lista_colunas)

# Calcular a média de faltas por equipe (em casa e fora)
faltas_por_equipe = dfpl.groupby('HomeTeam')['HF'].sum().reset_index()
faltas_por_equipe.columns = ['Equipe', 'Faltas Casa']

faltas_por_equipe_away = dfpl.groupby('AwayTeam')['AF'].sum().reset_index()
faltas_por_equipe_away.columns = ['Equipe', 'Faltas Fora']

# Calcular a média de cartões amarelos por equipe (em casa e fora)
cartoes_amarelos_por_equipe = dfpl.groupby('HomeTeam')['HY'].sum().reset_index()
cartoes_amarelos_por_equipe.columns = ['Equipe', 'Cartões Amarelos Casa']

cartoes_amarelos_por_equipe_away = dfpl.groupby('AwayTeam')['AY'].sum().reset_index()
cartoes_amarelos_por_equipe_away.columns = ['Equipe', 'Cartões Amarelos Fora']

# Juntar os DataFrames das médias de faltas e cartões amarelos por equipe (apenas em casa)
resultadohome = pd.merge(faltas_por_equipe, cartoes_amarelos_por_equipe, on='Equipe')

#Juntar os DataFrames das médias de faltas e cartões amarelos por equipe (apenas fora de casa)
resultadoaway = pd.merge(faltas_por_equipe_away, cartoes_amarelos_por_equipe_away, on='Equipe')

# juntar os 2 dataframes com as estatísticas em casa e fora por equipe
df_final = pd.merge(resultadohome, resultadoaway, on='Equipe')

# cálculo e criação de colunas com a média de faltas e média de cartões amarelos por equipe
media_falta = lambda x: round((x['Faltas Casa'] + x['Faltas Fora'])/38,3)
df_final['Média Falta'] = df_final.apply(media_falta,axis = 1)
media_cartao = lambda x: round((x['Cartões Amarelos Casa'] + x['Cartões Amarelos Fora'])/38,3)
df_final['Média Cartão Amarelo'] = df_final.apply(media_cartao,axis = 1)
df_ord_faltas = df_final.sort_values(by='Média Falta')
#print(df_ord_faltas.head(20))

df_ord_cartoes = df_final.sort_values(by='Média Cartão Amarelo')
#print(df_ord_cartoes.head(20))

#print(df_ord_faltas.columns)

equipes = df_ord_faltas["Equipe"].tolist()
m_falta = df_ord_faltas["Média Falta"].tolist()
m_cartao = df_ord_faltas["Média Cartão Amarelo"].tolist()

fig = plt.subplots(figsize=(12, 8))

plt.subplot(2,1,1)
plt.barh(equipes,m_falta, color="green")
plt.ylabel("Equipes")
plt.xlabel("Média de Faltas")
plt.subplot(2,1,2)
plt.barh(equipes,m_cartao, color="yellow")
plt.ylabel("Equipes")
plt.xlabel("Média de Cartões Amarelos")
plt.show()
>>>>>>> 6536bcabfd4bce67e1f84395e71571d165301b94
