import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
housing = pd.read_csv(url)
summary_stats = housing.describe()
report_content = ""

# grafico valor medio das casas na california
housing["median_house_value"].hist(bins=50, figsize=(10, 5))
plt.title("Valor Médio das Casas")
plt.xlabel("Valor Médio das Casas ($)")
plt.ylabel("Frequência")
img_filename1 = os.path.join('raiz/imagens', "historico_valor_casas.png")
plt.savefig(img_filename1)
plt.close()

# graficos por proximidade ao oceano
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

longitude_mean = summary_stats.loc["mean", "longitude"]
latitude_mean = summary_stats.loc["mean", "latitude"]
median_age_mean = summary_stats.loc["mean", "housing_median_age"]
median_income_mean = summary_stats.loc["mean", "median_income"]
median_house_value_mean = summary_stats.loc["mean", "median_house_value"]
population_mean = summary_stats.loc["mean", "population"]
households_mean = summary_stats.loc["mean", "households"]

results_section = """
## Resultados Obtidos

Nesta seção, apresentamos uma análise detalhada das estatísticas descritivas do conjunto de dados "California Housing Prices". Essas estatísticas fornecem insights valiosos sobre as características e distribuições das variáveis relevantes, fornecendo uma base sólida para a compreensão do cenário imobiliário na Califórnia. Abaixo estão alguns pontos-chave destacados pelas estatísticas descritivas:

### 1. Longitude e Latitude
- **Longitude Média:** As coordenadas geográficas médias indicam uma localização centralizada, aproximadamente a {longitude_mean}.
- **Latitude Média:** A latitude média, em torno de {latitude_mean}, sugere que os dados se concentram em uma região específica da Califórnia.

### 2. Idade Média das Casas
- **Média de Idade das Casas:** A idade média das casas na região é de {median_age_mean} anos. Isso pode influenciar significativamente as preferências dos compradores e as condições gerais do mercado imobiliário.

### 3. Renda Média
- **Renda Média:** A renda média da população local é de {median_income_mean}, indicando o potencial de compra dos residentes.

### 4. Valores Médios das Casas
- **Valor Médio das Casas:** O valor médio das casas é de ${median_house_value_mean}. Esta informação é crucial para avaliar a acessibilidade e a faixa de preços do mercado imobiliário.

### 5. Distribuição de População e Habitações
- **População Média:** A população média é de {population_mean}, enquanto o número médio de domicílios é de {households_mean}. Esses números refletem o tamanho médio das comunidades locais.

### 6. Estatísticas Adicionais
- **Variabilidade:** A presença de desvios padrão e valores mínimos e máximos fornece insights sobre a variabilidade e a amplitude das variáveis em questão.

Essas análises estatísticas formam a base para as etapas subsequentes do projeto, permitindo uma compreensão mais profunda das nuances do mercado imobiliário da Califórnia. Além disso, servirão como referência ao explorar relações mais complexas e ao desenvolver modelos preditivos no decorrer do projeto.
"""

report_content += results_section
report_content += f"\n\n- Data do Relatório: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
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
![Valor Médio das Casas](imagens/historico_valor_casas.png)

- Variáveis Importantes por Proximidade ao Oceano:

  - Renda Média:

  ![Renda Média](imagens/median_income_por_proximidade_oceano.png)

  - Idade Média das Casas:

  ![Idade Média das Casas](imagens/housing_median_age_por_proximidade_oceano.png)

  - Valor Médio das Casas:

  ![Valor Médio das Casas](imagens/median_house_value_por_proximidade_oceano.png)

{results_section}

- Algumas estatísticas descritivas:

{summary_stats.to_markdown()}
"""

report_filename = os.path.join('raiz', "report.md")
with open(report_filename, "w", encoding="utf-8") as file:
    file.write(report_content)
