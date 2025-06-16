from controle.controleGenerico import ControleGenerico
from modelo.prestador import Prestador

class ControlePrestador(ControleGenerico):
    def incluir_prestador(self, prestador: Prestador):
        self.incluir(prestador)

    def alterar_prestador(self, prestador: Prestador):
        self.alterar(prestador)

    def deletar_prestador(self, prestador: Prestador):
        self.delete(prestador)

    def pesquisa_codigo(self, prestador: Prestador):
        registro = self.procuraRegistro(prestador)
        retorno = Prestador()
        if registro and len(registro) > 0:
            return self.converte_prestador(registro[0])
        return retorno

    def listar_todos_prestadores(self, prestador: Prestador):
        registros = self.listarTodos(prestador)
        formatados = []
        for registro in registros:
            formatados.append(self.converte_prestador(registro))
        return formatados

    def converte_prestador(self, entrada):
        prestador = Prestador()
        prestador.idprestador = entrada[0]
        prestador.nome_empresa = entrada[1]
        prestador.cidade = entrada[2]
        prestador.uf = entrada[3]
        prestador.cep = entrada[4]
        return prestador