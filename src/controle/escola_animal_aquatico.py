from src.util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from src.util.data import Data
from src.entidades.escola import inserir_escola, Escola, get_escolas
from src.entidades.animal_aquatico import inserir_animal_aquatico, AnimalAquatico, get_animais_aquaticos
from src.entidades.aquario import inserir_aquario, Aquario, get_aquarios
from src.entidades.passeio_turistico import criar_passeio_turistico, get_passeios_turisticos, selecionar_passeios_turisticos

def cadastrar_escolas():
    inserir_escola(Escola('12.345.678/0001-01', 'Colégio Alpha', 1200, True))
    inserir_escola(Escola('23.456.789/0001-02', 'Escola Horizonte', 2000, False))
    inserir_escola(Escola('34.567.890/0001-03', 'Instituto Saber', 2000, True))
    inserir_escola(Escola('45.678.901/0001-04', 'Colégio Excelência', 950, False))
    inserir_escola(Escola('56.789.012/0001-05', 'Escola Pioneira', 1800, True))
    inserir_escola(Escola('67.890.123/0001-06', 'Centro Aurora', 600, False))
    inserir_escola(Escola('78.901.234/0001-07', 'Escola Nova Geração', 2500, True))
    inserir_escola(Escola('89.012.345/0001-08', 'Colégio Nexus', 1300, False))
    inserir_escola(Escola('90.123.456/0001-09', 'Escola do Futuro', 3000, True))
    inserir_escola(Escola('01.234.567/0001-10', 'Instituto Liberdade', 400, False))

def cadastrar_animais_aquaticos():
    inserir_animal_aquatico(AnimalAquatico('Beta', 'oceano', 19, True))
    inserir_animal_aquatico(AnimalAquatico('Tubarão', 'oceano', 250, False))
    inserir_animal_aquatico(AnimalAquatico('Dory', 'mar fechado', 200, False))
    inserir_animal_aquatico(AnimalAquatico('Nemo', 'mar fechado', 1, False))
    inserir_animal_aquatico(AnimalAquatico('Golfinho', 'oceano', 150, True))
    inserir_animal_aquatico(AnimalAquatico('Pirarucu', 'água doce', 220, True))
    inserir_animal_aquatico(AnimalAquatico('Estrela do Mar', 'mar fechado', 0.5, False))
    inserir_animal_aquatico(AnimalAquatico('Cavalo-marinho', 'oceano', 0.3, True))
    inserir_animal_aquatico(AnimalAquatico('Tartaruga Marinha', 'oceano', 200, True))
    inserir_animal_aquatico(AnimalAquatico('Peixe-boi', 'água doce', 500, True))

def cadastrar_aquarios():
    aquario = Aquario('Aqua Mundo', 'Guarujá - SP', 1000)
    inserir_aquario(aquario)
    aquario.inserir_animal_aquatico(AnimalAquatico('Tubarão', 'oceano', 250, False))

    aquario = Aquario('Oceanário de Aracaju', 'Aracaju - SE', 800)
    inserir_aquario(aquario)
    aquario.inserir_animal_aquatico(AnimalAquatico('Golfinho', 'oceano', 150, True))

    aquario = Aquario('Aquário de Ubatuba', 'Ubatuba - SP', 700)
    inserir_aquario(aquario)
    aquario.inserir_animal_aquatico(AnimalAquatico('Pirarucu', 'água doce', 220, True))

    aquario = Aquario('Projeto Tamar', 'Salvador - BA', 900)
    inserir_aquario(aquario)
    aquario.inserir_animal_aquatico(AnimalAquatico('Tartaruga Marinha', 'oceano', 200, True))

    aquario = Aquario('Aquário de Bonito', 'Recife - PE', 600)
    inserir_aquario(aquario)
    aquario.inserir_animal_aquatico(AnimalAquatico('Dory', 'mar fechado', 200, False))

    aquario = Aquario('Sea Life', 'São Paulo - SP', 1200)
    inserir_aquario(aquario)
    aquario.inserir_animal_aquatico(AnimalAquatico('Estrela do Mar', 'mar fechado', 0.5, False))

    aquario = Aquario('Mundo Submarino', 'Recife - PE', 1500)
    inserir_aquario(aquario)
    aquario.inserir_animal_aquatico(AnimalAquatico('Cavalo-marinho', 'oceano', 0.3, True))

    aquario = Aquario('Aquário Amazônico', 'Manaus - AM', 1300)
    inserir_aquario(aquario)
    aquario.inserir_animal_aquatico(AnimalAquatico('Peixe-boi', 'água doce', 500, True))

def cadastrar_passeios_turisticos():
    criar_passeio_turistico('Aqua Mundo', 'Tubarão', 'Colégio Alpha', Data(10, 5, 2014))
    criar_passeio_turistico('Aquário de Bonito', 'Dory', 'Escola Horizonte', Data(12, 5, 2012))
    criar_passeio_turistico('Sea Life', 'Estrela do Mar', 'Centro Aurora', Data(7, 6, 2022))
    criar_passeio_turistico('Projeto Tamar', 'Tartaruga Marinha', 'Escola do Futuro', Data(5, 6, 2015))
    criar_passeio_turistico('Mundo Submarino', 'Cavalo-marinho', 'Instituto Liberdade', Data(30, 5, 2011))

def imprimir_somente_para_alinhar_formatação():
 print('\nAquários : nome - cidade - capacidade')
 for índice, aquario in enumerate(get_aquarios().values()): print(aquario)
 print('\nAnimais Aquáticos dos Aquários:')
 for aquario in get_aquarios().values():
  for animal in aquario.animal_aquatico.values(): print(animal)


if __name__ == '__main__':
    cadastrar_escolas()
    imprimir_objetos('\nEscolas : nome - CNPJ - número de alunos - possui programa ambiental', get_escolas().values())

    cadastrar_aquarios()
    imprimir_somente_para_alinhar_formatação()

    print('\nAquários : nome - cidade - capacidade')
    print(' - Animais Aquáticos : nome - habitat - peso - risco de extinção')
    for índice, aquario in enumerate(get_aquarios().values()):
        imprimir_objeto(índice, str(aquario))
        imprimir_objetos_internos(aquario.animal_aquatico.values())

    cadastrar_passeios_turisticos()
    cabeçalho = 'Passeios Turísticos : nome do aquário - nome do animal aquático - nome da escola - data do passeio'
    imprimir_objetos('\n' + cabeçalho, get_passeios_turisticos())

    cabeçalho_filtros = cabeçalho + '\n -- número de alunos da escola - cidade do aquário - peso do animal aquático'

    filtros, selecionados = selecionar_passeios_turisticos()
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)

    filtros, selecionados = selecionar_passeios_turisticos(data_minima_passeio=Data(1, 1, 2012))
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)

    filtros, selecionados = selecionar_passeios_turisticos(Data(1, 1, 2012), peso_minimo_animal=150)
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)

    filtros, selecionados = selecionar_passeios_turisticos(Data(1, 1, 2012), 150, max_alunos_escola=2000)
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)

    filtros, selecionados = selecionar_passeios_turisticos(Data(1, 1, 2012), 150, 2000, cidade_aquario='Recife - PE')
    imprimir_objetos_associação_filtros(cabeçalho_filtros, selecionados, filtros)
