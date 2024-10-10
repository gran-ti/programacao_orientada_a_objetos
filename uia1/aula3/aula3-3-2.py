soma = 0
contador = 0
while contador < 10:
    numero =  int(input("Digite um número inteiro: "))
    soma += numero
    contador += 1

media = soma / 10
print("A média dos números é:" , media)