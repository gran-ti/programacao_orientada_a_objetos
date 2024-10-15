def somar(a, b):
    resultado = a + b
    print(f"O resultado da soma é {resultado}")

somar(2, 3)

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

minha_lista = ["maçã", "banana", "laranja"]
imprimir_lista(minha_lista)

variavel_global = "Esta é uma variável global"
def imprimir_variavel():
    variavel_local = "Esta é uma variável local"
    print(variavel_global)
    print(variavel_local)

imprimir_variavel()
print(variavel_global)
print(variavel_local) # Erro: variável local não definida