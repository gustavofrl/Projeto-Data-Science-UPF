import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os
import pdfkit

url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
housing = pd.read_csv(url)
summary_stats = housing.describe()

# grafico valor medio das casas na california
housing["median_house_value"].hist(bins=50, figsize=(10, 5))
plt.title("Valor Médio das Casas")
plt.xlabel("Valor Médio das Casas ($)")
plt.ylabel("Frequência")
img_filename1 = os.path.join('raiz/imagens', "historico_valor_casas.png")
plt.savefig(img_filename1)
plt.close()

# graficos por proximidade ao ocenao
for col in ["median_income", "housing_median_age", "median_house_value"]:
    plt.figure(figsize=(8, 5))
    
    category_mapping = {
        "NEAR BAY": "Próximo à Baía",
        "<1H OCEAN": "Menos de 1 Hora do Oceano",
        "INLAND": "Interior",
        "NEAR OCEAN": "Próximo ao Oceano",
        "ISLAND": "Ilha"
    }    
    sns.boxplot(x=housing["ocean_proximity"].map(category_mapping), y=housing[col])
    
    if col == "median_income":
        title = "Gráfico de Renda Média por Proximidade ao Oceano"
        y_label = "Renda Média"
    elif col == "housing_median_age":
        title = "Gráfico de Idade Média das Casas por Proximidade ao Oceano"
        y_label = "Média de Idade das Casas"
    elif col == "median_house_value":
        title = "Gráfico de Valor Médio das Casas por Proximidade ao Oceano"
        y_label = "Valor Médio das Casas"
    
    plt.title(title)
    plt.xlabel("Proximidade ao Oceano")
    plt.ylabel(y_label)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    img_filename2 = os.path.join('raiz/imagens', f"{col}_por_proximidade_oceano.png")
    plt.savefig(img_filename2)
    
    plt.close() 

# relatório em Markdown
report_content = f"""
# Relatório do Projeto: California Housing Prices

## Tema do Projeto
Prever os preços das casas na Califórnia com base em diversos recursos.

## URL no GitHub
[California Housing Prices](https://github.com/ageron/handson-ml2)

## Dataset Utilizado
- Origem: [California Housing dataset](https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv)
- Variáveis: {', '.join(housing.columns)}

## Modificações no Dataset Original
- Nenhuma modificação foi realizada no dataset de exemplo.

## Análise Exploratória de Dados
- Visualização do Valor Médio das Casas:
![Valor Médio das Casas](imagenss/historico_valor_casas.png)

- Boxplots de Variáveis Importantes por Proximidade ao Oceano:
  - Renda Média:
  ![Renda Média](imagens/median_income_por_proximidade_oceano.png)

  - Idade Média das Casas:
  ![Idade Média das Casas](imagens/housing_median_age_por_proximidade_oceano.png)

  - Valor Médio das Casas:
  ![Valor Médio das Casas](imagens/median_house_value_por_proximidade_oceano.png)

## Modelos Utilizados ou Desenvolvidos
- Neste script de exemplo, a ênfase foi na análise exploratória de dados, e nenhum modelo de aprendizado de máquina específico foi desenvolvido. 
  Futuramente, ao evoluir o projeto, modelos podem ser explorados e incluídos nesta seção.

## Resultados Obtidos
- Algumas estatísticas descritivas:

{summary_stats.to_markdown()}

- Data do Relatório: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

report_filename = os.path.join('raiz', "report.md")
with open(report_filename, "w", encoding="utf-8") as file:
    file.write(report_content)

