# Definindo o valor inicial do contador e do acumulador
contador = 0
acumulador = 0
# Usando a repetição para percorrer um intervalo de números de 1 a 5
for i in range(1, 6):
    # Incrementando o contador a cada iteração
    contador += 1
    # Acumulando o valor da variável i no acumulador a cada iteração
    acumulador += i
    # Imprimindo o resultado do contador e do acumulador
print( "Contador: " , contador)
print( "Acumulador: " , acumulador)