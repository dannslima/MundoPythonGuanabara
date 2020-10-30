#crie um programa que tenha uma função fatorial () que receba dois parametros: O
#primeiro que indique o numero a calcular e o outro chamado Show, que será um valor
#logico (opcional) indicando se será mostrado ou nao o processo de calculo de fatorial.


def fatorial(n,show = False):
    """

    :param n: O numero de Fatorial a ser calculado
    :param show: Mostrar ou não a conta
    :return: Ele retorna o valor do Fatorial de um numero n.
    """
    f = 1
    for c in range (n , 0, -1):
        f *= c

    if show == True:

        for c in range (n , 0 , -1):
            if c == 1 :
                print (f' {c} = ', end ='')
            else:
                print(f' {c} X ', end='')
            c += 1
    return f

n = int (input('Digite o número para o fatorial '))

show = input('Deseja saber a equação ?').upper()
if  show == 'SIM':
    show = True

print (fatorial(n, show))

