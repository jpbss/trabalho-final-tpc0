# app.py

from flask import Flask, render_template

from visao.rotasCliente import bpCliente
from visao.rotasDespesa import bpDespesa
from visao.rotasPrestador import bpPrestador
from visao.rotasVeiculo import bpVeiculo
# --- Adicionar estas importações ---
from visao.rotasCompra import bpCompra
from visao.rotasVenda import bpVenda

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ajufgaiujkhvxziyovsghwloygunsckviosygfw[´123]~1´4[12~]'

app.register_blueprint(bpCliente)
app.register_blueprint(bpPrestador)
app.register_blueprint(bpVeiculo)
app.register_blueprint(bpDespesa)
# --- Adicionar estes registros ---
app.register_blueprint(bpCompra)
app.register_blueprint(bpVenda)


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)