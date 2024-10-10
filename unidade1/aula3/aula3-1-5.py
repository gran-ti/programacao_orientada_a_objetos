soma = 0
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / 10
print(f"A média dos números é: {media}")