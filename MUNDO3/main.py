itens = dict()
carrinho =  list()

valortotal = 0
while True:
    itens.clear()
    itens['item']= str(input('Digite o nome do Item ')).upper()
    itens['quantidade']=int(input('Digite a quantidade deste item '))
    itens['Valor Unitário']= float(input('Digite o valor unitário do item '))
    valortotal =  valortotal + itens['Valor Unitário']
    itens['Peso'] = float(input('Digite o Peso do item KG '))
    carrinho.append(itens.copy())
    while True:
        resposta = str(input('Deseja adcionar mais itens \n SIM [S] NÃO [N] ?')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resposta == 'N':
        break

for i in carrinho:
    for k, v in i.items():
        print (f' {k} __ {v}')

    print ('-'* 30)


print(f' Houveram {len(carrinho)} produtos variados')
print(f' O valor total do carrinho foi R${valortotal}')



