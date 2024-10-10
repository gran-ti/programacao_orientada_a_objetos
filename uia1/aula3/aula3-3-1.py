candidato1 = 0
candidato2 = 0
nulos = 0
votos = 0
while True:
    voto = int(input("Digite o número do candidato (1 ou 2): "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    else:
        nulos += 1
    votos += 1
    continuar = input("Deseja continuar? (s/n) ")
    if continuar == "n":
        break
print(f"Total de votos: {votos}" )
print(f"Candidato 1: {candidato1} votos")
print(f"Candidato 2: {candidato2} votos")
print(f"Votos nulos: {nulos} votos")