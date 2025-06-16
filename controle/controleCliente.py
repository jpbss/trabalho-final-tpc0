from controle.controleGenerico import ControleGenerico
from modelo.cliente import Cliente

class ControleCliente(ControleGenerico):
    def incluir_cliente(self, cliente: Cliente):
        self.incluir(cliente)

    def alterar_cliente(self, cliente: Cliente):
        self.alterar(cliente)

    def deletar_cliente(self, cliente: Cliente):
        self.delete(cliente)

    def pesquisa_codigo(self, cliente: Cliente):
        registro = self.procuraRegistro(cliente)
        retorno = Cliente()
        if registro and len(registro) > 0:
            return self.converte_cliente(registro[0])
        return retorno

    def listar_todos_clientes(self, cliente: Cliente):
        registros = self.listarTodos(cliente)
        formatados = []
        for registro in registros:
            formatados.append(self.converte_cliente(registro))
        return formatados

    def converte_cliente(self, entrada):
        cliente = Cliente()
        cliente.idcliente = entrada[0]
        cliente.nome = entrada[1]
        cliente.endereco = entrada[2]
        cliente.cidade = entrada[3]
        cliente.uf = entrada[4]
        cliente.cep = entrada[5]
        return cliente