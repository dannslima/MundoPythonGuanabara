#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre
# A) os 5 primeiros
# B) Os últimos 4 colocados.
# C) Times em Ordem Alfabética.
# D) Em que posição está o time da Chapecoense

brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print('-='*15)
print(f'5 Primeiros Colocados {brasileirao[0:5]}')
print('-='*15)
print(f'Os últimos 4 colocados são {brasileirao[-4:]}')
print('-='*15)
print(f' Ordem Alfabética {sorted(brasileirao)}')
print('-='*15)
print (f'O Chapecó está na {brasileirao.index("Chapecoense")+1}º posição')