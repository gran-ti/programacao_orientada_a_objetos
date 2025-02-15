class Produto:
    def __init__(self, codigo, nome, quantidade):
        self._codigo = codigo
        self._nome = nome
        self._quantidade = quantidade
    
    # Getter para o atributo "codigo"
    @property
    def codigo(self):
        return self._codigo
    
    # Setter para o atributo "codigo"
    @codigo.setter
    def codigo(self, novo_codigo):
        self._codigo = novo_codigo
    
    # Getter para o atributo "nome"
    @property
    def nome(self):
        return self._nome
    
    # Setter para o atributo "nome"
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    #Getter para o atributo "quantidade"
    @property
    def quantidade(self):
        return self._quantidade
    
    # Setter para o atributo "quantidade"
    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade

produto1 = Produto("123", "camiseta", 10)

print(produto1.codigo)      #123
print(produto1.nome)        # Camiseta
print(produto1.quantidade)  # 10

produto1.codigo = "456"
produto1.nome = "Calça"
produto1.quantidade = 5

print(produto1.codigo)      # 456
print(produto1.nome)        # Calça
print(produto1.quantidade)  # 5