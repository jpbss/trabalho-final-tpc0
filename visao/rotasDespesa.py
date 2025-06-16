from flask import Blueprint, render_template, request, redirect, url_for

from controle.controleDespesa import ControleDespesa
from controle.controleVeiculo import ControleVeiculo
from modelo.despesa import Despesa
from modelo.veiculo import Veiculo
from visao.rotasVeiculo import veiculoDAO

bpDespesa = Blueprint(
    'bpDespesa', __name__,
    template_folder='templates',
    url_prefix='/despesas'
)

despesaDAO = ControleDespesa()
veiculoDAO = ControleVeiculo()
placaAtual = ""

@bpDespesa.route('/<string:idveiculo>')
def lista(idveiculo):

    veiculo = Veiculo()
    veiculo.idplaca = idveiculo
    veiculo = veiculoDAO.pesquisar_por_placa(veiculo)

    despesas = despesaDAO.listar_despesas_veiculo(veiculo)
    global placaAtual
    placaAtual = idveiculo
    return render_template("despesas/list.html", despesas=despesas, totalDespesas=veiculo.total_despesa)

@bpDespesa.route('/new')
def novo():
    return render_template('despesas/form.html', despesa=Despesa(), idplaca=placaAtual)


# @bpDespesa.route('/edit/<int:id>')
# def editar(id):
#     cliente= Cliente()
#     cliente.idcliente = int(id)
#     cliente_encontrado = clienteDAO.pesquisa_codigo(cliente)
#     return render_template('clientes/form.html', cliente=cliente_encontrado)


@bpDespesa.route('/save', methods=['POST'])
def salvar():
    despesa = Despesa()
    despesa.veiculo.idplaca = placaAtual
    despesa.valor = float(request.form.get('valor'))
    despesa.data_servico = request.form.get('data')
    despesa.descricao = request.form.get('descricao')
    despesa.prestador.idprestador = 1

    if despesa.iddespesa:
        despesaDAO.alterar_despesa(despesa)
    else:
        despesaDAO.incluir_despesa(despesa)

    return redirect(url_for('bpDespesa.lista', idveiculo=placaAtual))
