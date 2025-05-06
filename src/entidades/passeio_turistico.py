from src.entidades.aquario import get_aquarios
from src.entidades.escola import get_escolas

passeios_turisticos = []

def get_passeios_turisticos():
    return passeios_turisticos

def inserir_passeio_turistico(passeio):
    if passeio not in passeios_turisticos:
        passeios_turisticos.append(passeio)
    else:
        print('Passeio turístico já cadastrado --- ' + str(passeio))

def criar_passeio_turistico(nome_aquario, nome_animal, cnpj_escola, data):
    aquario = get_aquarios().get(nome_aquario)
    if aquario is None:
        print('Aquário ' + nome_aquario + ' não cadastrado')
        return
    animal = aquario.animal_aquatico.get(nome_animal)
    if animal is None:
        print('Animal aquático ' + nome_animal + ' não cadastrado no aquário ' + nome_aquario)
        return
    escola = get_escolas().get(cnpj_escola)
    if not escola:
        print('Escola ' + cnpj_escola + ' não cadastrada ')
        return
    
    passeio = PasseioTuristico(aquario, animal, escola, data)
    inserir_passeio_turistico(passeio)

def selecionar_passeios_turisticos(data_minima_passeio=None, peso_minimo_animal=None,
                                   max_alunos_escola=None, cidade_aquario=None):
    filtros = '\nFiltros -- '
    if data_minima_passeio: filtros += 'data minima_passeio: '+str(data_minima_passeio)
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
        formato = '{} {:<20} {} {:<17} {} {:<19} {} {:<10} {}'
        return formato.format('|', self.aquario.nome, '|', self.animal_aquatico.nome, '|',
                              self.escola.nome, '|', str(self.data), '|')

    def str_filtro(self):
        formato = '{:>5} {} {:<14} {} {:<5} {}'
        return self.__str__() + formato.format(self.escola.n_alunos, '|',
                                               self.aquario.cidade, '|',
                                               str(self.animal_aquatico.peso) + 'kg', '|')
