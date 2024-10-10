# Criando um dicionário
meu_dicionario = {'nome':'Joao', 'idade': 25, 'cidade': 'São Paulo'}
# Acessando elementos do dicionário
print(meu_dicionario['nome']) # Output: João
print(meu_dicionario['idade']) # Output: 25
print(meu_dicionario['cidade']) # Output: São Paulo
# Adicionando um novo elemento ao dicionário
meu_dicionario['profissão'] = 'Engenheiro'
# Acessando o novo elemento adicionado
print(meu_dicionario['profissão']) # Output: Engenheiro
# Atualizando um elemento existente no dicionário
meu_dicionario['idade'] = 30
# Acessando o elemento atualizado
print(meu_dicionario['idade']) # Output: 30

# Removendo um elemento do dicionário com o método pop()
valor_removido = meu_dicionario.pop('cidade') 
print(meu_dicionario) # Output: {'nome': 'Joao', 'idade': 30, 'profissão': 'Engenheiro'}
print(valor_removido) # Output: São Paulo
# Removendo um elemento do dicionário com a instrução del
del meu_dicionario['idade']
print (meu_dicionario)

# Percorrendo as cahves do dicionário
for chave in meu_dicionario:
    print(chave)
# Percorrendo os valores do dicionário
for valor in meu_dicionario.values():
    print(valor)
# Percorrendo as chaves e os valores do dicionário
for chave, valor in meu_dicionario.items():
    print(chave, valor)