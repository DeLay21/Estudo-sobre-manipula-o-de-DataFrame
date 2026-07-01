import pandas as pd
import numpy as np

#Dados coletados onde é armazendado qualquer tipo de dados onde possui um rotulo (index) que associa a cada elemento
print("\n ======================================")
series = pd.Series([7, 4, 2, np.nan, 6, 9])
print(series)

#Uma estrutura do tipo series
print("\n ======================================")
print(type(series))

#Como obter datas no pandas e seis devidos peridos e frequência de tempo
print("\n ======================================")

datas = pd.date_range('20180112', periods = 6, freq= 'D')
print(datas)

#Criaçãod de um DataFrame com 6 linhas e 4 colunas onde a função randn gerar numeros aleatorios com uma media 0 e um desvio padrão 1 com o index datas
print("\n ======================================")

df = pd.DataFrame(np.random.randn(6,4), index= datas, columns= list("ABCD"))
print(df)
print(type(df))

df2 = pd.DataFrame({"A": 7,
                    "B": pd.Timestamp("20190101"),
                    "C": pd.Series(1, index=list(range(4)), dtype='Float32'),
                    "D": pd.array([3] * 4, dtype='int32'),
                    "E": pd.Categorical(["teste", "train", "test", "train"]),
                    "F": "Python"
                    })
print(df2)
print(df2.dtypes)