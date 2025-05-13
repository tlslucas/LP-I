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

class Escola:
    def __init__(self, cnpj, nome, n_alunos, programa_ambiental):
        self.cnpj = cnpj
        self.nome = nome
        self.n_alunos = n_alunos
        self.programa_ambiental = programa_ambiental

    def __str__(self):
        ambiental = 'Programa Ambiental'' |' if self.programa_ambiental else ' '
        formato = '{} {:<19} {} {:<18} {} {:<5} {} {:<3}'
        return formato.format('|', self.nome, '|', self.cnpj, '|', self.n_alunos, '|', ambiental)
