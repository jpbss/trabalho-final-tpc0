from flask import Blueprint, render_template, request, redirect, url_for, flash
from controle.controleVeiculo import ControleVeiculo
from modelo.veiculo import Veiculo

bpVeiculo = Blueprint('bpVeiculo', __name__, template_folder='templates', url_prefix='/veiculos')
veiculoDAO = ControleVeiculo()


@bpVeiculo.route('/')
def lista():
    veiculos = veiculoDAO.listar_todos_veiculos(Veiculo())
    return render_template('veiculos/list.html', veiculos=veiculos)


@bpVeiculo.route('/edit/<string:id>')
def editar(id):
    veiculo = Veiculo()
    veiculo.idplaca = id
    veiculo_encontrado = veiculoDAO.pesquisar_por_placa(veiculo)
    return render_template('veiculos/form.html', veiculo=veiculo_encontrado, is_edit=True)


@bpVeiculo.route('/new')
def novo():
    return render_template('veiculos/form.html', veiculo=Veiculo(), is_edit=False)


@bpVeiculo.route('/save', methods=['POST'])
def salvar():
    is_edit = request.form.get('is_edit') == 'True'
    veiculo = Veiculo()

    veiculo.idplaca = request.form.get('idplaca')
    veiculo.ano = request.form.get('ano')
    veiculo.modelo = request.form.get('modelo')
    veiculo.preco_fipe = request.form.get('preco_fipe')
    veiculo.fabricante = request.form.get('fabricante')
    veiculo.modelo_veiculo = request.form.get('modelo_veiculo')
    veiculo.preco_venda = request.form.get('preco_venda')
    veiculo.cor = request.form.get('cor')

    if is_edit:
        veiculoDAO.alterar_veiculo(veiculo)
    else:
        veiculo_existente = veiculoDAO.pesquisar_por_placa(veiculo)
        if veiculo_existente and veiculo_existente.idplaca:
            flash('Erro: A placa informada já está cadastrada.', 'error')
            return render_template('veiculos/form.html', veiculo=veiculo, is_edit=False)

        veiculoDAO.incluir_veiculo(veiculo)

    return redirect(url_for('bpVeiculo.lista'))


@bpVeiculo.route('/delete/<string:id>', methods=['POST'])
def deletar(id):

    veiculo = Veiculo()
    veiculo.idplaca = id
    veiculoDAO.deletar_veiculo(veiculo)
    return redirect(url_for('bpVeiculo.lista'))

