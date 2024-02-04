import pandas as pd

df = pd.read_excel('Dados.xlsx', sheet_name='Dados Brutos')
comprimentosdf = df.iloc[0]
comprimentos = [float(comprimento) for comprimento in comprimentosdf[1:9]]
periodo = df.iloc[7]
periodo2 = [float(tempo)**2 for tempo in periodo[1:9]]

print(periodo2)
print(comprimentos)