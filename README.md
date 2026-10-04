# Análise de Dados de Recursos Humanos (HR)

**Aluna:** Celina Machado de Liz

**Turma:** T3 - VISUALIZAÇÃO DE DADOS E BUSINESS INTELLIGENCE

## Objetivo do Trabalho
O meu objetivo neste projeto foi analisar dados de Recursos Humanos utilizando SQL para a extração e Python para a Análise Exploratória de Dados (EDA). Direcionei a análise para entender a distribuição de salários e a relação entre cargos, departamentos e regiões.

## Tabelas Utilizadas
Extraí os dados do banco FreeSQL (esquema HR) utilizando as seguintes tabelas:
* **EMPLOYEES:** Dados dos funcionários e seus respectivos salários.
* **DEPARTMENTS & JOBS:** Informações sobre os departamentos e os cargos ocupados.
* **LOCATIONS, COUNTRIES & REGIONS:** Dados geográficos para o mapeamento da localização dos funcionários.

## Consultas SQL
Desenvolvi duas consultas utilizando `LEFT JOIN` e filtros `WHERE`:
1. **query_1.sql:** Relaciona os funcionários com os seus departamentos e cargos, filtrando salários superiores a 3000.
2. **query_2.sql:** Mapeia os funcionários por região (Cidade, Estado, País), garantindo que a região não seja nula.

## Análise em Python
Importei os dados extraídos em formato CSV para um script Python e utilizei as bibliotecas Pandas, Matplotlib e Seaborn para a exploração.
Calculei as seguintes métricas de salário:
* **Média:** R$ 7696.49
* **Mediana:** R$ 7500.00
* **Mínimo:** R$ 3100.00
* **Máximo:** R$ 24000.00

Criei dois gráficos principais: um Histograma para demonstrar a distribuição geral dos salários e um Boxplot para evidenciar a variação salarial entre os diferentes departamentos.

## Como Executar o Projeto
**Pré-requisitos:** Python 3.x, Pandas, Matplotlib, Seaborn.
1. Clone este repositório.
2. Crie e ative um ambiente virtual (`python -m venv venv`).
3. Instale as dependências (`pip install pandas matplotlib seaborn`).
4. Execute o arquivo `analise.py` para visualizar os cálculos no terminal e os gráficos em uma janela anexa.

## Sugestões de Melhoria
Para versões futuras deste meu projeto, considero interessante automatizar a extração de dados diretamente do banco de dados para o Python via API ou biblioteca de conexão, além de cruzar dados de tempo de empresa com os salários atuais.
