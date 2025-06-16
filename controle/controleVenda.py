from controle.controleGenerico import ControleGenerico
from controle.controleCliente import ControleCliente
from controle.controleVeiculo import ControleVeiculo
from modelo.venda import Venda
from modelo.cliente import Cliente
from modelo.veiculo import Veiculo


class ControleVenda(ControleGenerico):

    def incluir_venda(self, venda: Venda):
        self.incluir(venda)

    def alterar_venda(self, venda: Venda):
        self.alterar(venda)

    def deletar_venda(self, venda: Venda):
        self.delete(venda)

    def pesquisa_codigo(self, venda: Venda):
        registro = self.procuraRegistro(venda)
        if registro and len(registro) > 0:
            return self.converte_venda(registro[0])
        return Venda()

    def listar_todas_vendas(self, objeto: Venda):
        registros = self.listarTodos(objeto)
        vendas_formatadas = []
        for registro in registros:
            vendas_formatadas.append(self.converte_venda(registro))
        return vendas_formatadas

    def converte_venda(self, entrada: list):
        venda = Venda()

        venda.idvenda = entrada[0]
        venda.data = entrada[1]
        venda.valor_vendido = entrada[2]
        venda.forma_pagamento = entrada[5]

        cliente_dao = ControleCliente()
        cliente_temp = Cliente()
        cliente_temp.idcliente = entrada[3]
        venda.cliente = cliente_dao.pesquisa_codigo(cliente_temp)

        veiculo_dao = ControleVeiculo()
        veiculo_temp = Veiculo()
        veiculo_temp.idplaca = entrada[4]
        venda.veiculo = veiculo_dao.pesquisar_por_placa(veiculo_temp)

        return venda