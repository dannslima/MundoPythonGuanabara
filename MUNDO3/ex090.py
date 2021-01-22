#Faça um programa que leia nome e media de um aluno, guardando também a
#situação em um dicionario. No final, mostre o conteúdo da estrutura na tela

aluno = dict()
aluno['nome'] = str (input('Nome: '))
aluno ['media'] = float(input(f'Média de {aluno["nome"]} '))

if aluno['media'] >=7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperacao'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f' {k} é igual a {v}')
