aquarios = {}

def get_aquarios(): return aquarios

def inserir_aquario(aquario):
    nome_aquario = aquario.nome
    if nome_aquario not in aquarios.keys():
        aquarios[nome_aquario] = aquario
        return True
    else:
        print('Aquário ' + nome_aquario + ' já está cadastrado')
        return False

class Aquario:
    def __init__(self, nome, cidade, capacidade):
        self.nome = nome
        self.cidade = cidade
        self.capacidade = capacidade
        self.animais_aquaticos = {}

    def __str__(self):
        formato = '{} {:<20} {} {:<14} {} {:<4} {}'
        return formato.format('|', self.nome, '|', self.cidade, '|', str(self.capacidade), '|')

    def inserir_animais_aquaticos(self, animal):
        chave_animal = animal.nome
        if chave_animal not in self.animais_aquaticos.keys(): self.animais_aquaticos[chave_animal] = animal
        else:
            print('Animal aquático' +chave_animal+ 'já está cadastrado no aquário')
