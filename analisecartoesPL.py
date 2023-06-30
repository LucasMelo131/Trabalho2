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
from matplotlib import pyplot as plt

#leitura do csv
ARQ = "epl_results_2022-23.csv"
dfpl = pd.read_csv(ARQ)
lista_colunas = list(dfpl.columns)
print(dfpl.head(400))

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

# Juntar os dataframes das médias de faltas e cartões amarelos por equipe (apenas em casa)
resultadohome = pd.merge(faltas_por_equipe, cartoes_amarelos_por_equipe, on='Equipe')

# Juntar os dataframes das médias de faltas e cartões amarelos por equipe (apenas fora de casa)
resultadoaway = pd.merge(faltas_por_equipe_away, cartoes_amarelos_por_equipe_away, on='Equipe')

# Juntar os 2 dataframes com as estatísticas em casa e fora por equipe
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
#print(df_final.head(20))

equipes = df_ord_faltas["Equipe"].tolist()
m_falta = df_ord_faltas["Média Falta"].tolist()
m_cartao = df_ord_faltas["Cartão Amarelo"].tolist()

fig, axes = plt.subplots(figsize=(16, 9), nrows=2, ncols=1)

axes[0].barh(equipes, m_falta, color="green")
axes[0].set_ylabel("Equipes")
axes[0].set_xlabel("Média de Faltas")

axes[1].barh(equipes, m_cartao, color="yellow")
axes[1].set_ylabel("Equipes")
axes[1].set_xlabel("Cartões Amarelos")

# Adicionar valores do eixo x como índices ao lado de cada barra
for ax in axes:
    for i, valor in enumerate(ax.patches):
        ax.text(valor.get_width(), valor.get_y() + valor.get_height() / 2,
                f"{round(valor.get_width(), 2)}",
                ha='left', va='center')

plt.tight_layout()
plt.show()
