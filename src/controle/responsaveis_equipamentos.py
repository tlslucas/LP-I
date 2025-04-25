from src.entidades.animalaquatico import (inserir_animalaquatico, Animalaquatico, get_animaisaquaticos, selecionar_animalaquatico)
from src.entidades.escola import (inserir_escola, Escola, get_escolas, selecionar_escola)

from src.util.gerais import imprimir_objetos


def cadastrar_animalaquatico():
    inserir_animalaquatico(Animalaquatico(nome='Beta', habitat='oceano', peso=19, riscoextincao=True))
    inserir_animalaquatico(Animalaquatico(nome='Tubarão', habitat='oceano', peso=250, riscoextincao=False))
    inserir_animalaquatico(Animalaquatico(nome='Dory', habitat='mar fechado', peso=2, riscoextincao=False))
    inserir_animalaquatico(Animalaquatico(nome='Nemo', habitat='mar fechado', peso=1, riscoextincao=False))
    inserir_animalaquatico(Animalaquatico(nome='Golfinho', habitat='oceano', peso=150, riscoextincao=True))
    inserir_animalaquatico(Animalaquatico(nome='Pirarucu', habitat='água doce', peso=220, riscoextincao=True))
    inserir_animalaquatico(Animalaquatico(nome='Estrela do Mar', habitat='mar fechado', peso=0.5, riscoextincao=False))
    inserir_animalaquatico(Animalaquatico(nome='Cavalo-marinho', habitat='oceano', peso=0.3, riscoextincao=True))
    inserir_animalaquatico(Animalaquatico(nome='Tartaruga Marinha', habitat='oceano', peso=200, riscoextincao=True))
    inserir_animalaquatico(Animalaquatico(nome='Peixe-boi', habitat='água doce', peso=500, riscoextincao=True))


if __name__ == '__main__':

    cadastrar_animalaquatico()
    cabeçalho ='      Nome         Hbitat    Peso         Risco de Extincao'
    imprimir_objetos("\nResponsaveis cadastrados",get_animaisaquaticos())

    filtros, animaisaquaticos_selecionados = selecionar_animalaquatico()

    imprimir_objetos(cabeçalho, animaisaquaticos_selecionados, filtros)
    filtros, animaisaquaticos_selecionados = selecionar_animalaquatico(habitat='oceano')

    imprimir_objetos(cabeçalho, animaisaquaticos_selecionados, filtros)
    filtros, animaisaquaticos_selecionados = selecionar_animalaquatico('oceano',peso_minimo=20)

    imprimir_objetos(cabeçalho, animaisaquaticos_selecionados, filtros)
    filtros, animaisaquaticos_selecionados = selecionar_animalaquatico('oceano',20, riscoextincao=True)

    imprimir_objetos(cabeçalho, animaisaquaticos_selecionados, filtros)


def cadastrar_escola():
    inserir_escola(Escola('12.345.678/0001-01', 'Colégio Alpha', 1200, True))
    inserir_escola(Escola('23.456.789/0001-02', 'Escola Horizonte', 850, False))
    inserir_escola(Escola('34.567.890/0001-03', 'Instituto Saber', 2000, True))
    inserir_escola(Escola('45.678.901/0001-04', 'Colégio Excelência', 950, False))
    inserir_escola(Escola('56.789.012/0001-05', 'Escola Pioneira', 1800, True))
    inserir_escola(Escola('67.890.123/0001-06', 'Centro Aurora', 600, False))
    inserir_escola(Escola('78.901.234/0001-07', 'Escola No va Geração', 2500, True))
    inserir_escola(Escola('89.012.345/0001-08', 'Colégio Nexus', 1300, False))
    inserir_escola(Escola('90.123.456/0001-09', 'Escola do Futuro', 3000, True))
    inserir_escola(Escola('01.234.567/0001-10', 'Instituto Liberdade', 400, False))


if __name__ == '__main__':

    cadastrar_escola()
    cabeçalho ='      CNPJ     Nome         Alunos Matriculados    Publica'
    imprimir_objetos("\nEscolas cadastrados", get_escolas())

    filtros, escolas_selecionadas = selecionar_escola()

    imprimir_objetos(cabeçalho, escolas_selecionadas, filtros)
    filtros, escolas_selecionadas = selecionar_escola(publica=True)

    imprimir_objetos(cabeçalho, escolas_selecionadas, filtros)
    filtros, escolas_selecionadas = selecionar_escola(publica=True, alunos_matriculados_minimo= 1500)

    imprimir_objetos(cabeçalho, escolas_selecionadas, filtros)
    filtros, escolas_selecionadas = selecionar_escola(publica=True, alunos_matriculados_minimo= 1500,prefixo_nome= "Instituto" )

    imprimir_objetos(cabeçalho, escolas_selecionadas, filtros)
from src.entidades.animalaquatico import (inserir_animalaquatico, Animalaquatico, get_animaisaquaticos, selecionar_animalaquatico)
from src.entidades.escola import (inserir_escola, Escola, get_escolas, selecionar_escola)

from src.util.gerais import imprimir_objetos


def cadastrar_animalaquatico():
    inserir_animalaquatico(Animalaquatico(nome='Beta', habitat='oceano', peso=19, riscoextincao=True))
    inserir_animalaquatico(Animalaquatico(nome='Tubarão', habitat='oceano', peso=250, riscoextincao=False))
    inserir_animalaquatico(Animalaquatico(nome='Dory', habitat='mar fechado', peso=2, riscoextincao=False))
    inserir_animalaquatico(Animalaquatico(nome='Nemo', habitat='mar fechado', peso=1, riscoextincao=False))
    inserir_animalaquatico(Animalaquatico(nome='Golfinho', habitat='oceano', peso=150, riscoextincao=True))
    inserir_animalaquatico(Animalaquatico(nome='Pirarucu', habitat='água doce', peso=220, riscoextincao=True))
    inserir_animalaquatico(Animalaquatico(nome='Estrela do Mar', habitat='mar fechado', peso=0.5, riscoextincao=False))
    inserir_animalaquatico(Animalaquatico(nome='Cavalo-marinho', habitat='oceano', peso=0.3, riscoextincao=True))
    inserir_animalaquatico(Animalaquatico(nome='Tartaruga Marinha', habitat='oceano', peso=200, riscoextincao=True))
    inserir_animalaquatico(Animalaquatico(nome='Peixe-boi', habitat='água doce', peso=500, riscoextincao=True))


if __name__ == '__main__':

    cadastrar_animalaquatico()
    cabeçalho ='      Nome         Hbitat    Peso         Risco de Extincao'
    imprimir_objetos("\nResponsaveis cadastrados",get_animaisaquaticos())

    filtros, animaisaquaticos_selecionados = selecionar_animalaquatico()

    imprimir_objetos(cabeçalho, animaisaquaticos_selecionados, filtros)
    filtros, animaisaquaticos_selecionados = selecionar_animalaquatico(habitat='oceano')

    imprimir_objetos(cabeçalho, animaisaquaticos_selecionados, filtros)
    filtros, animaisaquaticos_selecionados = selecionar_animalaquatico('oceano',peso_minimo=20)

    imprimir_objetos(cabeçalho, animaisaquaticos_selecionados, filtros)
    filtros, animaisaquaticos_selecionados = selecionar_animalaquatico('oceano',20, riscoextincao=True)

    imprimir_objetos(cabeçalho, animaisaquaticos_selecionados, filtros)


def cadastrar_escola():
    inserir_escola(Escola('12.345.678/0001-01', 'Colégio Alpha', 1200, True))
    inserir_escola(Escola('23.456.789/0001-02', 'Escola Horizonte', 850, False))
    inserir_escola(Escola('34.567.890/0001-03', 'Instituto Saber', 2000, True))
    inserir_escola(Escola('45.678.901/0001-04', 'Colégio Excelência', 950, False))
    inserir_escola(Escola('56.789.012/0001-05', 'Escola Pioneira', 1800, True))
    inserir_escola(Escola('67.890.123/0001-06', 'Centro Aurora', 600, False))
    inserir_escola(Escola('78.901.234/0001-07', 'Escola No va Geração', 2500, True))
    inserir_escola(Escola('89.012.345/0001-08', 'Colégio Nexus', 1300, False))
    inserir_escola(Escola('90.123.456/0001-09', 'Escola do Futuro', 3000, True))
    inserir_escola(Escola('01.234.567/0001-10', 'Instituto Liberdade', 400, False))


if __name__ == '__main__':

    cadastrar_escola()
    cabeçalho ='      CNPJ     Nome         Alunos Matriculados    Publica'
    imprimir_objetos("\nEscolas cadastrados", get_escolas())

    filtros, escolas_selecionadas = selecionar_escola()

    imprimir_objetos(cabeçalho, escolas_selecionadas, filtros)
    filtros, escolas_selecionadas = selecionar_escola(publica=True)

    imprimir_objetos(cabeçalho, escolas_selecionadas, filtros)
    filtros, escolas_selecionadas = selecionar_escola(publica=True, alunos_matriculados_minimo= 1500)

    imprimir_objetos(cabeçalho, escolas_selecionadas, filtros)
    filtros, escolas_selecionadas = selecionar_escola(publica=True, alunos_matriculados_minimo= 1500,prefixo_nome= "Instituto" )

    imprimir_objetos(cabeçalho, escolas_selecionadas, filtros)



