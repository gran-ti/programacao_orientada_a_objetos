try:
    # Código que pode gerar exceção
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    resultado = x / y
    print(f"O resultado da divisão é: {resultado}" )

except ValueError:
    # Código para tratar exceção de valor inválido
    print("Você deve digitar apenas números inteiros.")

except ZeroDivisionError:
    # Código para tratar exceção de divisão por zero
    print("Não é possível dividir por zero.")

else:
    # Código que será executado se não houver exceções
    print("Cálculo realizado com sucesso!")

finally:
    # Código que será executado sempre, com ou sem exceção
    print("Programa encerrado.")