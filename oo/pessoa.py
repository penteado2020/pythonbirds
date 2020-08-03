class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        #Atributo nome é = self.nome
        # e abaixo eu passo o valor do atributo nome o valor do parametro nome
        # alt+Enter já cria a linha de inclusão do atributo, informaado no parametro acima,
        # exemplo idade=35 criará a linha self.idade = idade
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__== '__main__':
    renzo = Pessoa(nome="Renzo")
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    #print(luciano.filhos)