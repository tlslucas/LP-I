adaquarios = {}

def get_aquarios():
    return aquarios

def inserir_aquario(aquario):
    nome_aquario = aquario.nome
    if nome_aquario not in aquarios:
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
        self.animal_aquatico = {}

    def __str__(self):
        formato = '{} {:<25} {} {:<18} {} {:<6} {}'
        return formato.format('|', self.nome, '|', self.cidade, '|', str(self.capacidade), '|')

    def inserir_animal_aquatico(self, animal):
        nome_animal = animal.nome
        if nome_animal not in self.animal_aquatico:
            self.animal_aquatico[nome_animal] = animal
        else:
            print(f'Animal aquático {nome_animal} já está cadastrado no aquário')
