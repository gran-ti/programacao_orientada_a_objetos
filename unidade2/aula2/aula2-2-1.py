funcao = lambda x: x * x
resultado = funcao(5)
print(resultado) # saída: 25

def dobro(x):
    return x * 2
lista = [1, 2, 3, 4, 5]
resultado = map(dobro, lista)
print(list(resultado)) # saída: [2, 4, 6, 8, 10]

lista = [1, 2, 3, 4, 5]
resultado = map(lambda x: x * 2, lista)
print(list(resultado)) # saída: [2, 4, 6, 8, 10]

def eh_impar(x):
    return x % 2!= 0
lista = [1, 2, 3, 4, 5]
resultado = filter(eh_impar, lista)
print(list(resultado)) # saída: [1, 3, 5]

lista = [1, 2, 3, 4, 5]
resultado = filter(lambda x: x % 2!= 0, lista)
print(list(resultado)) # saída: [1, 3, 5]

def eh_par(x):
    return x % 2 == 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(eh_par, numeros))
print(pares) # saída: [2, 4, 6, 8, 10]

palavras = ['banana', 'maçã', 'abacaxi', 'laranja', 'uva']
a_words = list(filter(lambda s: s.startswith('a'), palavras))
print(a_words) # saída: [‘abacaxi’]

frase = "Aprendendo Python"
if frase.startswith("Apre"):
    print("A string começa com 'Apre'")
else:
    print("A string não começa com 'Apre'")