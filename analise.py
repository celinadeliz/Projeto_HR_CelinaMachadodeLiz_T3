import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# carregando os csvs que baixei do banco
tabela_salarios = pd.read_csv('query_01.csv')
tabela_regioes = pd.read_csv('query_02.csv')

# garantindo que as colunas fiquem em maiusculo para nao dar erro
tabela_salarios.columns = tabela_salarios.columns.str.upper()
tabela_regioes.columns = tabela_regioes.columns.str.upper()

# calculos de salario
print("--- Estatísticas de Salário ---")
print(f"Média: R$ {tabela_salarios['SALARY'].mean():.2f}")
print(f"Mediana: R$ {tabela_salarios['SALARY'].median():.2f}")
print(f"Mínimo: R$ {tabela_salarios['SALARY'].min():.2f}")
print(f"Máximo: R$ {tabela_salarios['SALARY'].max():.2f}")

# plotando os graficos
plt.figure(figsize=(12, 5))

# histograma geral
plt.subplot(1, 2, 1)
sns.histplot(tabela_salarios['SALARY'], bins=10, kde=True, color='blue')
plt.title('Distribuição dos Salários')
plt.xlabel('Salário')
plt.ylabel('Quantidade de Pessoas')

# boxplot por departamento
plt.subplot(1, 2, 2)
sns.boxplot(data=tabela_salarios, x='SALARY', y='DEPARTMENT_NAME', color='purple')
plt.title('Salários por Departamento')
plt.xlabel('Salário')
plt.ylabel('Departamento')

plt.tight_layout()
plt.show()