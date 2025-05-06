animais_aquaticos = {}

def get_animais_aquaticos():
    return animais_aquaticos

def inserir_animais_aquaticos(animal):
    animais_aquaticos.append(animal)

class AnimalAquatico:
    def __init__(self, nome, habitat, peso, risco_extincao):
        self.nome = nome
        self.habitat = habitat if habitat in ('oceano', 'água doce', 'mar fechado') else 'indefinido'
        self.peso = peso
        self.risco_extincao = risco_extincao

    def __str__(self):
        risco = 'em risco |' if self.risco_extincao else ' '
        formato = '{} {:<17} {} {:<11} {} {:<6} {} {:<7}'
        return formato.format('|', self.nome, '|', self.habitat, '|', str(self.peso) + ' kg', '|', risco)
