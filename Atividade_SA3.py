#Exercício Calculadora de Troco SA3

print('{:^30}'.format('CALCULADORA DE TROCO'))
print('=' * 50)
compras = float(input('Quanto deu o total de suas compras?'))
dinheiro = float(input('Quanto você tem em dinheiro?'))
print('=' * 50)
valor = round((dinheiro - compras), 2)

print('=' * 50)
print(f'Valor do seu troco é de R$:{valor} ')

cem = int(valor / 100)
valor = valor - (cem * 100)

cinquenta = int(valor / 50)
valor = valor - (cinquenta * 50)

dez = int(valor / 10)
valor = valor - (dez * 10)

cinco = int(valor / 5)
valor = valor - (cinco * 5)

dois = int(valor / 2)
valor = valor - (dois * 2)

um = int(valor / 1)
valor = valor - (um * 1)

cinquentaCent = int(valor / 0.50)
valor = valor - (cinquentaCent * 0.50)

vinteCincoCent = int(valor / 0.25)
valor = valor - (vinteCincoCent * 0.25)

dezCent = int(valor / 0.10)
valor = valor - (dezCent * 0.10)

cincoCent = int(valor / 0.05)
valor = valor - (cincoCent * 0.05)

print('=' * 50)
print('Notas R$100,00 = ', cem)
print('Notas R$ 50,00 = ', cinquenta)
print('Notas R$ 10,00 = ', dez)
print('Notas R$  5,00 = ', cinco)
print('Notas R$  2,00 = ', dois)
print('Notas R$  1,00 = ', um)
print('Notas R$  0,50 = ', cinquentaCent)
print('Notas R$  0,25 = ', vinteCincoCent)
print('Notas R$  0,10 = ', dezCent)
print('Notas R$  0,05 = ', cincoCent)