class AnimalAquatico:
    def __init__(self, nome, habitat, peso, risco_extincao):
        self.nome = nome
        self.habitat = habitat if habitat in ('oceano', 'água doce', 'mar fechado') else 'indefinido'
        self.peso = peso
        self.risco_extincao = risco_extincao


class Tubarao(AnimalAquatico):
    def __init__(self, nome, habitat, peso, risco_extincao, tipo_dente, selvagem):
        super().__init__(nome, habitat, peso, risco_extincao)
        self.tipo_dente = tipo_dente if tipo_dente in ('serrilhado', 'liso') else 'indefinido'
        self.selvagem = selvagem

    def __str__(self):
        if self.risco_extincao: risco_extincao_str = 'em risco |'
        else: risco_extincao_str=''
        if self.selvagem: selvagem_str = 'selvagem |'
        else: selvagem_str='cativeiro |'
        formato = '{} {:<17} {} {:<11} {} {:<8} {} {:<10} {} {} {}'
        tubarao_formatado = formato.format('|', self.nome, '|', self.habitat, '|', str(self.peso) + ' kg', '|',self.tipo_dente, '|',selvagem_str, risco_extincao_str)
        return tubarao_formatado

class Baleia(AnimalAquatico):

    def __init__(self, nome, habitat, peso, risco_extincao, alimentacao, idade):
        super().__init__(nome, habitat, peso, risco_extincao)
        self.alimentacao = alimentacao if alimentacao in ('carnivoro', 'herbivoro') else 'indefinido'
        self.idade = idade

    def __str__(self):
        if self.risco_extincao: risco_extincao_str = 'em risco |'
        else: risco_extincao_str=''
        formato = '{} {:<17} {} {:<11} {} {:<8} {} {:<10} {} {:<7} {} {:<7}'
        baleia_formatado = formato.format('|', self.nome, '|', self.habitat, '|', str(self.peso) + ' kg', '|',self.alimentacao, '|',f'{self.idade:d}' + ' anos', '|', risco_extincao_str)
        return baleia_formatado