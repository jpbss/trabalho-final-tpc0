from flask import Blueprint, render_template, request, redirect, url_for, flash
from controle.controleVenda import ControleVenda
from controle.controleVeiculo import ControleVeiculo
from controle.controleCliente import ControleCliente
from modelo.venda import Venda
from modelo.veiculo import Veiculo
from modelo.cliente import Cliente

bpVenda = Blueprint(
    'bpVenda', __name__,
    template_folder='templates',
    url_prefix='/vendas'
)

vendaDAO = ControleVenda()
veiculoDAO = ControleVeiculo()
clienteDAO = ControleCliente()

@bpVenda.route('/')
def lista():
    vendas = vendaDAO.listar_todas_vendas(Venda())
    return render_template('vendas/list.html', vendas=vendas)

@bpVenda.route('/new')
def novo():
    veiculos = veiculoDAO.listar_todos_veiculos(Veiculo())
    clientes = clienteDAO.listar_todos_clientes(Cliente())
    return render_template('vendas/form.html', venda=Venda(), veiculos=veiculos, clientes=clientes, is_edit=False)

@bpVenda.route('/edit/<int:id>')
def editar(id):
    venda = Venda()
    venda.idvenda = id
    venda_encontrada = vendaDAO.pesquisa_codigo(venda)

    if not venda_encontrada.idvenda:
        return redirect(url_for('bpVenda.lista'))

    veiculos = veiculoDAO.listar_todos_veiculos(Veiculo())
    clientes = clienteDAO.listar_todos_clientes(Cliente())

    return render_template('vendas/form.html', venda=venda_encontrada, veiculos=veiculos, clientes=clientes, is_edit=True)

@bpVenda.route('/save', methods=['POST'])
def salvar():
    venda = Venda()
    is_edit = request.form.get('is_edit') == 'True'

    venda.idvenda = int(request.form.get('idvenda')) if request.form.get('idvenda') else None
    venda.data = request.form.get('data')
    venda.valor_vendido = float(request.form.get('valor_vendido'))
    venda.forma_pagamento = request.form.get('forma_pagamento')
    venda.veiculo.idplaca = request.form.get('idplaca')
    venda.cliente.idcliente = int(request.form.get('idcliente'))

    if is_edit:
        vendaDAO.alterar_venda(venda)
    else:
        vendaDAO.incluir_venda(venda)

    return redirect(url_for('bpVenda.lista'))

@bpVenda.route('/delete/<int:id>', methods=['POST'])
def deletar(id):
    venda = Venda()
    venda.idvenda = id
    vendaDAO.deletar_venda(venda)
    return redirect(url_for('bpVenda.lista'))