import streamlit as st
import pandas as pd
import plotly.express as px

#-----------------------------------------------------------------------------------------------------------------------
# --- Configuração da Página ---
#-----------------------------------------------------------------------------------------------------------------------
st.set_page_config(
    page_title="Dashboard de Salários com Área de Dados",
    page_icon="📊",
    layout="wide"
)


df = pd.read_csv("https://raw.githubusercontent.com/GustavoDAgostinZanelato/Interactive_Dashboard_With_Python/refs/heads/master/salaryData.csv")


#-----------------------------------------------------------------------------------------------------------------------
# --- Barra Lateral (Filtros) ---
#-----------------------------------------------------------------------------------------------------------------------
st.sidebar.header("🔍 Filtros")

# Filtros de Ano
availableYears = sorted(df['ano'].unique())
SelectedYears = st.sidebar.multiselect("Ano", availableYears, default=availableYears)

# Filtros de Senioridade
availableExpLevel = sorted(df['senioridade'].unique())
selectedExpLevel = st.sidebar.multiselect("Senioridade", availableExpLevel, default=availableExpLevel)

# Filtro por Tipo de Contrato
availableContracts = sorted(df["contrato"].unique())
selectedContracts = st.sidebar.multiselect("Tipo de Contrato", availableContracts, default=availableContracts)

# Filtro por Tamanho da Empresa
availableSize = sorted(df['tamanho_empresa'].unique())
selectedSize = st.sidebar.multiselect("Tamanho da Empresa", availableSize, default=availableSize)

# Aplicando os filtros as informações da página
filtered_df = df[
    (df["ano"].isin(SelectedYears)) &
    (df["senioridade"].isin(selectedExpLevel)) &
    (df["contrato"].isin(selectedContracts)) &
    (df["tamanho_empresa"].isin(selectedSize))
]


#-----------------------------------------------------------------------------------------------------------------------
# --- Conteúdo Principal da Página ---
#-----------------------------------------------------------------------------------------------------------------------
st.title("Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.")

st.subheader("Métricas gerais (Salário anual em USD)")

if not filtered_df.empty:
    salario_medio = filtered_df['usd'].mean()
    salario_maximo = filtered_df['usd'].max()
    total_registros = filtered_df.shape[0]
    cargo_mais_frequente  = filtered_df['cargo'].mode()[0]
else:
    salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário Médio", f"${salario_medio:,.0f}")
col2.metric("Salário Máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de Registros", f"${total_registros:,.0f}")
col4.metric("Cargo mais Frequente", cargo_mais_frequente)

st.markdown("---")


# --- Gráficos com Plotly ---
st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not filtered_df.empty:
        top_jobs = filtered_df.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        job_chart = px.bar(
            top_jobs, 
            x='usd', 
            y='cargo', 
            orientation="h", 
            title="Top 10 cargos por salário médio",
            labels={'usd': "Média salarial anual (USD)", "cargo": ""}
        )
        job_chart.update_layout(title_x = 0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(job_chart, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

with col_graf2:
    if not filtered_df.empty:
        hist_chart = px.histogram(
            filtered_df,
            x='usd',
            nbins = 30,
            title = "Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': ''}
        )
        hist_chart.update_layout(title = 0.1)
        st.plotly_chart(hist_chart, use_container_width=True)
       
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")


col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not filtered_df.empty:
        remote_count = filtered_df['remoto'].value_counts().reset_index()
        remote_count.columns = ['tipo_trabalho', 'quantidade']
        remote_chart = px.pie(
            remote_count,
            names = 'tipo_trabalho',
            values = 'quantidade',
            title = "Proporção dos tipos de trabalho",
        )
        remote_chart.update_traces(textinfo='percent+label')
        remote_chart.update_layout(title=0.1)
        st.plotly_chart(remote_chart, use_container_width=True)
       
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with col_graf4:
    if not filtered_df.empty:
        df_ds = filtered_df[filtered_df['cargo'] == 'Data Scientist']
        avg_country_ds = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        country_chart = px.choropleth(
            avg_country_ds,
            locations = 'residencia_iso3',
            color = 'usd',
            color_continuous_scale='rdylgn',
            title='Salário médio de Cientista de Dados por país',
            labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
        )
        country_chart.update_layout(title=0.1)
        st.plotly_chart(country_chart, use_container_width=True)
       
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")


# --- Tabela de Dados Detalhados ---
st.subheader("Dados Detalhados")
st.dataframe(filtered_df)
