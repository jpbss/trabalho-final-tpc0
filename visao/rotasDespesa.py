from flask import Blueprint, render_template, request, redirect, url_for

from controle.controleDespesa import ControleDespesa
from controle.controleVeiculo import ControleVeiculo
from controle.controlePrestador import ControlePrestador
from modelo.despesa import Despesa
from modelo.prestador import Prestador
from modelo.veiculo import Veiculo

bpDespesa = Blueprint(
    'bpDespesa', __name__,
    template_folder='templates',
    url_prefix='/despesas'
)

despesaDAO = ControleDespesa()
veiculoDAO = ControleVeiculo()
prestadorDAO = ControlePrestador()


# Rota para LISTAR as despesas de um veículo específico
@bpDespesa.route('/<string:idveiculo>')
def lista(idveiculo):
    v = Veiculo()
    v.idplaca = idveiculo
    v = veiculoDAO.pesquisar_por_placa(v)
    despesas = despesaDAO.listar_despesas_veiculo(v)
    return render_template("despesas/list.html", despesas=despesas, totalDespesas=v.total_despesa, idveiculo=idveiculo)


# Rota para o formulário de uma NOVA despesa
@bpDespesa.route('/new/<string:idveiculo>')
def novo(idveiculo):
    # Apenas busca os prestadores e os envia. Simples assim.
    prestadores = prestadorDAO.listar_todos_prestadores(Prestador())
    return render_template('despesas/form.html', despesa=Despesa(), prestadores=prestadores, idveiculo=idveiculo)


@bpDespesa.route('/edit/<string:idveiculo>/<int:iddespesa>')
def editar(idveiculo, iddespesa):
    d = Despesa()
    d.iddespesa = iddespesa
    despesa_encontrada = despesaDAO.pesquisa_codigo(d)

    prestadores = prestadorDAO.listar_todos_prestadores(Prestador())

    return render_template('despesas/form.html', despesa=despesa_encontrada, prestadores=prestadores,
                           idveiculo=idveiculo)
@bpDespesa.route('/save/<string:idveiculo>', methods=['POST'])
def salvar(idveiculo):
    d = Despesa()

    d.iddespesa = request.form.get('iddespesa')
    d.veiculo.idplaca = idveiculo
    d.valor = float(request.form.get('valor'))
    d.data_servico = request.form.get('data_servico')
    d.descricao = request.form.get('descricao')
    d.prestador.idprestador = int(request.form.get('idprestador'))

    # Se 'iddespesa' for uma string vazia, converte para None
    if not d.iddespesa:
        d.iddespesa = None

    if d.iddespesa:
        # Chama o método correto que já existia no seu controle
        despesaDAO.alterar_despesa(d)
    else:
        despesaDAO.incluir_despesa(d)

    return redirect(url_for('bpDespesa.lista', idveiculo=idveiculo))


# Rota para DELETAR uma despesa
@bpDespesa.route('/delete/<string:idveiculo>/<int:iddespesa>', methods=['POST'])
def deletar(idveiculo, iddespesa):
    d = Despesa()
    d.iddespesa = iddespesa
    # O método deletar_despesa precisa do id do veículo para recalcular o total
    d.veiculo.idplaca = idveiculo

    # Chama o método correto que já existia no seu controle
    despesaDAO.deletar_despesa(d)

    return redirect(url_for('bpDespesa.lista', idveiculo=idveiculo))