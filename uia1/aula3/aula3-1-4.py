candidato_1 = 0
candidato_2 = 0
votos_nulos= 0
for i in range(5):
    voto = int(input(f"Digite o voto do aluno {i+1}: "))
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    else:
        votos_nulos += 1
print(f"Tota de votos para o candidato 1: {candidato_1}")
print(f"Tota de votos para o candidato 2: {candidato_2}")
print(f"Tota de votos nulos: {votos_nulos}")