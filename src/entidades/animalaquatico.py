animaisaquaticos = []


def get_animaisaquaticos() : return animaisaquaticos


def inserir_animalaquatico(animalaquatico): animaisaquaticos.append(animalaquatico)


class Animalaquatico:
    def __init__(self, nome, peso, habitat, riscoextincao=False):
        self.nome = nome
        self.habitat = habitat if habitat in ('oceano', 'mar fechado', 'água doce') else 'indefinida'
        self.peso = peso
        self.riscoextincao = riscoextincao



    def __str__(self):
        if self.riscoextincao: riscoextincao_str = 'riscoextincao |'
        else: riscoextincao_str = ''
        formato = '{} {:<18} {} {:<9} {} {:<12} {} {}'
        animalaquatico_formatado = formato.format('|', self.nome, '|', f'{self.peso:.1f}' + ' kg', '|', self.habitat, '|', riscoextincao_str)
        return animalaquatico_formatado



def selecionar_animalaquatico(habitat = None, peso_minimo = None, riscoextincao = None):
    filtros = '\nFiltros: '
    if habitat is not None: filtros += 'habitat: ' + habitat
    if peso_minimo is not None: filtros += ' - peso minima: '  + str(peso_minimo)
    if riscoextincao: filtros += ' riscoextincao: true '
    elif riscoextincao == False: filtros += ' riscoextincao: false'

    animaisaquaticos_selecionados = []

    for animalaquatico in animaisaquaticos:
        if habitat is not None and animalaquatico.habitat != habitat:
            continue
        if peso_minimo is not None and animalaquatico.peso < peso_minimo:
            continue
        if riscoextincao in (True, False) and animalaquatico.riscoextincao != riscoextincao:
            continue
        animaisaquaticos_selecionados.append(animalaquatico)

    return filtros, animaisaquaticos_selecionados