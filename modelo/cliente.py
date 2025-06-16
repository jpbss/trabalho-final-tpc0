class Cliente:
    def __init__(self):
        self.__idcliente = 0
        self.__nome = ''
        self.__endereco = ''
        self.__cidade = ''
        self.__uf = ''
        self.__cep = ''

        self.__lista = 'nome, endereco, cidade, uf, cep'
        self.__tabelaBanco = 'cliente'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        return f"'{self.nome}', '{self.endereco}', '{self.cidade}', '{self.uf}', '{self.cep}'"

    @property
    def dadosUpdate(self):
        return f"nome='{self.nome}', endereco='{self.endereco}', cidade='{self.cidade}', uf='{self.uf}', cep='{self.cep}' where idcliente={self.idcliente}"

    @property
    def dadosDelete(self):
        return f"where idcliente={self.idcliente}"

    @property
    def dadosPesquisa(self):
        return f"select * from {self.tabelaBanco} where idcliente = {self.idcliente}"

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def idcliente(self):
        return self.__idcliente

    @idcliente.setter
    def idcliente(self, entrada):
        self.__idcliente = entrada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, entrada):
        self.__nome = entrada

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, entrada):
        self.__endereco = entrada

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
        return f"ID: {self.idcliente} - Nome: {self.nome}"