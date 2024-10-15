class MinhaClasse:
    atributo_classe = "Valor do atributo da classe"
    
    @classmethod
    def metodo_de_classe(cls):
        print("Este é um método de classe")
        print("Acessando o atributo da classe: ", cls.atributo_classe)

# Chamando o método de classe diretamente na classe
MinhaClasse.metodo_de_classe()