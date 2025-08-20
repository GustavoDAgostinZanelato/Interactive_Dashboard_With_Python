# 📊 Dashboard de Salários na Área de Dados

Este projeto é um **dashboard interativo** desenvolvido em **Python**
com **Streamlit** e **Plotly**, que apresenta uma análise gráfica dos
salários de profissionais da área de dados.

O objetivo é permitir a exploração de informações sobre remuneração
considerando variáveis como **ano, senioridade, tipo de contrato e
tamanho da empresa**, de forma simples e visual.

🔗 O dashboard pode ser acessado online através do link:\
👉 [Dashboard de Salários na Área de
Dados](https://dashboard-de-salarios-com-area-de-dados.streamlit.app/)

------------------------------------------------------------------------

## 🚀 Funcionalidades

-   Filtros interativos por **ano, senioridade, tipo de contrato** e
    **tamanho da empresa**.
-   Exibição de **métricas gerais** como salário médio, salário máximo,
    total de registros e cargo mais frequente.
-   **Visualizações gráficas** com Plotly:
    -   Top 10 cargos por salário médio.
    -   Distribuição de salários anuais.
    -   Proporção de tipos de trabalho (remoto, híbrido, presencial).
    -   Mapa de salários médios de **Cientistas de Dados** por país.
-   **Tabela detalhada** com os dados filtrados.

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    Interactive_Dashboard_With_Python
    ├── Dashboard.py            # Arquivo principal com o código do Streamlit
    ├── requirements.txt        # Dependências do projeto
    ├── functionsSummary.txt    # Anotações feitas durante as aulas
    ├── salaryData.csv          # Arquivo .csv de dados (importado via GitHub)
    └── README.md               # Documentação do projeto

------------------------------------------------------------------------

## 🛠️ Tecnologias Utilizadas

-   **Python 3.10+**
-   **Streamlit** -- para criação do dashboard interativo\
-   **Pandas** -- para manipulação e tratamento dos dados\
-   **Plotly Express** -- para visualizações gráficas avançadas\
-   **CSV Dataset** -- com informações sobre salários de profissionais
    da área de dados

------------------------------------------------------------------------

## 📥 Instalação

1.  Clone este repositório:

``` bash
git clone https://github.com/GustavoDAgostinZanelato/Interactive_Dashboard_With_Python.git
cd Interactive_Dashboard_With_Python
```

2.  Crie um ambiente virtual (opcional, mas recomendado):

``` bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scriptsctivate      # Windows
```

3.  Instale as dependências:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Execução

Para rodar o projeto localmente, execute:

``` bash
streamlit run .\dashboard.py
```

O Streamlit abrirá automaticamente o dashboard no navegador em:\
👉 `http://localhost:8501`

------------------------------------------------------------------------

## 📊 Fonte do Projeto

Este projeto foi desenvolvido com base na **Imersão Dados Python**,
curso oferecido pela **Alura**.
