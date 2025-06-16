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


@bpDespesa.route('/<string:idveiculo>')
def lista(idveiculo):
    v = Veiculo()
    v.idplaca = idveiculo
    v = veiculoDAO.pesquisar_por_placa(v)
    despesas = despesaDAO.listar_despesas_veiculo(v)
    # Passando o idveiculo para ser usado nos links do template
    return render_template("despesas/list.html", despesas=despesas, totalDespesas=v.total_despesa, idveiculo=idveiculo)


@bpDespesa.route('/new/<string:idveiculo>')
def novo(idveiculo):
    prestadores = prestadorDAO.listar_todos_prestadores(Prestador())
    # Passamos um objeto Despesa vazio e o idveiculo
    return render_template('despesas/form.html', despesa=Despesa(), prestadores=prestadores, idveiculo=idveiculo)


@bpDespesa.route('/edit/<string:idveiculo>/<int:iddespesa>')
def editar(idveiculo, iddespesa):
    d = Despesa()
    d.iddespesa = iddespesa
    despesa_encontrada = despesaDAO.pesquisa_codigo(d)

    prestadores = prestadorDAO.listar_todos_prestadores(Prestador())

    return render_template('despesas/form.html', despesa=despesa_encontrada, prestadores=prestadores,
                           idveiculo=idveiculo)


# Rota para SALVAR (tanto novas despesas quanto edições)
@bpDespesa.route('/save/<string:idveiculo>', methods=['POST'])
def salvar(idveiculo):
    d = Despesa()

    # Pega os dados do formulário
    d.iddespesa = request.form.get('iddespesa')
    d.veiculo.idplaca = idveiculo
    d.valor = float(request.form.get('valor'))
    d.data_servico = request.form.get('data_servico')
    d.descricao = request.form.get('descricao')

    # CORREÇÃO CRÍTICA: Pega o ID do prestador selecionado no formulário
    d.prestador.idprestador = int(request.form.get('idprestador'))

    # Se 'iddespesa' tiver um valor, é uma alteração. Senão, é uma inclusão.
    if d.iddespesa:
        # A API de alteração não estava implementada, agora está
        despesaDAO.alterar(d)  # Supondo que seu controle genérico tenha o método alterar
    else:
        despesaDAO.incluir_despesa(d)

    return redirect(url_for('bpDespesa.lista', idveiculo=idveiculo))


# Rota para DELETAR uma despesa
@bpDespesa.route('/delete/<string:idveiculo>/<int:iddespesa>', methods=['POST'])
def deletar(idveiculo, iddespesa):
    d = Despesa()
    d.iddespesa = iddespesa

    # O método de deleção deve estar no seu controle de despesas
    despesaDAO.delete(d)  # Supondo que seu controle genérico tenha o método delete

    return redirect(url_for('bpDespesa.lista', idveiculo=idveiculo))