from flask import Blueprint, render_template, request, redirect, url_for, flash
from controle.controlePrestador import ControlePrestador
from modelo.prestador import Prestador

bpPrestador = Blueprint('bpPrestador', __name__, template_folder='templates', url_prefix='/prestadores')
prestadorDAO = ControlePrestador()


@bpPrestador.route('/')
def lista():
    prestadores = prestadorDAO.listar_todos_prestadores(Prestador())
    return render_template('prestadores/list.html', prestadores=prestadores)


@bpPrestador.route('/new')
def novo():
    return render_template('prestadores/form.html', prestador=Prestador())


@bpPrestador.route('/edit/<int:id>')
def editar(id):
    prestador = Prestador()
    prestador.idprestador = id
    prestador_encontrado = prestadorDAO.pesquisa_codigo(prestador)
    return render_template('prestadores/form.html', prestador=prestador_encontrado)


@bpPrestador.route('/save', methods=['POST'])
def salvar():
    prestador = Prestador()
    prestador.idprestador = request.form.get('idprestador')
    prestador.nome_empresa = request.form.get('nome')
    prestador.cidade = request.form.get('cidade')
    prestador.uf = request.form.get('uf')
    prestador.cep = request.form.get('cep')

    if prestador.idprestador:
        prestadorDAO.alterar_prestador(prestador)
    else:
        prestadorDAO.incluir_prestador(prestador)

    return redirect(url_for('bpPrestador.lista'))


@bpPrestador.route('/delete/<int:id>', methods=['POST'])
def deletar(id):
    prestador = Prestador()
    prestador.idprestador = id
    prestadorDAO.deletar_prestador(prestador)
    return redirect(url_for('bpPrestador.lista'))
