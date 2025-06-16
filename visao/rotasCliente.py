from flask import Blueprint, render_template, request, redirect, url_for
from controle.controleCliente import ControleCliente
from modelo.cliente import Cliente

bpCliente = Blueprint(
    'bpCliente', __name__,
    template_folder='templates',
    url_prefix='/clientes'
)

clienteDAO = ControleCliente()

@bpCliente.route('/')
def lista():
    clientes = clienteDAO.listar_todos_clientes(Cliente())
    return render_template('clientes/list.html', clientes=clientes)


@bpCliente.route('/new')
def novo():
    return render_template('clientes/form.html', cliente=Cliente())


@bpCliente.route('/edit/<int:id>')
def editar(id):
    cliente= Cliente()
    cliente.idcliente = int(id)
    cliente_encontrado = clienteDAO.pesquisa_codigo(cliente)
    return render_template('clientes/form.html', cliente=cliente_encontrado)


@bpCliente.route('/save', methods=['POST'])
def salvar():
    cliente = Cliente()
    cliente.idcliente = int(request.form.get('idcliente')) if request.form.get('idcliente') else None
    cliente.nome = request.form.get('nome')
    cliente.endereco = request.form.get('endereco')
    cliente.cidade = request.form.get('cidade')
    cliente.uf = request.form.get('uf')
    cliente.cep = request.form.get('cep')

    if cliente.idcliente:
        clienteDAO.alterar_cliente(cliente)
    else:
        clienteDAO.incluir_cliente(cliente)

    return redirect(url_for('bpCliente.lista'))


@bpCliente.route('/delete/<int:id>', methods=['POST'])
def deletar(id):
    cliente = Cliente()
    cliente.idcliente = int(id)
    clienteDAO.deletar_cliente(cliente)
    return redirect(url_for('bpCliente.lista'))
