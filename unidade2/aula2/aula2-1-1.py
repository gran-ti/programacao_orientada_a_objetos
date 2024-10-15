def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)

resultado = fatorial(5)
print(resultado) # saída: 120