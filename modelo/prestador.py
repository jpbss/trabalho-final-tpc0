class Prestador:
    def __init__(self):
        self.__idprestador = 0
        self.__nome_empresa = ''
        self.__cidade = ''
        self.__uf = ''
        self.__cep = ''

        self.__lista = 'nome_empresa, cidade, uf, cep'
        self.__tabelaBanco = 'prestador'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return f"'{self.nome_empresa}', '{self.cidade}', '{self.uf}', '{self.cep}'"

    @property
    def dadosUpdate(self):
        return f"nome_empresa='{self.nome_empresa}', cidade='{self.cidade}', uf='{self.uf}', cep='{self.cep}' where idprestador={self.idprestador}"

    @property
    def dadosDelete(self):
        return f"where idprestador={self.idprestador}"

    @property
    def dadosPesquisa(self):
        return f"select * from {self.tabelaBanco} where idprestador = {self.idprestador}"

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idprestador(self):
        return self.__idprestador

    @idprestador.setter
    def idprestador(self, entrada):
        self.__idprestador = entrada

    @property
    def nome_empresa(self):
        return self.__nome_empresa

    @nome_empresa.setter
    def nome_empresa(self, entrada):
        self.__nome_empresa = entrada

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, entrada):
        self.__cidade = entrada

    @property
    def uf(self):
        return self.__uf

    @uf.setter
    def uf(self, entrada):
        self.__uf = entrada

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, entrada):
        self.__cep = entrada

    def __repr__(self):
        return f"ID: {self.idprestador} - Empresa: {self.nome_empresa}"