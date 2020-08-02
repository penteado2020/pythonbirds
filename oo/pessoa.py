class Pessoa:
    def __init__(self, nome=None, idade=35):
        #Atributo nome é = self.nome
        # e abaixo eu passo o valor do atributo nome o valor do parametro nome
        # alt+Enter já cria a linha de inclusão do atributo, informaado no parametro acima,
        # exemplo idade=35 criará a linha self.idade = idade
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__== '__main__':
    p = Pessoa("jeje")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Jefferson'
    print(p.nome)
    print(p.idade)