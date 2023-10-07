# abrir arquivos excel
import pandas as pd

listaMeses = ['Janeiro', 'Fevereiro', 'Março',
              'Abril', 'Maio', 'Junho']
# abrir cada arquivo do excell
for mes in listaMeses: #loop
    #print(mes)
    tabelaVendas = pd.read_excel(f'{mes}.xlsx') # abrindo tabela excel
    #print(tabelaVendas)
# para cada arquivo verificar se há venda maior que 55mil
    if (tabelaVendas['Vendas'] > 55000).any(): # pedindo para filtar se houve essa venda
        vendedor = tabelaVendas.loc[tabelaVendas['Vendas'] > 55000, 'Vendedor'].values[0] # pedidndo para isolar 'quem' e
        vendas = tabelaVendas.loc[tabelaVendas['Vendas'] > 55000, 'Vendas'].values[0] #o 'valor' da venda
        print(f'No mês de: {mes}, o vendedor: {vendedor}, bateu a meta com venda de: R${vendas:.2f}')




        #OBS:>>>>  no final foi usado o aplicativo 'Twilio' que também pode ser importado pelo python para que
        # fosse enviado um sms ao, por exemplo, gerente informando quem foi o vendedor que bateu
        # a meta do mès e com qual valor.


