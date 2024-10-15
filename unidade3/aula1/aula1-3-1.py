class Categoria:
    def __init__ (self, nome):
        self.nome = nome

class Produto:
    def __init__ (self, codigo, nome, quantidade, categoria):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.categoria = categoria
    
    def mostrar_detalhes(self):
        print("Deta1hes do produto:")
        print("Código: ", self.codigo)
        print("Nome: ", self. nome)
        print("Quantidade : ", self.quantidade)
        print("Categoria : ", self.categoria.nome)

# Criando uma instancia da classe Categoria
categoria = Categoria("Eletrônicos")

# Criando uma instância da classe Produto, passando a categoria como argumento
produto = Produto(1,"celular",10, categoria)

# chamando o método mostrar_detalhes do produto
produto.mostrar_detalhes()