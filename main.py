import pandas as pd

compras = pd.read_excel('compras.xlsx')
pagamentos = pd.read_excel('pagamentos.xlsx')

pagamentos_pendentes =pagamentos.loc[pagamentos['Status']=='Pendente']


for indexP, rowP in pagamentos_pendentes.iterrows():
    print(indexP, rowP)

    compras_localizadas = compras.loc[(compras['Status'] =='Pendente') &
                                        (compras['Valor'] == rowP['Valor']) &
                                        (compras['Vencimento'] == rowP['Data Pagamento'])]
    
    if(len(compras_localizadas) > 0):
        for indexC, rowC in compras_localizadas.iterrows():
            compras.loc[indexC, 'Status'] = 'Pago'
            pagamentos.loc[indexP, 'Status'] = 'Pago'
            print('ALTERADO')
            break

compras.to_excel('compras2.xlsx', index=False)
pagamentos.to_excel('pagamentos2.xlsx', index=False)