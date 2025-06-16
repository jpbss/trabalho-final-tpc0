import datetime
from modelo.cliente import Cliente
from modelo.veiculo import Veiculo


class Compra:
    def __init__(self):
        self.__idcompra = 0
        self.__data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__valor_pago = 0.0
        self.__forma_pagamento = ''

        self.__cliente = Cliente()
        self.__veiculo = Veiculo()

        self.__lista = 'idplaca, idcliente, data, valor_pago, forma_pagamento'
        self.__tabelaBanco = 'compra'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return f"'{self.veiculo.idplaca}', {self.cliente.idcliente}, '{self.data}', {self.valor_pago}, '{self.forma_pagamento}'"

    @property
    def dadosUpdate(self):
        return f"idplaca='{self.veiculo.idplaca}', idcliente={self.cliente.idcliente}, data='{self.data}', valor_pago={self.valor_pago}, forma_pagamento='{self.forma_pagamento}' where idcompra={self.idcompra}"

    @property
    def dadosDelete(self):
        return f"where idcompra={self.idcompra}"

    @property
    def dadosPesquisa(self):
        return f"select * from {self.tabelaBanco} where idcompra = {self.idcompra}"

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idcompra(self):
        return self.__idcompra

    @idcompra.setter
    def idcompra(self, entrada):
        self.__idcompra = entrada

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, entrada):
        self.__data = entrada

    @property
    def valor_pago(self):
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, entrada):
        self.__valor_pago = entrada

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, entrada):
        self.__forma_pagamento = entrada

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, entrada):
        if isinstance(entrada, Cliente):
            self.__cliente = entrada
        else:
            print("O objeto não é da classe Cliente")

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, entrada):
        if isinstance(entrada, Veiculo):
            self.__veiculo = entrada
        else:
            print("O objeto não é da classe Veiculo")

    def __repr__(self):
        return f"Compra ID: {self.idcompra} - Data: {self.data} - Valor: {self.valor_pago}"