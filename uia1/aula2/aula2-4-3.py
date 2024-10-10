salario_bruto = float(input('digite o seu salario: '))
if salario_bruto < 2000:
    gratificaçao = salario_bruto * 5/10
elif salario_bruto >= 2000 and salario_bruto <= 2500:
    gratificaçao = salario_bruto * 10/100
elif salario_bruto > 2500 and salario_bruto <= 3000:
    gratificaçao = salario_bruto * 15/100
else:
    gratificaçao = salario_bruto * 20/100
salario_liquido = salario_bruto + gratificaçao

print(f'Seu salario liquido é de R${salario_liquido:.2f}')
print(f'Sua gratificação foi de R${gratificaçao:.2f}')