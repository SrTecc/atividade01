from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route("/")
def index ():
    return render_template('index.html')

@app.route("/sobre")
def sobre():
    return "<h1> Portal de vendas</h1>"

@app.route("/perfil/<username>")
def username(username):
    cok = make_response("<h2> cookie criado </h2>")
    cok.set_cookie('username', username)
    print("O que está se passando", username)
    return cok

@app.route('/perfil2/')
@app.route("/perfil2/<username>")
def username2(username=None):
    cokusername = request.cookies.get('username')
    return render_template('perfil.html', username=username, cokusername=cokusername)

@app.route("/cad/usario")
def usuario():
    return render_template('perfil.html', titulo="Cadastro de Usuario")

@app.route("/cad/caduser", methods=['POST'])
def caduser():
    return request.form

@app.route("/cad/anuncio")
def anuncio():
    return render_template('anuncio.html')

@app.route("/anuncios/pergunta")
def pergunta():
    return render_template('pergunta.html')

@app.route("/anuncios/compra")
def compra():
    print("anuncio comprado")
    return ""

@app.route("/anuncio/favoritos")
def favoritos():
    print("favorito inserido")
    return f"<h4>Comprado</h4>"

@app.route("/config/categoria")
def categoria():
    return render_template('categoria.html')

@app.route("/relatorios/vendas")
def relVendas():
    return render_template('relVendas.html')

@app.route("/relatorios/compras")
def relCompras():
    return render_template('relCompras.html')

