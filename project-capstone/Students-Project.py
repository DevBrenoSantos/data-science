# Breno Amaral Santos - C02177

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Students-Project.csv')
df.head()

# Histograma da coluna 'Age'
plt.figure(figsize=(10, 6))
sns.histplot(df['entry_age'], kde=True)
plt.title('Distribuição da Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()

# Gráfico de barras da coluna 'Gender'
plt.figure(figsize=(10, 6))
sns.countplot(x='gender', data=df)
plt.title('Distribuição por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.show()

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
sns.scatterplot(x='entry_age', y='hs_gpa', data=df)
plt.title('Relação entre Idade e Pontuação')
plt.xlabel('Idade')
plt.ylabel('Pontuação')
plt.show()