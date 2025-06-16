from select import select
from unicodedata import decimal

from controle.controleGenerico import ControleGenerico
from controle.controleVeiculo import ControleVeiculo
from controle.controlePrestador import ControlePrestador
from modelo.despesa import Despesa
from modelo.veiculo import Veiculo
from modelo.prestador import Prestador

class ControleDespesa(ControleGenerico):

    def incluir_despesa(self, despesa: Despesa):
        self.incluir(despesa)
        veiculo = Veiculo()
        veiculo.idplaca = despesa.veiculo.idplaca
        ControleVeiculo().atualizar_total_despesas(veiculo, despesa.valor)

    def alterar_despesa(self, despesa: Despesa):
        self.alterar(despesa)

    def deletar_despesa(self, despesa: Despesa):
        self.delete(despesa)

    def pesquisa_codigo(self, despesa: Despesa):
        registro = self.procuraRegistro(despesa)
        if registro and len(registro) > 0:
            return self.converte_despesa(registro[0])
        return Despesa()

    def listar_todas_despesas(self, despesa: Despesa):
        registros = self.listarTodos(despesa)
        formatadas = []
        for registro in registros:
            formatadas.append(self.converte_despesa(registro))
        return formatadas

    def listar_despesas_veiculo(self, veiculo: Veiculo):
        sql = f"select * from despesa where idplaca = '{veiculo.idplaca}'"
        self.ob.abrirConexao()
        registros = self.ob.selectQuery(sql)
        formatadas = []
        for registro in registros:
            formatadas.append(self.converte_despesa(registro))
        return formatadas

    def converte_despesa(self, entrada):
        despesa = Despesa()
        despesa.iddespesa = int(entrada[1])
        despesa.descricao = entrada[2]
        despesa.valor = entrada[3]
        despesa.data_servico = entrada[4]

        veiculo_dao = ControleVeiculo()
        veiculo_obj = Veiculo()
        veiculo_obj.idplaca = entrada[0]
        despesa.veiculo = veiculo_dao.pesquisar_por_placa(veiculo_obj)

        prestador_dao = ControlePrestador()
        prestador_obj = Prestador()
        prestador_obj.idprestador = int(entrada[5])
        despesa.prestador = prestador_dao.pesquisa_codigo(prestador_obj)
        return despesa