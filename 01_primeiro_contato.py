import pandas as pd
caminho = 'C:/Users/sabado/Desktop/Diogo/01_base_vendas.xlsx'

### Leitura simples de arquivo do excel ###

df = pd.read_excel(caminho)
print(df)

#Lendo uma planilha específica

df_clientes = pd.read_excel(caminho,sheet_name=0)
print(df_clientes)

df_clientes2 = pd.read_excel(caminho,sheet_name=1)
print(df_clientes)

#Lendo uma coluna específica

dfNomeClientes = pd.read_excel(caminho, sheet_name=0, usecols=['Cliente'])
print(dfNomeClientes)

#Lendo a partir de uma linha

df_vendas = pd.read_excel(
    caminho,
    sheet_name=0,
    skiprows=5
)

print(df_vendas)