import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. DADOS EXTRAÍDOS DOS PDFS (Amostragem Real) ---
# Estou criando um DataFrame com os dados reais que li dos seus documentos
data = [
    # GUSTAVO FREITAS MACEDO (O "Campeão")
    {"Data": "2025-01-20", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 73727.56, "Categoria": "Consultoria/Jurídico", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-02-25", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 44695.49, "Categoria": "Consultoria/Jurídico", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-02-25", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 85483.74, "Categoria": "Consultoria/Jurídico", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-03-31", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 132391.24, "Categoria": "Consultoria/Jurídico", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-05-27", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 123333.82, "Categoria": "Consultoria/Jurídico", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-06-26", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 110124.55, "Categoria": "Consultoria/Jurídico", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-07-25", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 106306.11, "Categoria": "Consultoria/Jurídico", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-08-28", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 106515.92, "Categoria": "Consultoria/Jurídico", "CNPJ": "41.146.282/0001-17"},

    # NUNES GOLGO (O Advogado)
    {"Data": "2025-02-25", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 34540.28, "Categoria": "Jurídico", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-03-31", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 52359.23, "Categoria": "Jurídico", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-06-26", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 74494.81, "Categoria": "Jurídico", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-07-30", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 74545.29, "Categoria": "Jurídico", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-08-29", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 74563.46, "Categoria": "Jurídico", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-09-26", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 75331.69, "Categoria": "Jurídico", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-10-30", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 76553.74, "Categoria": "Jurídico", "CNPJ": "19.320.060/0001-10"},

    # MASTER PROJETOS (A Obra do Contrato 017/2025)
    {"Data": "2025-02-25", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 77350.00, "Categoria": "Obras", "CNPJ": "46.523.623/0001-40"},
    {"Data": "2025-07-30", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 46900.00, "Categoria": "Obras", "CNPJ": "46.523.623/0001-40"},
    {"Data": "2025-09-29", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 46900.00, "Categoria": "Obras", "CNPJ": "46.523.623/0001-40"},
    {"Data": "2025-09-30", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 77350.00, "Categoria": "Obras", "CNPJ": "46.523.623/0001-40"},
    {"Data": "2025-10-30", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 46900.00, "Categoria": "Obras", "CNPJ": "46.523.623/0001-40"},

    # CONSTRUÇÃO AMX (Outra grande beneficiária)
    {"Data": "2025-03-21", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Obras/Serviços", "CNPJ": "21.238.834/0001-00"},
    {"Data": "2025-06-26", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Obras/Serviços", "CNPJ": "21.238.834/0001-00"},
    {"Data": "2025-08-29", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Obras/Serviços", "CNPJ": "21.238.834/0001-00"},
    {"Data": "2025-10-30", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Obras/Serviços", "CNPJ": "21.238.834/0001-00"},

    # EXEMPLOS DE PESSOAS FÍSICAS (A "Folha")
    {"Data": "2025-09-19", "Favorecido": "DAVID MEDEIROS DE CASTRO", "Valor": 6760.00, "Categoria": "Pessoa Física", "CNPJ": "-"},
    {"Data": "2025-09-19", "Favorecido": "MIGUEL DA COSTA MIRANDA", "Valor": 6300.00, "Categoria": "Pessoa Física", "CNPJ": "-"},
    {"Data": "2025-09-24", "Favorecido": "WENDREL LOPES RIBEIRO", "Valor": 1260.00, "Categoria": "Pessoa Física", "CNPJ": "-"},
    {"Data": "2025-05-06", "Favorecido": "LARISSA REIS DE FARIAS", "Valor": 5450.00, "Categoria": "Pessoa Física", "CNPJ": "-"},
]

df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data'])

# --- 2. CONFIGURAÇÃO DA PÁGINA STREAMLIT ---
st.set_page_config(page_title="Rastreador de Royalties - Nhamundá", layout="wide")

st.title("🕵️‍♀️ Rastreador de Royalties: Nhamundá 2025")
st.markdown("""
**Onde foi parar o dinheiro?** A prefeitura declarou milhões em "Despesas Diversas". Esta ferramenta abre a caixa preta 
e mostra quem são os reais beneficiários desses pagamentos.
""")

# --- 3. METRICAS TOPO ---
col1, col2, col3 = st.columns(3)
total_gasto = df['Valor'].sum()
maior_favorecido = df.groupby('Favorecido')['Valor'].sum().idxmax()
valor_maior = df.groupby('Favorecido')['Valor'].sum().max()

col1.metric("Total Identificado (Amostra)", f"R$ {total_gasto:,.2f}")
col2.metric("Maior Beneficiário Individual", maior_favorecido)
col3.metric("Valor Recebido (Maior Benef.)", f"R$ {valor_maior:,.2f}")

st.markdown("---")

# --- 4. FILTROS E BUSCA ---
st.subheader("🔍 Busque por nomes ou empresas")
col_busca1, col_busca2 = st.columns(2)
busca_nome = col_busca1.text_input("Nome do Favorecido (Ex: Nunes Golgo, Gustavo)")
filtro_cat = col_busca2.multiselect("Filtrar por Categoria", df['Categoria'].unique())

df_filtrado = df.copy()

if busca_nome:
    df_filtrado = df_filtrado[df_filtrado['Favorecido'].str.contains(busca_nome, case=False)]
if filtro_cat:
    df_filtrado = df_filtrado[df_filtrado['Categoria'].isin(filtro_cat)]

# --- 5. TABELA DE DADOS ---
st.dataframe(
    df_filtrado[['Data', 'Favorecido', 'CNPJ', 'Categoria', 'Valor']].sort_values(by='Data', ascending=False),
    use_container_width=True,
    hide_index=True
)

# --- 6. GRÁFICOS REVELADORES ---
st.markdown("---")
st.subheader("📊 Quem está levando a maior fatia?")

# Gráfico de Barras: Top 10 Favorecidos
top_favorecidos = df_filtrado.groupby('Favorecido')['Valor'].sum().reset_index().sort_values(by='Valor', ascending=False).head(10)

fig_bar = px.bar(
    top_favorecidos, 
    x='Valor', 
    y='Favorecido', 
    orientation='h',
    text_auto='.2s',
    title="Top 10 Maiores Beneficiários (2025)",
    color='Valor',
    color_continuous_scale='Reds'
)
fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig_bar, use_container_width=True)

# Alerta sobre Lei dos Royalties
st.warning("""
⚠️ **Nota de Transparência:** Pela Lei 12.858/2013, 75% dos royalties deveriam ir para **Educação** e 25% para **Saúde**. Os dados acima mostram predominância de gastos com **Consultoria Jurídica, 
Construção Civil e Pessoas Físicas**.

""")
