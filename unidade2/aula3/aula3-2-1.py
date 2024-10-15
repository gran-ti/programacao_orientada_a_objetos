class Produto:
    def __init__ (self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
    
    def mostrar_detalhes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self. nome}" )
        print(f"Quantidade: {self.quantidade}")
    
    def adicionar_estoque(self, quantidade):    
        self.quantidade += quantidade

# Criando um objeto "produtol" da classe "Produto"
produto1 = Produto(1, "Camisa",10)

# Chamando o método "mostrar detalhes" do objeto "produtol"
produto1.mostrar_detalhes()

# Adicionando estoque ao objeto "produtol"
produto1.adicionar_estoque (5)

# Chamando o método "mostrar detalhes" novamente para verificar a quantidade atualizada
produto1.mostrar_detalhes()