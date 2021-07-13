custo_compras = float(input('Quanto custou as compras?'))
valor_dinheiro = float(input('Quanto tem em dinheiro?'))
print('=' * 50)
troco = round((valor_dinheiro - custo_compras), 2)
print(f'O troco vai ser de R$ {troco} em notas de:')
total = troco
print('=' * 50)
cedulas = 100
cedulas_total = 0
while True:
    if total >= cedulas:
        total -= cedulas
        cedulas_total += 1
    else:
        if cedulas_total > 0:
            print(f'{cedulas_total} cédulas de R${cedulas}')
        if cedulas == 100:
            cedulas = 50
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        elif cedulas == 5:
            cedulas = 2
        elif cedulas == 2:
            cedulas = 1
        elif cedulas == 1:
            cedulas = 0.5
        elif cedulas == 0.5:
            cedulas = 0.05
        elif cedulas == 0.05:
            cedulas = 0.01
        elif cedulas == 0.01:
            cedulas = 1
        cedulas_total = 0
        if total == 0:
            cedulas_total = 0