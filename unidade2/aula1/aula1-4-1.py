def calcular_quadrado(numero):
    quadrado = numero ** 2
    return quadrado

resultado = calcular_quadrado(5)
print(resultado) # saída: 25

def encontrar_maior_valor(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior

numeros = [2, 8, 4, 10, 5]
maior_numero = encontrar_maior_valor(numeros)
print(maior_numero) # saída: 10

def calcular_quadrado_e_cubo(numero):
    quadrado = numero ** 2
    cubo = numero ** 3
    return quadrado, cubo

resultado_quadrado, resultado_cubo = calcular_quadrado_e_cubo(3)
print(resultado_quadrado) # saída: 9
print(resultado_cubo) # saída: 27