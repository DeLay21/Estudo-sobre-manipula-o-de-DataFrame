import pandas as pd
import numpy as np

a = {'ID': ['AA2930', 'BB4563', 'CC2139', 'DE2521', 'GT3462', 'HH1158'],
    'Nome': ['Victor', 'Amanda', 'Bruna', 'Carlos', 'Ricardo', 'Maria'],
    'Idade': [20,35,40,54,30,27],
    'CEP': ['00092-029', '11111-111', '22222-888', '00000-999', '88888-111', '77777-666']
}

a = pd.DataFrame(a, columns= ['ID', 'Nome', 'Idade', 'CEP'])
print(a)

print('\n ==================================================')

b = {'ID': ['CC2617', 'DD1239', 'EE1208', 'GT3462', 'HH1158'],
    'Nome': ['Marcos', 'Patricia', 'Erika', 'Ricardo', 'Maria'],
    'Idade': [19,30,22,30,27],
    'CEP': ['00092-029', '11111-111', '22222-888', '88888-111', '77777-666']
}

b = pd.DataFrame(b, columns= ['ID', 'Nome', 'Idade', 'CEP'])
print(b)

print('\n ==================================================')

Compras = {'ID': ['AA2930', 'DD1239', 'CC2139', 'DD1239', 'CC2617', 'AA2930', 'HH1158', 'HH1158'],
            'Data': ['2019-01-30', '2019-01-30', '2019-01-30', '2019-02-01', '2019-02-20', '2019-03-15', '2019-04-13', '2019-05-01'],
            'Valor': [200, 100, 40, 150, 300, 25, 50, 500]
        }

Compras = pd.DataFrame(Compras, columns= ['ID', 'Data', 'Valor'])
print(Compras)

print('\n ==================================================')

#Com que funciona o merge pd.merge(tabela_esquerda, tabela_direita, on="coluna_coincidente", how="left|right|inner|outer" )

#inner Join
Clientes_ab = pd.merge(a, b, on=["ID"], how= "inner")
print(Clientes_ab)

print('\n ==================================================')

Clientes_ab = pd.merge(a, b[['ID', 'Idade']], on=["ID"], how= "inner", suffixes=('_A', '_b'))
print(Clientes_ab)

print('\n ==================================================')

#Join Full
Lojas = pd.concat([a, b], ignore_index=True)
Clientes_unicos = Lojas.drop_duplicates(subset='ID') #.drop_duplicates remove todas as duplicadas do DataFreame
print(Clientes_unicos)

print('\n ==================================================')

#Left Join

CompA = pd.merge(a, Compras, on=['ID'], how='left')
print(CompA)

print('\n ==================================================')

#Outer

OuAB = pd.merge(a, b, on=['ID'], how='outer', suffixes=('_A', '_B'), indicator=True)
print(OuAB)

print('\n ==================================================')

#GroupBy

df = pd.DataFrame({'A': ['Verdadeiro', 'Falso', 'Verdadeiro', 'Falso', 'Verdadeiro', 'Falso', 'Verdadeiro', 'Falso'],
                    'B': ['um', 'um', 'dois', 'tres', 'dois', 'dois', 'um', 'tres'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)
                })
print(df)

print('\n ==================================================')

somaA = df.groupby(['A']).sum()
print(somaA)

print('\n ==================================================')

somaB = df.groupby(['B']).sum()
print(somaB)

print('\n ==================================================')

somaAB = df.groupby(['A', 'B']).sum()
print(somaAB)