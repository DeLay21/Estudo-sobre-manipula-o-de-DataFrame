import pandas as pd
import numpy as np

#Acresentando coluna a um Dataset existente
print("\n ======================================")
AtuData = pd.date_range('20090501', periods= 60, freq='D')
AtuDf = pd.DataFrame(np.random.randn(60,5), index = AtuData, columns= list("ABCDE"))
print(AtuDf.shape)
print(AtuDf.head(5))

AtuDf['Produto'] = AtuDf['A'] * AtuDf['B']
print(AtuDf)

#Visualização de dados
print("\n ======================================")

AtuDf.head(3) #.head permite ver a quantidade de linhas a serem visualizando a parti de cima para baixo
AtuDf.tail(3) #.tail permite ver a quantidade de linhas a serem visualizando a parti de baixo para cima
print(AtuDf.columns) #.columns Permite ver as colunas de um DataSet
print(AtuDf.T)#.T é a transpostar do conujunto de dados, ela pega o que é linha e transforma em coluna e o que coluna em linha

#Combinando DataFrames
print("\n ======================================")

ComDF1 = pd.DataFrame({'A': ['A0','A1', 'A2', 'A3',],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index = [0,1,2,3])

ComDF2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                        index = [4,5,6,7])

ComDF3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index = [8,9,10,11])

CombFra = pd.concat([ComDF1, ComDF2, ComDF3])
print(CombFra)

print("\n ======================================")

CombFra = pd.concat([ComDF1, ComDF2, ComDF3], keys=['F1', 'F2', 'F3']) #O Keys ele define a chave para cada Dataframe Concatenado
print(CombFra)