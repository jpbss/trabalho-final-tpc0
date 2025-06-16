import datetime
from modelo.cliente import Cliente
from modelo.veiculo import Veiculo


class Venda:
    def __init__(self):
        self.__idvenda = 0
        self.__data = datetime.date.today().strftime('%Y-%m-%d')
        self.__valor_vendido = 0.0
        self.__forma_pagamento = ''

        self.__cliente = Cliente()
        self.__veiculo = Veiculo()

        self.__lista = 'data, valor_vendido, idcliente, idplaca, forma_pagamento'
        self.__tabelaBanco = 'venda'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return f"'{self.data}', {self.valor_vendido}, {self.cliente.idcliente}, '{self.veiculo.idplaca}', '{self.forma_pagamento}'"

    @property
    def dadosUpdate(self):
        return (f"data='{self.data}', valor_vendido={self.valor_vendido}, idcliente={self.cliente.idcliente}, "
                f"idplaca='{self.veiculo.idplaca}', forma_pagamento='{self.forma_pagamento}' where idvenda={self.idvenda}")

    @property
    def dadosDelete(self):
        return f"where idvenda={self.idvenda}"

    @property
    def dadosPesquisa(self):
        return f"select * from {self.tabelaBanco} where idvenda = {self.idvenda}"

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idvenda(self):
        return self.__idvenda

    @idvenda.setter
    def idvenda(self, entrada):
        self.__idvenda = entrada

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, entrada):
        self.__data = entrada

    @property
    def valor_vendido(self):
        return self.__valor_vendido

    @valor_vendido.setter
    def valor_vendido(self, entrada):
        self.__valor_vendido = entrada

    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, entrada):
        self.__forma_pagamento = entrada

    # --- Getters e Setters para os objetos relacionados ---

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, entrada):
        if isinstance(entrada, Cliente):
            self.__cliente = entrada
            self.__idcliente = entrada.idcliente
        else:
            print("O objeto fornecido não é da classe Cliente")

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, entrada):
        if isinstance(entrada, Veiculo):
            self.__veiculo = entrada
            self.__idplaca = entrada.idplaca
        else:
            print("O objeto fornecido não é da classe Veiculo")

    def __repr__(self):
        return (f"Venda ID: {self.idvenda} | Data: {self.data} | Valor: R$ {self.valor_vendido:.2f}\n"
                f"  -> Cliente: {self.cliente.nome}\n"
                f"  -> Veículo: {self.veiculo.idplaca}")