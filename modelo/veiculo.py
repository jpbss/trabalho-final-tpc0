class Veiculo:
    def __init__(self):
        self.__idplaca = ''
        self.__ano = 0
        self.__modelo = 0
        self.__preco_fipe = 0.0
        self.__fabricante = ''
        self.__modelo_veiculo = ''
        self.__cor = ''
        self.__preco_venda = 0.0
        self.__total_despesa = 0.0

        self.__lista = 'idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda, total_despesa'
        self.__tabelaBanco = 'veiculo'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return f"'{self.idplaca}', {self.ano}, {self.modelo}, {self.preco_fipe}, '{self.fabricante}', '{self.modelo_veiculo}', '{self.cor}', {self.preco_venda}, {self.total_despesa}"

    @property
    def dadosUpdate(self):
        return f"ano={self.ano}, modelo={self.modelo}, preco_fipe={self.preco_fipe}, fabricante='{self.fabricante}', modelo_veiculo='{self.modelo_veiculo}', cor='{self.cor}', preco_venda={self.preco_venda}, total_despesa={self.total_despesa} where idplaca='{self.idplaca}'"

    @property
    def dadosDelete(self):
        return f"where idplaca='{self.idplaca}'"

    @property
    def dadosPesquisa(self):
        return f"select * from {self.tabelaBanco} where idplaca = '{self.idplaca}'"

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idplaca(self):
        return self.__idplaca

    @idplaca.setter
    def idplaca(self, entrada):
        self.__idplaca = entrada

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, entrada):
        self.__ano = entrada

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, entrada):
        self.__modelo = entrada

    @property
    def preco_fipe(self):
        return self.__preco_fipe

    @preco_fipe.setter
    def preco_fipe(self, entrada):
        self.__preco_fipe = entrada

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, entrada):
        self.__fabricante = entrada

    @property
    def modelo_veiculo(self):
        return self.__modelo_veiculo

    @modelo_veiculo.setter
    def modelo_veiculo(self, entrada):
        self.__modelo_veiculo = entrada

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, entrada):
        self.__cor = entrada

    @property
    def preco_venda(self):
        return self.__preco_venda

    @preco_venda.setter
    def preco_venda(self, entrada):
        self.__preco_venda = entrada

    @property
    def total_despesa(self):
        return self.__total_despesa

    @total_despesa.setter
    def total_despesa(self, entrada):
        self.__total_despesa = entrada

    def __repr__(self):
        return f"Placa: {self.idplaca} - Modelo: {self.fabricante} {self.modelo_veiculo} {self.ano}"