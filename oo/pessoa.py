class Pessoa:
    #A criação do atributo default, deve ficar fora do método def__init__
    #exemplo = olhos=2
    olhos = 2
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
    #Adicionando atributos Dinamicamente     Obs.: Não costuma ser uma boa prática.
    #exemplo: luciano.sobrenome = 'Ramalho '
    #Remover atributos Dinamicamente         bs.: Não costuma ser uma boa prática.
    #exemplo: del luciano.filhos
    #print(luciano.filhos)
    #O __dict__ exibe todos os atributos daquele atributos de instancia de um objeto exemplo print(luciano.__dict__)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(renzo.__dict__)
    print(luciano.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))