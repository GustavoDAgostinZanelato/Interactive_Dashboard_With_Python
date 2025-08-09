import pandas as pd
from RenamedColumns import RENAMED_COLUMNS, RENAMED_COMPANY_SIZE, RENAMED_EMPLOYMENT_TYPE, RENAMED_EXPERIENCE_LEVEL, RENAMED_REMOTE_RATIO

import numpy as np

#Reading the .csv file
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
 

def dataCleaning():
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
 

if __name__ == "__main__":
    dataCleaning()
    dfClean = dataCleaning()

    print("-" * 200 + "\n TABLE \n" + "-" * 200)
    print(dfClean.head())
    lines, columns = dfClean.shape[0], dfClean.shape[1]
    print(f"{lines} lines | {columns} columns")

    print("\n" + "-" * 200 + "\n TABLE DESCRIPTION \n" + "-" * 200)
    print(dfClean.describe())

    print("\n" + "-" * 200 + "\n COLUMNS TYPE INFOS \n" + "-" * 200)
    print(dfClean.info())