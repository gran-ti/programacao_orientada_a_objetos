class Produto:
    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade

    def exibir_dados(self):
        print(f"Código: {self.codigo}\nNome: {self.nome}\nQuantidade: {self.quantidade}")

class produtoEletronico(Produto):
    def __init__ (self, codigo, nome, quantidade, marca):
        super().__init__(codigo, nome, quantidade)
        self._marca = marca

def exibir_marca(self):
    print(f"Marca: {self._marca}")