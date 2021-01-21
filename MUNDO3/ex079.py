#Crie um progrma qonde o usuario possa digitar varios valores numericos
#e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
#No final , serão exibidos todos os valores unicos digitados em ordem crescente.

lista = []

while True:
    n = int(input('Digite um valor '))
    if n not in lista:
        lista.append(n)
    else:
        print('Numero ja existe ')
    r = str(input('Quer continuar ? [S/N]'))
    if r in 'Nn':
        break;
print(f'Os números digitados foram {lista}')
