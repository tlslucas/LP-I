escolas = []

def get_escolas() : return escolas

def inserir_escola(escola): escolas.append(escola)


class Escola:
    def __init__(self, cnpj, nome, alunos_matriculados, publica=False):
        self.cnpj = cnpj
        self.alunos_matriculados = alunos_matriculados
        self.publica = publica
        self.nome = nome




    def __str__(self):
        if self.publica: publica_str = 'publica |'
        else: publica_str = ''
        formato = '{} {:<8} {} {:<20} {} {:4} {} {}'
        escola_formatado = formato.format('|', self.cnpj, '|', self.nome, '|', self.alunos_matriculados, '|', publica_str)
        return escola_formatado



def selecionar_escola(prefixo_nome = None, alunos_matriculados_minimo = None, publica = None):
    filtros = '\nFiltros: '
    if prefixo_nome is not None: filtros += 'prefixo_nome: ' + prefixo_nome
    if alunos_matriculados_minimo is not None: filtros += ' - alunos_matriculados_minimo: '  + str(alunos_matriculados_minimo)
    if publica: filtros += ' publica: true '
    elif publica == False: filtros += ' publica: false'

    escolas_selecionadas = []

    for escola in escolas:
        if prefixo_nome is not None and not escola.nome.startswith(prefixo_nome): continue

        if alunos_matriculados_minimo is not None and escola.alunos_matriculados < alunos_matriculados_minimo:
            continue
        if publica in (True, False) and escola.publica != publica:
            continue
        escolas_selecionadas.append(escola)

    return filtros, escolas_selecionadas