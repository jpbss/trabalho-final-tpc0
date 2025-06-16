from controle.controleGenerico import ControleGenerico
from controle.controleCliente import ControleCliente
from controle.controleVeiculo import ControleVeiculo
from modelo.compra import Compra
from modelo.cliente import Cliente
from modelo.veiculo import Veiculo


class ControleCompra(ControleGenerico):

    def incluir_compra(self, compra: Compra):
        self.incluir(compra)

    def alterar_compra(self, compra: Compra):
        self.alterar(compra)

    def deletar_compra(self, compra: Compra):
        self.delete(compra)

    def pesquisa_codigo(self, compra: Compra):
        registro = self.procuraRegistro(compra)
        if registro and len(registro) > 0:
            return self.converte_compra(registro[0])
        return Compra()

    def listar_todas_compras(self, compra: Compra):
        registros = self.listarTodos(compra)
        formatadas = []
        for registro in registros:
            formatadas.append(self.converte_compra(registro))
        return formatadas

    def converte_compra(self, entrada):
        compra = Compra()
        compra.idcompra = entrada[0]
        compra.data = entrada[3]
        compra.valor_pago = entrada[4]
        compra.forma_pagamento = entrada[5]

        cliente_dao = ControleCliente()
        cliente_obj = Cliente()
        cliente_obj.idcliente = entrada[2]
        compra.cliente = cliente_dao.pesquisa_codigo(cliente_obj)

        veiculo_dao = ControleVeiculo()
        veiculo_obj = Veiculo()
        veiculo_obj.idplaca = entrada[1]
        compra.veiculo = veiculo_dao.pesquisar_por_placa(veiculo_obj)

        return compra