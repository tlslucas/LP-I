escolas = {}

def get_escolas():
    return escolas

def inserir_escola(escola):
    cnpj = escola.cnpj
    if cnpj not in escolas:
        escolas[cnpj] = escola
        return True
    else:
        print('Escola com CNPJ ' + cnpj + ' já está cadastrada')
        return False

def selecionar_escola(max_alunos=None, possui_programa_ambiental=None, prefixo_nome=None):
    filtros = '\nFiltros -- '
    if max_alunos is not None: filtros += 'máximo de alunos: ' + str(max_alunos)
    if possui_programa_ambiental in (True, False): filtros += ' - possui programa ambiental: ' + str(possui_programa_ambiental)
    if prefixo_nome is not None: filtros += ' - prefixo do nome: ' + prefixo_nome

    selecionadas = []
    for escola in escolas.values():
        if max_alunos is not None and escola.n_alunos > max_alunos:
            continue
        if possui_programa_ambiental in (True, False) and escola.programa_ambiental != possui_programa_ambiental:
            continue
        if prefixo_nome and not escola.nome.startswith(prefixo_nome):
            continue
        selecionadas.append(escola)
    return filtros, selecionadas

class Escola:
    def __init__(self, cnpj, nome, n_alunos, programa_ambiental):
        self.cnpj = cnpj
        self.nome = nome
        self.n_alunos = n_alunos
        self.programa_ambiental = programa_ambiental

    def __str__(self):
        ambiental = 'sim' if self.programa_ambiental else 'não'
        formato = '{} {:<22} {} {:<18} {} {:<5} {} {:<3} {}'
        return formato.format('|', self.nome, '|', self.cnpj, '|', self.n_alunos, '|', ambiental, '|')
