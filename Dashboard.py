import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import plotly.express as px
from RenamedColumns import RENAMED_COLUMNS, RENAMED_COMPANY_SIZE, RENAMED_EMPLOYMENT_TYPE, RENAMED_EXPERIENCE_LEVEL, RENAMED_REMOTE_RATIO

#Reading the .csv file
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
 

def renamingColumns():
    df.rename(columns=RENAMED_COLUMNS, inplace=True)

    replacements = {
        "Tamanho_Empresa": RENAMED_COMPANY_SIZE,
        "Proporcao_Trabalho_Remoto": RENAMED_REMOTE_RATIO,
        "Tipo_Emprego": RENAMED_EMPLOYMENT_TYPE,
        "Nivel_Experiencia": RENAMED_EXPERIENCE_LEVEL
    }

    for col, mapping in replacements.items():
        df[col] = df[col].replace(mapping)


def dataCleaning():
    dfClean = (
        df.dropna() # Removing the 10 null values
        .astype({'Ano': "int64", "Salario": "float64", "Salario_USD": "float64"}) # Changing the type of the columns
    )
    return dfClean
 

def tableChats():
    # Criando uma figura para encaixar os gráficos
    fig, axs = plt.subplots(2, 2, figsize=(14,10))
    fig.suptitle("Análise Salarial")

    # Gráfico de barras Nivel_Experiencia x Salario_USD
    chartOrder = dfClean.groupby('Nivel_Experiencia')['Salario_USD'].mean().sort_values(ascending=True).index
    sns.barplot(data=dfClean, x="Nivel_Experiencia", y="Salario_USD", order=chartOrder, ax=axs[0, 0])
    axs[0, 0].set_title("Salário médio por senioridade")
    axs[0, 0].set_xlabel("Senioridade")
    axs[0, 0].set_ylabel("Salário médio anual (USD)")

    # Histograma Frequência dos salários Salario_USD
    sns.histplot(dfClean['Salario_USD'], bins=50, kde=True, ax=axs[0, 1]) #"Bins" é a largura das dolunas. "KDE" é a linha mestra do gráfico
    axs[0, 1].set_title("Distribuição anual dos salários")
    axs[0, 1].set_xlabel("Salário em USD")
    axs[0, 1].set_ylabel("Frequência")

    # Boxplot Frequência dos salários Salario_USD
    sns.boxplot(x=dfClean['Salario_USD'], ax=axs[1, 0])
    axs[1, 0].set_title("Boxplot Salário USD Anual")
    axs[1, 0].set_xlabel("Salário em USD")

    # Boxplot Distribuição dos salários por senioridade
    expLevelOrder = ["Júnior", "Pleno", "Sênior", "Executivo"]
    sns.boxplot(x="Nivel_Experiencia", y="Salario_USD", data=dfClean, order=expLevelOrder, palette="Set2", hue="Nivel_Experiencia", ax=axs[1, 1])
    axs[1, 1].set_title("Distribuição por Senioridade")
    axs[1, 1].set_xlabel("Nível de Experiência")
    axs[1, 1].set_ylabel("Salário em USD")

    plt.tight_layout()  # Junta as subfiguras a figura principal
    charts = plt.show() # variável com a tela formada
    return charts      


if __name__ == "__main__":
    renamingColumns()
    dfClean = dataCleaning()

    print("-" * 200 + "\n TABLE \n" + "-" * 200)
    print(dfClean.head())
    lines, columns = dfClean.shape[0], dfClean.shape[1]
    print(f"{lines} lines | {columns} columns")

    # print("\n" + "-" * 200 + "\n TABLE DESCRIPTION \n" + "-" * 200)
    # print(dfClean.describe())

    # print("\n" + "-" * 200 + "\n COLUMNS TYPE INFOS \n" + "-" * 200)
    # print(dfClean.info())

    charts = tableChats()