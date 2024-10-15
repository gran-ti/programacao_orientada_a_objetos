class Produto:
    def __init__ (self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
    
    def mostrardetalhes(self):
        print(f"Código: {self. codigo}")
        print(f"Nome: {self.nome}")
        print(f"Quantidade: {self.quantidade}")
    
    def adicionarestoque(self, quantidade):
        self.quantidade += quantidade

class ProdutoEletronico(Produto):
    def __init__ (self, codigo, nome, quantidade, marca):
        super().__init__(codigo, nome, quantidade)
        self.marca = marca
    
    def exibirmarca(self):
        print(f"Marca: {self.marca}")

meu_produto = ProdutoEletronico("001", "Smartphone", 10, "Samsung")