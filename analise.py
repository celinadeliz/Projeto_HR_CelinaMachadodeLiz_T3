import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurei o visual base para deixar os gráficos mais limpos e sem poluição
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    'font.size': 11,
    'font.family': 'sans-serif',
    'axes.titleweight': 'bold',
    'figure.facecolor': '#FAFAFA', # fundo levemente claro para dar contraste
    'axes.facecolor': '#FAFAFA'
})

# Carregando os csvs que extraí do banco
tabela_salarios = pd.read_csv('query_01.csv')
tabela_regioes = pd.read_csv('query_02.csv')

# Garantindo que as colunas fiquem em maiúsculo para eu não ter erro
tabela_salarios.columns = tabela_salarios.columns.str.upper()
tabela_regioes.columns = tabela_regioes.columns.str.upper()

# Meus cálculos de salário
print("--- Estatísticas de Salário ---")
print(f"Média: R$ {tabela_salarios['SALARY'].mean():.2f}")
print(f"Mediana: R$ {tabela_salarios['SALARY'].median():.2f}")
print(f"Mínimo: R$ {tabela_salarios['SALARY'].min():.2f}")
print(f"Máximo: R$ {tabela_salarios['SALARY'].max():.2f}")

# Defini uma paleta de cores: lilás escuro no histograma e lilás claro no boxplot
cor_histograma = '#5E35B1' # lilás mais escuro para destacar
cor_boxplot = '#C3B1E1'    # lilás pastel suave 

# Aumentei a largura da figura para dar mais espaço aos nomes dos departamentos
plt.figure(figsize=(16, 6))

# Meu gráfico 1: Histograma geral
plt.subplot(1, 2, 1)
ax1 = sns.histplot(tabela_salarios['SALARY'], bins=10, kde=True, color=cor_histograma, edgecolor='white')
plt.title('Distribuição dos Salários', pad=15)
plt.xlabel('Salário (R$)', labelpad=10)
plt.ylabel('Quantidade de Pessoas', labelpad=10)
sns.despine(left=True, bottom=True) # tirei as bordas sólidas para não poluir
ax1.yaxis.grid(True, linestyle='--', alpha=0.5) 
ax1.xaxis.grid(False)

# Meu gráfico 2: Boxplot por departamento
plt.subplot(1, 2, 2)
# Ordenei os departamentos pela mediana do salário para ficar harmônico
ordem = tabela_salarios.groupby('DEPARTMENT_NAME')['SALARY'].median().sort_values(ascending=False).index
ax2 = sns.boxplot(data=tabela_salarios, x='SALARY', y='DEPARTMENT_NAME', color=cor_boxplot, order=ordem, linewidth=1.5, fliersize=4)
plt.title('Salários por Departamento', pad=15)
plt.xlabel('Salário (R$)', labelpad=10)
plt.ylabel('') # tirei o nome do eixo Y porque já fica óbvio que são os departamentos
sns.despine(left=True, bottom=True)
ax2.xaxis.grid(True, linestyle='--', alpha=0.5)
ax2.yaxis.grid(False)

# Aumentei o espaçamento (w_pad) para forçar a divisão entre os gráficos
plt.tight_layout(w_pad=5.0)
plt.show()