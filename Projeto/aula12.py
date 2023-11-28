nome = 'Wesley Teixeira Da Cunha Souza'
altura = 1.60
peso = 48
imc = ...

imc_calculo =  peso /  (altura * altura)
linha1 = f'{nome} tem {altura:,.2f} de altura'
linha2 =  f'pesa {peso}  quilos'
linha3 =   f'seu imc calculado é {imc_calculo:.2f}'

print (nome, 'tem', altura, 'de altura')
print ('pesa', peso, 'quilos')
print('seu imc calculado é', imc_calculo)
print(linha1)
print(linha2)
print(linha3)