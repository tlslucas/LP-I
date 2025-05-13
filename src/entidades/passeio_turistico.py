from src.entidades.aquario import get_aquarios
from src.entidades.escola import get_escolas

passeios_turisticos = []

def get_passeios_turisticos():
    return passeios_turisticos

def inserir_passeio_turistico(passeio_turistico):
    if passeio_turistico not in passeios_turisticos:
        passeios_turisticos.append(passeio_turistico)
    else:
        print('Passeio turístico já cadastrado --- ' + str(passeio_turistico))

def criar_passeio_turistico(nome_aquario, cnpj_escola, data):
    aquario = get_aquarios().get(nome_aquario)
    if aquario is None:
        print('Aquário ' + nome_aquario + ' não cadastrado')
        return
    escola = get_escolas().get(cnpj_escola)
    if not escola:
        print('Escola ' + cnpj_escola + ' não cadastrada ')
        return
    
    passeio_turistico = PasseioTuristico(aquario, escola, data)
    if passeio_turistico not in passeios_turisticos: passeios_turisticos.append(passeio_turistico) 
    else:print('Passeio ja tem cadastro ---' +str(passeios_turisticos))

def selecionar_passeios_turisticos(data_minima_passeio=None, peso_minimo_animal=None,
                                   max_alunos_escola=None, cidade_aquario=None):
    filtros = '\nFiltros -- '
    if data_minima_passeio: filtros += 'data minima_passeio: '+str(data_minima_passeio)
    if peso_minimo_animal: filtros += f' - peso minimo do animal: '+str(peso_minimo_animal)
    if max_alunos_escola: filtros += f' - máximo de alunos na escola: '+str(max_alunos_escola)
    if cidade_aquario: filtros += f' - cidade do aquário: '+str(cidade_aquario)

    selecionados = []
    for passeio_turistico in passeios_turisticos:
        if data_minima_passeio and passeio_turistico.data < data_minima_passeio:
            continue
        for animal_aquatico in passeio_turistico.aquario.animais_aquaticos.values():
            if peso_minimo_animal is not None and animal_aquatico.peso < peso_minimo_animal:
                excluir_passeio_turistico = True
                break
        if max_alunos_escola and passeio_turistico.escola.n_alunos > max_alunos_escola:
            continue
        if cidade_aquario and passeio_turistico.aquario.cidade != cidade_aquario:
            continue
        selecionados.append(passeio_turistico)
    return filtros, selecionados

class PasseioTuristico:
    def __init__(self, aquario, escola, data):
        self.aquario = aquario
        self.escola = escola
        self.data = data

    def __str__(self):
        formato = '{} {:<20} {} {:<19} {} {:<10} {}'
        return formato.format('|', self.aquario.nome, '|', self.escola.nome, '|', str(self.data), '|')

    def str_atributos_animais_aquaticos(self):
        atributos_animais_aquaticos_str=''
        for indice, animal_aquatico in enumerate(self.aquario.animais_aquaticos.values()):
            if(indice>0): atributos_animais_aquaticos_str+='-'
            atributos_animais_aquaticos_str+= f'{animal_aquatico.peso:.2f}'+' kg'
            return atributos_animais_aquaticos_str

    def str_filtro(self):
        formato = '{:>5} {} {:<14} {} {:<5} {}'
        filtro_formatado = formato.format(str(self.escola.n_alunos), '|', self.aquario.cidade, '|', self.str_atributos_animais_aquaticos(), '|')
        return self.__str__() + filtro_formatado