from flask import Blueprint, render_template, request, redirect, url_for, flash
from controle.controleCompra import ControleCompra
from controle.controleVeiculo import ControleVeiculo
from controle.controleCliente import ControleCliente
from modelo.compra import Compra
from modelo.veiculo import Veiculo
from modelo.cliente import Cliente

bpCompra = Blueprint(
    'bpCompra', __name__,
    template_folder='templates',
    url_prefix='/compras'
)

compraDAO = ControleCompra()
veiculoDAO = ControleVeiculo()
clienteDAO = ControleCliente()

@bpCompra.route('/')
def lista():
    compras = compraDAO.listar_todas_compras(Compra())
    return render_template('compras/list.html', compras=compras)

@bpCompra.route('/new')
def novo():
    veiculos = veiculoDAO.listar_todos_veiculos(Veiculo())
    clientes = clienteDAO.listar_todos_clientes(Cliente())
    return render_template('compras/form.html', compra=Compra(), veiculos=veiculos, clientes=clientes, is_edit=False)

@bpCompra.route('/edit/<int:id>')
def editar(id):
    compra = Compra()
    compra.idcompra = id
    compra_encontrada = compraDAO.pesquisa_codigo(compra)

    if not compra_encontrada.idcompra:
        return redirect(url_for('bpCompra.lista'))

    veiculos = veiculoDAO.listar_todos_veiculos(Veiculo())
    clientes = clienteDAO.listar_todos_clientes(Cliente())

    return render_template('compras/form.html', compra=compra_encontrada, veiculos=veiculos, clientes=clientes, is_edit=True)

@bpCompra.route('/save', methods=['POST'])
def salvar():
    compra = Compra()
    is_edit = request.form.get('is_edit') == 'True'

    compra.idcompra = int(request.form.get('idcompra')) if request.form.get('idcompra') else None
    compra.data = request.form.get('data')
    compra.valor_pago = float(request.form.get('valor_pago'))
    compra.forma_pagamento = request.form.get('forma_pagamento')
    compra.veiculo.idplaca = request.form.get('idplaca')
    compra.cliente.idcliente = int(request.form.get('idcliente'))

    if is_edit:
        compraDAO.alterar_compra(compra)
    else:
        compraDAO.incluir_compra(compra)

    return redirect(url_for('bpCompra.lista'))

@bpCompra.route('/delete/<int:id>', methods=['POST'])
def deletar(id):
    compra = Compra()
    compra.idcompra = id
    compraDAO.deletar_compra(compra)
    return redirect(url_for('bpCompra.lista'))