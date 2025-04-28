from datetime import date

class Data:
    def __init__(self, dia, mês, ano):
        self.dia = dia
        self.mês = mês
        self.ano = ano

    def __str__(self):
        if self.dia < 10:
            data_str = '0' + str(self.dia)
        else:
            data_str = str(self.dia)

        if self.mês < 10:
            data_str += "/0" + str(self.mês) + "/"
        else:
            data_str += "/" + str(self.mês) + "/"

        data_str += str(self.ano)
        return data_str

    def __eq__(self, data):
        if self.dia == data.dia and self.mês == data.mês and self.ano == data.ano:
            return True
        return False

    def __ne__(self, data):
        return not self == data

    def __gt__(self, data):
        if self.ano > data.ano:
            return True
        elif self.ano < data.ano:
            return False

        if self.mês > data.mês:
            return True
        elif self.mês < data.mês:
            return False

        if self.dia > data.dia:
            return True
        elif self.dia < data.dia:
            return False

        return False
