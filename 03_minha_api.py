from flask import Flask, render_template
#Criar o app flask

app = Flask(__name__)

# Rota da página inicial
@app.route('/') #decorator - verificar
def home():
    return "<h1>Bem vindo a página inicial.</h1>"

# Rota do Sobre
@app.route('/sobre')
def sobre():
    return "Feito com carinho ♥ por Diogo"
# Rota com variavel na url
@app.route('/ola/<nome>')
def ola(nome):
    return f'<h1>Olá, {nome}</h1>'


#Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)