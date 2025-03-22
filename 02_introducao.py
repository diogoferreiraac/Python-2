import pandas as pd

#Carregar arquivo
arquivo = 'C:/Users/sabado/Desktop/Diogo/01_base_vendas.xlsx'

#Carregar os dados das duas abas do excel
df1 = pd.read_excel(arquivo,sheet_name=0)
df2 = pd.read_excel(arquivo, sheet_name=1)

#Exibir as primeiras linhas para conferir como estão os dados
print(f'Relatório de Vendas 1:\n{df1.head()}')
print(f'Relatório de Vendas 2:\n{df2.head()}')

#Verificar se tem duplicatas nas duas planilhas
print(f'Duplicadas no "Relatório de Vendas 1" \n {df1.duplicated().sum()}') #O código verifica se há valores duplicados e os soma
print(f'Duplicadas no "Relatório de Vendas 2" \n {df2.duplicated().sum()}')

#Merge dos dois DataFrames combinando as tabelas concatenando apenas as linhas, já que as colunas são as mesmas
dfConsolidado = pd.concat([df1,df2], ignore_index=True)
print(f'\nDados Consolidados \n {dfConsolidado.head()}')

print(f'Verificar se há duplicatas no consolidado: \n {dfConsolidado.duplicated().sum()}')

#Removendo as duplicatas, caso existam

dfConsolidado = dfConsolidado.drop_duplicates()

#Exibir o número de clientes por cidade

clientesPorCidade = dfConsolidado.groupby('Cidade')['Cliente'].nunique().sort_values(ascending=False)
print(f'\nNúmero de clientes por cidade\n{clientesPorCidade}')

#Exibir o número de vendas por plano
vendasPorPlano = dfConsolidado['Plano Vendido'].value_counts()
print(f'\nNúmero de vendas por plano\n{vendasPorPlano}')

#Exibir as 3 primeiras cidades com mais clientes
topCidades = clientesPorCidade.head(3)
print(f'\nTop 3 Cidades\n{topCidades}')

#Adicionar a coluna de 'status' (exemplo ficticio de analise) e classificar os planos (Premium = Entreprise, Else = Padrão)
dfConsolidado['Status'] = dfConsolidado['Plano Vendido'].apply(lambda x: 'Premium' if x == 'Enterprise' else 'Padrão') #verificar lambda

#Exibir a distribuição dos Status
statusDist = dfConsolidado['Status'].value_counts()
print(f'\nDistribuição de Status por PLano\n{statusDist}')

#Salvar o DataFrame consolidado em dois formatos (Excel e CSV)
dfConsolidado.to_excel('Dados_Consolidados.xlsx', index=False)
dfConsolidado.to_csv('Dados_Consolidados.csv', index=False)
print("Dados gerados com sucesso. Confira o(s) arquivo(s) na pasta.")