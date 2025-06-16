import datetime
from modelo.veiculo import Veiculo
from modelo.prestador import Prestador


class Despesa:
    def __init__(self):
        self.__iddespesa = 0
        self.__descricao = ''
        self.__valor = 0.0
        self.__data_servico = datetime.date.today().strftime('%Y-%m-%d')

        self.__veiculo = Veiculo()
        self.__prestador = Prestador()

        self.__lista = 'idplaca, idprestador, descricao, valor, data_servico'
        self.__tabelaBanco = 'despesa'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return f"'{self.veiculo.idplaca}', {self.prestador.idprestador}, '{self.descricao}', {self.valor}, '{self.data_servico}'"

    @property
    def dadosUpdate(self):
        return f"idplaca='{self.veiculo.idplaca}', idprestador={self.prestador.idprestador}, descricao='{self.descricao}', valor={self.valor}, data_servico='{self.data_servico}' where iddespesa={self.iddespesa}"

    @property
    def dadosDelete(self):
        return f"where iddespesa={self.iddespesa}"

    @property
    def dadosPesquisa(self):
        return f"select * from {self.tabelaBanco} where iddespesa = {self.iddespesa}"

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def iddespesa(self):
        return self.__iddespesa

    @iddespesa.setter
    def iddespesa(self, entrada):
        self.__iddespesa = entrada

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, entrada):
        self.__descricao = entrada

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, entrada):
        self.__valor = entrada

    @property
    def data_servico(self):
        return self.__data_servico

    @data_servico.setter
    def data_servico(self, entrada):
        self.__data_servico = entrada

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, entrada):
        if isinstance(entrada, Veiculo):
            self.__veiculo = entrada
        else:
            print("O objeto não é da classe Veiculo")

    @property
    def prestador(self):
        return self.__prestador

    @prestador.setter
    def prestador(self, entrada):
        if isinstance(entrada, Prestador):
            self.__prestador = entrada
        else:
            print("O objeto não é da classe Prestador")

    def __repr__(self):
        return f"Despesa ID: {self.iddespesa} - Descrição: {self.descricao} - Valor: {self.valor}"