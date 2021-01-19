#Crie um programa que tenha uma tupla com várias palavras
#(Não usar acentos). Depois disso voce deve mostrar para cada palavra quais são as suas vogais

palavras = ('laranja','mamao','limao','acabaxi','pera','uva','maca')
print(palavras)
for v in palavras:
    print(f' \n Na palavra {v} temos ', end='')
    for letra in v:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')