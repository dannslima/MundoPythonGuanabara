#Crie um programa que vai gerar cinco números aleatórios e colocar em uma
# Tupla. Depois disso , mostra a listagem de números gerador e também indique
#o menor e maior valor que estão na tupla

from random import randint
n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print(f'Sorteado o valor {n}')
print (f' O maior valor sorteado foi {max(n)}')
print (f' O menor valor sorteado foi {min(n)}')