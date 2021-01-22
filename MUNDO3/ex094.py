#Crie um programa que leia nome , sexo e idade de várias pessoas, guardando
#os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. NO final Mostre:

#A) Quantas pessoas cadastradas
#B) A media de idade
#C) Uma lista com mulheres
#D) Uma lista com idade acima da média

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('[M/F]]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor , digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resp =='N':
        break
print('-=' * 30)
print(f' A) Ao todo temos {len(galera)} pessoas cadastradas ')
media = soma / len(galera)
print(f' b) A media de idade é de {media:5.2f} anos ')
print (f'C) as Mulheres cadastradas foram ' , end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >=media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v} ', end=' ')
        print()
print('<< encerrado >>')