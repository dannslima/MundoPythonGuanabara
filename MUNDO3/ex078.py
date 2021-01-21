#Faça um programa que leia 5 valores  númericos e guarde-os em uma lista. No final,
# mostre qual foi a maior e o menor valor digirado e as suas respectivas posições na lista

lista = []
for c in range (0,5):
    lista.append(int(input(f'Digite um valor para a posição {c} ')))

print(f'  Você digitou os valores {lista} ')
print(f' O maior valor digitado foi {max(lista)} ')
maior = max(lista)
print(f' O menor valor digitado foi {min(lista)}')
menor = min(lista)

for indice, valor in enumerate(lista):
    if valor == maior:
        print(f' O maior valor está na posição {indice}')

for indice, valor in enumerate(lista):
    if valor == menor:
        print(f' O menor  valor está na posição {indice}')