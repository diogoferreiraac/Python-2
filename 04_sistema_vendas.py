#pip install flask
#pip install pandas
#pip install matplotlib

from flask import Flask, jsonify, send_file
import pandas as pd
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

#Carregar o nosso arquivo do excel
arquivo = 'C:/Users/sabado/Desktop/Diogo/01_base_vendas.xlsx'

df1 = pd.read_excel(arquivo,sheet_name=0)
df2 = pd.read_excel(arquivo,sheet_name=1)
dfConsolidado = pd.concat([df1,df2], ignore_index=True)
dfConsolidado['Status'] = dfConsolidado['Plano Vendido'].apply(lambda x: 'Premium' if x == 'Enterprise' else 'Padrão') #verificar lambda

@app.route('/')
def home():

    conteudo = '''
    API para análise de dados de vendas - Use as rotas para obter as análises! <br/> 
    <a href = '/clientes_por_cidade'> Clientes por Cidade </a> <br/>
    <a href = '/vendas_por_plano'> Vendas por Plano </a> <br/>
    <a href = '/topCidades'> Top 3 Cidades </a> <br/>
    <a href = '/total_clientes'> Total de Clientes </a> <br/>
    <a href = '/status'> Status do Plano </a> <br/>
    <a href = '/download/xlsx'> Download XLSX </a> <br/>
    <a href = '/download/csv'> Download CSV </a>
    '''

    return conteudo

@app.route('/clientes_por_cidade')
def clientesPorCidade():
    clientesPorCidade = dfConsolidado.groupby('Cidade')['Cliente'].nunique().sort_values(ascending=False)
    return jsonify(clientesPorCidade.to_dict())

@app.route('/vendas_por_plano')
def vendasPorPlano():
    vendasPorPlano = dfConsolidado['Plano Vendido'].value_counts()
    return jsonify(vendasPorPlano.to_dict())

@app.route('/topCidades')
def topCidades():
    clientesPorCidade = dfConsolidado.groupby('Cidade')['Cliente'].nunique().sort_values(ascending=False)
    topCidades = clientesPorCidade.head(3)
    return jsonify(topCidades.to_dict())

@app.route('/total_clientes')
def totalClientes():
    total = dfConsolidado['Cliente'].nunique()
    return jsonify({"totalClientes": total})

@app.route('/status')
def status():
    statusDist = dfConsolidado['Status'].value_counts()
    return jsonify(statusDist.to_dict())

@app.route('/download/xlsx')
def download_xlsx():
    salvar_xlsx = 'C:/Users/sabado/Desktop/Diogo/vendas_download.xlsx'
    dfConsolidado.to_excel(salvar_xlsx, index=False)
    return f"<h1> Arquivo de Excel salvo em {salvar_xlsx}</h1>"

@app.route('/download/csv')
def download_csv():
    salvar_csv = 'C:/Users/sabado/Desktop/Diogo/vendas_download.csv'
    dfConsolidado.to_csv(salvar_csv, index=False)
    return f"<h1> Arquivo CSV salvo em {salvar_csv}</h1>"

if __name__ == '__main__':
    app.run(debug=True)