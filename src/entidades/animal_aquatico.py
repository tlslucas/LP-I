animais_aquaticos = []

def get_animais_aquaticos():
    return animais_aquaticos

def inserir_animal_aquatico(animal):
    animais_aquaticos.append(animal)

def selecionar_animal_aquatico(habitat=None, risco_extincao=None, peso_máximo=None):
    filtros = '\nFiltros -- '
    if habitat: filtros += 'habitat: ' + habitat
    if risco_extincao in (True, False): filtros += ' - risco de extinção: ' + str(risco_extincao)
    if peso_máximo: filtros += ' - peso máximo: ' + str(peso_máximo)

    selecionados = []
    for animal in animais_aquaticos:
        if habitat and animal.habitat != habitat:
            continue
        if risco_extincao in (True, False) and animal.risco_extincao != risco_extincao:
            continue
        if peso_máximo and animal.peso > peso_máximo:
            continue
        selecionados.append(animal)
    return filtros, selecionados

class AnimalAquatico:
    def __init__(self, nome, habitat, peso, risco_extincao):
        self.nome = nome
        self.habitat = habitat if habitat in ('oceano', 'água doce', 'mar fechado') else 'indefinido'
        self.peso = peso
        self.risco_extincao = risco_extincao

    def __str__(self):
        risco = 'em risco' if self.risco_extincao else 'não ameaçado'
        formato = '{} {:<20} {} {:<12} {} {:<6} {} {:<12} {}'
        return formato.format('|', self.nome, '|', self.habitat, '|', str(self.peso) + ' kg', '|', risco, '|')
