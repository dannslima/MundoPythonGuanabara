#Crie um programa que tenha uma função chamada voto() que vai receber
#como parametro o ano de nascimento de uma pessoa. retornando um valor
#literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas
#eleições
from datetime import datetime
now = datetime.now ()
print (now.year)

def voto(anoNascimento):
    anoAtual = now.year
    idade = anoAtual - anoNascimento
    if idade < 16:
       print(f' Pessoa não vota. sua idade é {idade}')
    elif idade >= 16 and anoNascimento <= 17:
        print(f' Pessoa  vota Opcionalmente. sua idade é {idade}')
    else:
        print(f' Pessoa  vota. sua idade é {idade}')


anoNascimento = int(input('Digite o ano do seu nascimento '))
voto(anoNascimento)