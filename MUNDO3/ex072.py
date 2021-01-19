#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte.
#Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e motra-lo por extenso.

cont = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze',
'treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenovo','vinte')

while True:
    num =  int(input('Digite um numero de 0 a 20 '))
    if 0<= num <= 20:
        break
    print('Tente novamente')

print(f' Você digitou o número {cont[num]}')