from src.util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from src.util.data import Data
from src.entidades.escola import inserir_escola, Escola, get_escolas
from src.entidades.animal_aquatico import AnimalAquatico, Tubarao, Baleia
from src.entidades.aquario import inserir_aquario, Aquario, get_aquarios
from src.entidades.passeio_turistico import criar_passeio_turistico, get_passeios_turisticos, selecionar_passeios_turisticos

def cadastrar_escolas():
    inserir_escola(Escola('12.345.678/0001-01', 'Colégio Alpha', 1200, True))
    inserir_escola(Escola('23.456.789/0001-02', 'Escola Horizonte', 2000, False))
    inserir_escola(Escola('45.678.901/0001-04', 'Colégio Excelência', 950, False))
    inserir_escola(Escola('56.789.012/0001-05', 'Escola Pioneira', 2000, True))
    inserir_escola(Escola('67.890.123/0001-06', 'Centro Aurora', 600, False))
    inserir_escola(Escola('78.901.234/0001-07', 'Escola Nova Geração', 2500, True))
    inserir_escola(Escola('90.123.456/0001-09', 'Escola do Futuro', 3000, True))
    inserir_escola(Escola('01.234.567/0001-10', 'Instituto Liberdade', 400, False))
    inserir_escola(Escola('11.111.111/0001-11', 'Escola Monte Azul', 1500, True))
    inserir_escola(Escola('22.222.222/0001-22', 'Colégio Planalto', 1000, False))
    inserir_escola(Escola('33.333.333/0001-33', 'Escola Vida Verde', 1800, True))


def cadastrar_aquarios():
    aquario = Aquario('Aquário Atlântico', 'Fortaleza - CE', 1100)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Tubarao('Tubarão Cabeça-Chata', 'oceano', 250, True, 'serrilhado', True))
    aquario.inserir_animais_aquaticos(Baleia('Baleia Jubarte', 'oceano', 29000, True, 'herbivoro', 150))

    aquario = Aquario('Recife Marinho', 'Recife - PE', 1000)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Tubarao('Tubarão Azul', 'oceano', 260, False, 'serrilhado', True))

    aquario = Aquario('Mar de Coral', 'Natal - RN', 950)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Tubarao('Tubarão Enxada', 'oceano', 210, True, 'serrilhado', True))

    aquario = Aquario('Aqua Mundo', 'Guarujá - SP', 1000)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Tubarao('Tubarão Branco', 'oceano', 1100, False, 'serrilhado', True))
    aquario.inserir_animais_aquaticos(Baleia('Baleia Azul', 'oceano', 30000, True, 'herbivoro', 160))

    aquario = Aquario('Oceanário de Recife', 'Recife - PE', 800)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Tubarao('Tubarão Tigre', 'água doce', 220, False, 'serrilhado', True))

    aquario = Aquario('Aquário de Ubatuba', 'Ubatuba - SP', 700)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Tubarao('Tubarão Martelo', 'oceano', 180, True, 'liso', False))

    aquario = Aquario('Projeto Tamar', 'Salvador - BA', 900)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Baleia('Baleia Orca', 'oceano', 27000, False, 'carnivoro', 140))
    aquario.inserir_animais_aquaticos(Tubarao('Tubarão de Galha', 'oceano', 220, True, 'liso', False))

    aquario = Aquario('Aquário de Bonito', 'Recife - PE', 600)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Tubarao('Tubarão Lixa', 'água doce', 200, True, 'serrilhado', True))

    aquario = Aquario('Sea Life', 'Recife - PE', 1200)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Baleia('Baleia Minke', 'oceano', 28000, True, 'herbivoro', 110))
    aquario.inserir_animais_aquaticos(Baleia('Baleia Fin', 'água doce', 31000, True, 'carnivoro', 180))

    aquario = Aquario('Mundo Submarino', 'Recife - PE', 1500)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Tubarao('Tubarão Azul', 'oceano', 260, False, 'liso', True))

    aquario = Aquario('Aquário Amazônico', 'Recife - PE', 1300)
    inserir_aquario(aquario)
    aquario.inserir_animais_aquaticos(Baleia('Baleia Cinzenta', 'água doce', 32000, True, 'herbivoro', 200))
    aquario.inserir_animais_aquaticos(Baleia('Baleia Narval', 'oceano', 29000, False, 'carnivoro', 85))

def cadastrar_passeios_turisticos():
    criar_passeio_turistico('Aquário Atlântico', '11.111.111/0001-11', Data(12, 6, 2020))
    criar_passeio_turistico('Recife Marinho', '22.222.222/0001-22', Data(10, 7, 2021))
    criar_passeio_turistico('Mar de Coral', '33.333.333/0001-33', Data(25, 8, 2022))

    criar_passeio_turistico('Aqua Mundo', '12.345.678/0001-01', Data(10, 5, 2014))

    criar_passeio_turistico('Aquário de Bonito', '23.456.789/0001-02', Data(12, 5, 2011))

    criar_passeio_turistico('Sea Life', '67.890.123/0001-06', Data(7, 6, 2022))

    criar_passeio_turistico('Projeto Tamar', '90.123.456/0001-09', Data(5, 6, 2015))

    criar_passeio_turistico('Mundo Submarino', '01.234.567/0001-10', Data(30, 5, 2012))

    criar_passeio_turistico('Aquário de Ubatuba', '45.678.901/0001-04', Data(8, 7, 2019))

    criar_passeio_turistico('Oceanário de Aracaju', '78.901.234/0001-07', Data(14, 8, 2020))

    criar_passeio_turistico('Aquário Amazônico', '56.789.012/0001-05', Data(15, 11, 2017))


def imprimir_somente_para_alinhar_formatação():
 print('\nAquários : nome - cidade - capacidade')
 for indice, aquario in enumerate(get_aquarios().values()): print(aquario)
 print('\nAnimais Aquáticos dos Aquários:')
 for aquario in get_aquarios().values():
  for animal in aquario.animais_aquaticos.values(): print(animal)


if __name__ == '__main__':
    cadastrar_escolas()
    imprimir_objetos('\nEscolas : nome - CNPJ - número de alunos - possui programa ambiental', get_escolas().values())

    cadastrar_aquarios()
    imprimir_somente_para_alinhar_formatação()

    print('\nAquários : nome - cidade - capacidade')
    print(' - Animais Aquáticos : nome - habitat - peso - tubarao[tipo de dente - é selvagem] | baleia:[alimentação, idade] - risco de extinção')
    for indice, aquario in enumerate(get_aquarios().values()):
        imprimir_objeto(indice=indice, objeto_str=str(aquario))
        imprimir_objetos_internos(aquario.animais_aquaticos.values())
    cadastrar_passeios_turisticos()
    cabeçalho = 'Passeios Turísticos : nome do aquário - nome da escola - data do passeio'
    imprimir_objetos('\n' + cabeçalho, get_passeios_turisticos())

    cabeçalho_filtros = cabeçalho + '\n -- número de alunos da escola - peso do animal aquático - cidade do aquário '

    filtros, selecionados = selecionar_passeios_turisticos()
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)

    filtros, selecionados = selecionar_passeios_turisticos(data_minima_passeio=Data(1, 1, 2012))
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)

    filtros, selecionados = selecionar_passeios_turisticos(Data(1, 1, 2012), peso_minimo_animal=210)
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)

    filtros, selecionados = selecionar_passeios_turisticos(Data(1, 1, 2012), 210, max_alunos_escola=2900)
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)

    filtros, selecionados = selecionar_passeios_turisticos(Data(1, 1, 2012), 210, 2900, cidade_aquario='Recife - PE')
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)

    filtros, selecionados = selecionar_passeios_turisticos(Data(1, 1, 2012), 210, 2900, 'Recife - PE', 'liso')
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)
    
    filtros, selecionados = selecionar_passeios_turisticos(Data(1, 1, 2012), 210, 2900, 'Recife - PE', 'liso', 100)
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)