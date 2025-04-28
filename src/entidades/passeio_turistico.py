from src.entidades.aquario import get_aquarios
from src.entidades.animal_aquatico import get_animais_aquaticos
from src.entidades.escola import get_escolas

passeios_turisticos = []

def get_passeios_turisticos():
    return passeios_turisticos

def inserir_passeio_turistico(passeio):
    if passeio not in passeios_turisticos:
        passeios_turisticos.append(passeio)
    else:
        print('Passeio turístico já cadastrado --- ' + str(passeio))

def criar_passeio_turistico(nome_aquario, nome_animal, nome_escola, data):
    aquario = get_aquarios().get(nome_aquario)
    if not aquario:
        print('Aquário ' + nome_aquario + ' não cadastrado')
        return
    animal = aquario.animal_aquatico.get(nome_animal)
    if not animal:
        print('Animal aquático ' + nome_animal + ' não cadastrado no aquário ' + nome_aquario)
        return
    escola = None
    for e in get_escolas().values():
        if e.nome == nome_escola:
            escola = e
            break
    if not escola:
        print('Escola ' + nome_escola + ' não cadastrada')
        return
    passeio = PasseioTuristico(aquario, animal, escola, data)
    inserir_passeio_turistico(passeio)

def selecionar_passeios_turisticos(data_minima_passeio=None, peso_minimo_animal=None,
                                   max_alunos_escola=None, cidade_aquario=None):
    filtros = '\nFiltros -- '
    if data_minima_passeio: filtros += 'data minima: '+str(data_minima_passeio)
    if peso_minimo_animal: filtros += f' - peso minimo do animal: '+str(peso_minimo_animal)
    if max_alunos_escola: filtros += f' - máximo de alunos na escola: '+str(max_alunos_escola)
    if cidade_aquario: filtros += f' - cidade do aquário: '+str(cidade_aquario)

    selecionados = []
    for passeio in passeios_turisticos:
        if data_minima_passeio and passeio.data < data_minima_passeio:
            continue
        if peso_minimo_animal and passeio.animal_aquatico.peso < peso_minimo_animal:
            continue
        if max_alunos_escola and passeio.escola.n_alunos > max_alunos_escola:
            continue
        if cidade_aquario and passeio.aquario.cidade != cidade_aquario:
            continue
        selecionados.append(passeio)
    return filtros, selecionados

class PasseioTuristico:
    def __init__(self, aquario, animal_aquatico, escola, data):
        self.aquario = aquario
        self.animal_aquatico = animal_aquatico
        self.escola = escola
        self.data = data

    def __str__(self):
        formato = '{} {:<25} {} {:<18} {} {:<20} {} {:<10} {}'
        return formato.format('|', self.aquario.nome, '|', self.animal_aquatico.nome, '|',
                              self.escola.nome, '|', str(self.data), '|')

    def str_filtro(self):
        formato = '{:>5} {} {:<18} {} {:<6} {}'
        return self.__str__() + formato.format(self.escola.n_alunos, '|',
                                               self.aquario.cidade, '|',
                                               str(self.animal_aquatico.peso) + 'kg', '|')
