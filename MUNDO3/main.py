itens = dict()
carrinho =  list()

valortotal = 0
while True:
    itens.clear()
    itens['item']= str(input('Digite o nome do Item ')).upper()
    itens['quantidade']=int(input('Digite a quantidade deste item '))
    itens['Valor Unitário']= float(input('Digite o valor unitário do item '))
    valortotal = itens['Valor Unitário'] * itens['quantidade'] + valortotal
    itens['Peso'] = float(input('Digite o Peso do item KG '))
    carrinho.append(itens.copy())
    while True:
        resposta = str(input('Deseja adcionar mais itens \n SIM [S] NÃO [N] ?')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resposta == 'N':
        break
emails = list()
while True:
    emails.append(str(input('Digite o E-mail para dividir a conta')))
    while True:
        resposta = str(input('Deseja adcionar mais E-MAILS \n SIM [S] NÃO [N] ?')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Responda apenas S ou N')
    if resposta == 'N':
        break


for i in carrinho:
    for k, v in i.items():
        print (f' {k}: {v:.<15} ' , end='|')

    print()
print ('-'* 30)


print(f' Produtos variados {len(carrinho)}')
print(f' O valor total do carrinho foi R${valortotal:.2f}')
print(f' Os e-mails digitados foram :')
for i in emails:
    print( i)



