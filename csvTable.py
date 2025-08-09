import pandas as pd
from RenamedColumns import RENNAMED_COLUMNS, RENAMED_COMPANY_SIZE, RENAMED_EMPLOYMENT_TYPE, RENAMED_EXPERIENCE_LEVEL, RENAMED_REMOTE_RATIO

#Reading the .csv file
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
 

def renamingCollums():
    df.rename(columns=RENNAMED_COLUMNS, inplace=True)
    df["Tamanho da Empresa"] = df["Tamanho da Empresa"].replace(RENAMED_COMPANY_SIZE)
    df["Proporção de Trabalho Remoto"] = df["Proporção de Trabalho Remoto"].replace(RENAMED_REMOTE_RATIO)
    df["Tipo de Emprego"] = df["Tipo de Emprego"].replace(RENAMED_EMPLOYMENT_TYPE)
    df["Nível de Experiência"] = df["Nível de Experiência"].replace(RENAMED_EXPERIENCE_LEVEL)


if __name__ == "__main__":
    renamingCollums()

    print("-" * 200 + "\n TABLE \n" + "-" * 200)
    print(df.head())
    lines, columns = df.shape[0], df.shape[1]
    print(f"{lines} lines | {columns} columns")

    print("\n" + "-" * 200 + "\n TABLE DESCRIPTION \n" + "-" * 200)
    print(df.describe())

    print("\n" + "-" * 200 + "\n COLUMNS TYPE INFOS \n" + "-" * 200)
    print(df.info())