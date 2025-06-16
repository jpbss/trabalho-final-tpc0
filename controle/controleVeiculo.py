from controle.controleGenerico import ControleGenerico
from modelo.veiculo import Veiculo

class ControleVeiculo(ControleGenerico):
    def incluir_veiculo(self, veiculo: Veiculo):
        self.incluir(veiculo)

    def alterar_veiculo(self, veiculo: Veiculo):
        self.alterar(veiculo)

    def deletar_veiculo(self, veiculo: Veiculo):
        self.delete(veiculo)

    def atualizar_total_despesas(self, veiculo: Veiculo, despesaAdicional):
        veiculo = self.pesquisar_por_placa(veiculo)
        if veiculo:
            veiculo.total_despesa = veiculo.total_despesa + despesaAdicional
            self.alterar_veiculo(veiculo)

    def pesquisar_por_placa(self, veiculo: Veiculo):
        registro = self.procuraRegistro(veiculo)
        retorno = Veiculo()
        if registro and len(registro) > 0:
            return self.converte_veiculo(registro[0])
        return retorno

    def listar_todos_veiculos(self, veiculo: Veiculo):
        registros = self.listarTodos(veiculo)
        formatados = []
        for registro in registros:
            formatados.append(self.converte_veiculo(registro))
        return formatados

    def converte_veiculo(self, entrada):
        veiculo = Veiculo()
        veiculo.idplaca = entrada[0]
        veiculo.ano = entrada[1]
        veiculo.modelo = entrada[2]
        veiculo.preco_fipe = entrada[3]
        veiculo.fabricante = entrada[4]
        veiculo.modelo_veiculo = entrada[5]
        veiculo.cor = entrada[6]
        veiculo.preco_venda = entrada[7]
        veiculo.total_despesa = float(entrada[8])
        return veiculo