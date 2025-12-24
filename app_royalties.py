import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Monitor de Royalties - Nhamundá",
    page_icon="⚖️",
    layout="wide"
)

# --- 1. DADOS DOS DOCUMENTOS (Mantendo a base que extraímos) ---
data = [
    # GUSTAVO FREITAS MACEDO (Consultoria Jurídica/Administrativa)
    {"Data": "2025-01-20", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 73727.56, "Categoria": "Consultoria Jurídica/Adm", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-02-25", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 44695.49, "Categoria": "Consultoria Jurídica/Adm", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-02-25", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 85483.74, "Categoria": "Consultoria Jurídica/Adm", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-03-31", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 132391.24, "Categoria": "Consultoria Jurídica/Adm", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-05-27", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 123333.82, "Categoria": "Consultoria Jurídica/Adm", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-06-26", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 110124.55, "Categoria": "Consultoria Jurídica/Adm", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-07-25", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 106306.11, "Categoria": "Consultoria Jurídica/Adm", "CNPJ": "41.146.282/0001-17"},
    {"Data": "2025-08-28", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 106515.92, "Categoria": "Consultoria Jurídica/Adm", "CNPJ": "41.146.282/0001-17"},

    # NUNES GOLGO (Advocacia)
    {"Data": "2025-02-25", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 34540.28, "Categoria": "Advocacia Terceirizada", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-03-31", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 52359.23, "Categoria": "Advocacia Terceirizada", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-06-26", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 74494.81, "Categoria": "Advocacia Terceirizada", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-07-30", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 74545.29, "Categoria": "Advocacia Terceirizada", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-08-29", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 74563.46, "Categoria": "Advocacia Terceirizada", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-09-26", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 75331.69, "Categoria": "Advocacia Terceirizada", "CNPJ": "19.320.060/0001-10"},
    {"Data": "2025-10-30", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 76553.74, "Categoria": "Advocacia Terceirizada", "CNPJ": "19.320.060/0001-10"},

    # OBRAS E SERVIÇOS (Master Projetos e AMX)
    {"Data": "2025-02-25", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 77350.00, "Categoria": "Obras/Serviços", "CNPJ": "46.523.623/0001-40"},
    {"Data": "2025-07-30", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 46900.00, "Categoria": "Obras/Serviços", "CNPJ": "46.523.623/0001-40"},
    {"Data": "2025-09-29", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 46900.00, "Categoria": "Obras/Serviços", "CNPJ": "46.523.623/0001-40"},
    {"Data": "2025-09-30", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 77350.00, "Categoria": "Obras/Serviços", "CNPJ": "46.523.623/0001-40"},
    {"Data": "2025-10-30", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 46900.00, "Categoria": "Obras/Serviços", "CNPJ": "46.523.623/0001-40"},
    {"Data": "2025-03-21", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Obras/Serviços", "CNPJ": "21.238.834/0001-00"},
    {"Data": "2025-06-26", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Obras/Serviços", "CNPJ": "21.238.834/0001-00"},
    {"Data": "2025-08-29", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Obras/Serviços", "CNPJ": "21.238.834/0001-00"},
    {"Data": "2025-10-30", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Obras/Serviços", "CNPJ": "21.238.834/0001-00"},

    # PESSOAS FÍSICAS (Amostragem)
    {"Data": "2025-09-19", "Favorecido": "DAVID MEDEIROS DE CASTRO", "Valor": 6760.00, "Categoria": "Pagamentos PF (Folha?)", "CNPJ": "-"},
    {"Data": "2025-09-19", "Favorecido": "MIGUEL DA COSTA MIRANDA", "Valor": 6300.00, "Categoria": "Pagamentos PF (Folha?)", "CNPJ": "-"},
    {"Data": "2025-09-24", "Favorecido": "WENDREL LOPES RIBEIRO", "Valor": 1260.00, "Categoria": "Pagamentos PF (Folha?)", "CNPJ": "-"},
    {"Data": "2025-05-06", "Favorecido": "LARISSA REIS DE FARIAS", "Valor": 5450.00, "Categoria": "Pagamentos PF (Folha?)", "CNPJ": "-"},
]

df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data'])
df['Mês'] = df['Data'].dt.strftime('%Y-%m')

# --- CABEÇALHO E ALERTA ---
st.title("🚨 Raio-X dos Royalties: Nhamundá 2025")
st.markdown("""
> **A Lei 12.858/2013 determina:** 75% dos Royalties para **Educação** e 25% para **Saúde**.
>
> Abaixo, analisamos a destinação real dos recursos declarados como "Despesas Diversas".
""")

st.divider()

# --- CÁLCULOS CRÍTICOS ---
total_analisado = df['Valor'].sum()
# Nestes documentos, não identificamos verbas claras para Educação/Saúde nas "Diversas"
total_educacao_saude = 0 
total_outros = total_analisado

# --- VISUALIZAÇÃO 1: O TERMÔMETRO DA LEI (KPIs) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total em 'Despesas Diversas'", value=f"R$ {total_analisado:,.2f}")

with col2:
    st.metric(
        label="Investimento Visível em Saúde/Educação", 
        value=f"R$ {total_educacao_saude:,.2f}",
        delta="-100% (Desvio da Lei)",
        delta_color="inverse"
    )

with col3:
    st.metric(
        label="Gasto com Jurídico, Obras e Pessoal", 
        value=f"R$ {total_outros:,.2f}",
        delta="Destinação Questionável",
        delta_color="off"
    )

st.divider()

# --- VISUALIZAÇÃO 2: PARA ONDE FOI O DINHEIRO (TREEMAP) ---
st.subheader("💸 Onde o dinheiro foi parar (em vez da Educação)")
st.caption("Tamanho do bloco representa o volume de dinheiro gasto.")

fig_tree = px.treemap(
    df, 
    path=['Categoria', 'Favorecido'], 
    values='Valor',
    color='Categoria',
    color_discrete_map={
        'Consultoria Jurídica/Adm': '#EF553B', # Vermelho
        'Advocacia Terceirizada': '#EF553B',   # Vermelho
        'Obras/Serviços': '#FFA15A',           # Laranja
        'Pagamentos PF (Folha?)': '#FFD700'    # Amarelo
    }
)
fig_tree.update_layout(margin = dict(t=0, l=0, r=0, b=0))
st.plotly_chart(fig_tree, use_container_width=True)

# --- VISUALIZAÇÃO 3: EVOLUÇÃO TEMPORAL (CONSULTORIA) ---
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("📈 A 'Mesada' da Consultoria")
    st.caption("Evolução dos pagamentos apenas para Consultoria e Advocacia.")
    
    df_juridico = df[df['Categoria'].str.contains("Jurídica|Advocacia")]
    df_juridico_agg = df_juridico.groupby('Mês')['Valor'].sum().reset_index()
    
    fig_line = px.bar(
        df_juridico_agg, 
        x='Mês', 
        y='Valor', 
        text_auto='.2s',
        color_discrete_sequence=['#EF553B']
    )
    fig_line.update_layout(yaxis_title="Valor Pago (R$)")
    st.plotly_chart(fig_line, use_container_width=True)

with col_chart2:
    st.subheader("🏗️ Obras vs. Pessoal")
    st.caption("Comparativo de fluxo de caixa para outras categorias.")
    
    df_outros = df[~df['Categoria'].str.contains("Jurídica|Advocacia")]
    
    fig_bar = px.bar(
        df_outros, 
        x='Categoria', 
        y='Valor', 
        color='Favorecido',
        title="Quem recebeu fora do Jurídico?"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# --- TABELA DE DADOS DETALHADA ---
st.divider()
st.subheader("🔎 Auditoria Cidadã: Pesquise os Detalhes")

texto_busca = st.text_input("Digite o nome de uma empresa ou pessoa:", placeholder="Ex: Gustavo, Master, Nunes...")

if texto_busca:
    df_display = df[df['Favorecido'].str.contains(texto_busca, case=False)]
else:
    df_display = df

st.dataframe(
    df_display[['Data', 'Favorecido', 'CNPJ', 'Categoria', 'Valor']].sort_values(by='Data', ascending=False),
    use_container_width=True,
    hide_index=True
)

st.markdown("""
---
*Fonte dos Dados: Portal da Transparência / Diário Oficial de Nhamundá (2025). Análise automatizada baseada em documentos públicos.*
""")
