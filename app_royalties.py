import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Monitor de Royalties - Nhamundá",
    page_icon="💸",
    layout="wide"
)

# --- 1. DADOS REAIS EXTRAÍDOS DOS PDFS ---
# Adicionei os pagamentos de INSS que encontramos nos documentos
data_reais = [
    # --- JURÍDICO & CONSULTORIA ---
    {"Data": "2025-01-20", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 73727.56, "Categoria": "Consultoria Jurídica", "Grupo": "Jurídico"},
    {"Data": "2025-02-25", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 44695.49, "Categoria": "Consultoria Jurídica", "Grupo": "Jurídico"},
    {"Data": "2025-02-25", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 85483.74, "Categoria": "Consultoria Jurídica", "Grupo": "Jurídico"},
    {"Data": "2025-03-31", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 132391.24, "Categoria": "Consultoria Jurídica", "Grupo": "Jurídico"},
    {"Data": "2025-05-27", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 123333.82, "Categoria": "Consultoria Jurídica", "Grupo": "Jurídico"},
    {"Data": "2025-06-26", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 110124.55, "Categoria": "Consultoria Jurídica", "Grupo": "Jurídico"},
    {"Data": "2025-07-25", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 106306.11, "Categoria": "Consultoria Jurídica", "Grupo": "Jurídico"},
    {"Data": "2025-08-28", "Favorecido": "GUSTAVO FREITAS MACEDO", "Valor": 106515.92, "Categoria": "Consultoria Jurídica", "Grupo": "Jurídico"},
    
    {"Data": "2025-02-25", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 34540.28, "Categoria": "Advocacia", "Grupo": "Jurídico"},
    {"Data": "2025-03-31", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 52359.23, "Categoria": "Advocacia", "Grupo": "Jurídico"},
    {"Data": "2025-06-26", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 74494.81, "Categoria": "Advocacia", "Grupo": "Jurídico"},
    {"Data": "2025-07-30", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 74545.29, "Categoria": "Advocacia", "Grupo": "Jurídico"},
    {"Data": "2025-08-29", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 74563.46, "Categoria": "Advocacia", "Grupo": "Jurídico"},
    {"Data": "2025-09-26", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 75331.69, "Categoria": "Advocacia", "Grupo": "Jurídico"},
    {"Data": "2025-10-30", "Favorecido": "NUNES GOLGO SOCIEDADE DE ADVOGADOS", "Valor": 76553.74, "Categoria": "Advocacia", "Grupo": "Jurídico"},

    # --- INFRAESTRUTURA ---
    {"Data": "2025-02-25", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 77350.00, "Categoria": "Obras", "Grupo": "Infraestrutura"},
    {"Data": "2025-07-30", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 46900.00, "Categoria": "Obras", "Grupo": "Infraestrutura"},
    {"Data": "2025-09-29", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 46900.00, "Categoria": "Obras", "Grupo": "Infraestrutura"},
    {"Data": "2025-09-30", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 77350.00, "Categoria": "Obras", "Grupo": "Infraestrutura"},
    {"Data": "2025-10-30", "Favorecido": "MASTER PROJETOS DA CONSTRUÇÃO LTDA", "Valor": 46900.00, "Categoria": "Obras", "Grupo": "Infraestrutura"},
    
    {"Data": "2025-03-21", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Locação/Serviços", "Grupo": "Infraestrutura"},
    {"Data": "2025-06-26", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Locação/Serviços", "Grupo": "Infraestrutura"},
    {"Data": "2025-08-29", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Locação/Serviços", "Grupo": "Infraestrutura"},
    {"Data": "2025-10-30", "Favorecido": "CONSTRUÇÃO AMX LTDA", "Valor": 72500.00, "Categoria": "Locação/Serviços", "Grupo": "Infraestrutura"},

    # --- INSS E ENCARGOS (O Ponto Crítico) ---
    {"Data": "2025-05-27", "Favorecido": "INSS - PREVIDÊNCIA SOCIAL", "Valor": 100000.00, "Categoria": "Dívida Previdenciária", "Grupo": "Desvio de Finalidade (INSS)"},
    {"Data": "2025-07-23", "Favorecido": "INSS - PREVIDÊNCIA SOCIAL", "Valor": 135441.79, "Categoria": "Dívida Previdenciária", "Grupo": "Desvio de Finalidade (INSS)"},
    {"Data": "2025-09-24", "Favorecido": "INSS - PREVIDÊNCIA SOCIAL", "Valor": 103603.56, "Categoria": "Dívida Previdenciária", "Grupo": "Desvio de Finalidade (INSS)"},
    {"Data": "2025-10-29", "Favorecido": "INSS - PREVIDÊNCIA SOCIAL", "Valor": 112772.55, "Categoria": "Dívida Previdenciária", "Grupo": "Desvio de Finalidade (INSS)"},
    {"Data": "2025-06-25", "Favorecido": "INSS - PREVIDÊNCIA SOCIAL", "Valor": 80000.00, "Categoria": "Dívida Previdenciária", "Grupo": "Desvio de Finalidade (INSS)"},
    {"Data": "2025-02-25", "Favorecido": "RECEITA FEDERAL DO BRASIL", "Valor": 32901.49, "Categoria": "Tributos", "Grupo": "Desvio de Finalidade (INSS)"},

    # --- PESSOAS FÍSICAS (Amostra) ---
    {"Data": "2025-09-19", "Favorecido": "DAVID MEDEIROS DE CASTRO", "Valor": 6760.00, "Categoria": "Pessoal PF", "Grupo": "Pessoas Físicas"},
    {"Data": "2025-09-19", "Favorecido": "MIGUEL DA COSTA MIRANDA", "Valor": 6300.00, "Categoria": "Pessoal PF", "Grupo": "Pessoas Físicas"},
    {"Data": "2025-05-06", "Favorecido": "LARISSA REIS DE FARIAS", "Valor": 5450.00, "Categoria": "Pessoal PF", "Grupo": "Pessoas Físicas"},
]

# Calculando o buraco para chegar aos 5 Milhões reais dos PDFs
total_amostra = sum([d['Valor'] for d in data_reais])
total_real_pdfs = 4975746.35 # Soma dos rodapés dos PDFs
diferenca_pulverizada = total_real_pdfs - total_amostra

# Adicionando o restante
data_reais.append({
    "Data": "2025-10-31", 
    "Favorecido": "DIVERSOS (Centenas de Pagamentos Menores)", 
    "Valor": diferenca_pulverizada, 
    "Categoria": "Pulverizado", 
    "Grupo": "Outros/Pulverizado"
})

df = pd.DataFrame(data_reais)

# --- CABEÇALHO ---
st.title("👁️ Monitoramento: Royalties Nhamundá 2025")
st.markdown(f"""
**Total Analisado (Jan-Out/2025):** R$ {total_real_pdfs:,.2f}
\n
Este painel detalha o destino dos recursos classificados genericamente como "Despesas Diversas",
evidenciando o contraste com a obrigatoriedade legal de investimento em **Saúde (25%)** e **Educação (75%)**.
""")
st.divider()

# --- GRÁFICO 1: PIZZA DOS GRUPOS ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Para onde foi o dinheiro?")
    fig_pie = px.pie(
        df, 
        values='Valor', 
        names='Grupo',
        color='Grupo',
        color_discrete_map={
            'Jurídico': '#FF4B4B',        # Vermelho
            'Desvio de Finalidade (INSS)': '#555555', # Cinza Escuro (Dívida)
            'Infraestrutura': '#FFA15A',  # Laranja
            'Pessoas Físicas': '#F9CE1D', # Amarelo
            'Outros/Pulverizado': '#E0E0E0' # Cinza Claro
        },
        hole=0.4
    )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.markdown("### Pontos de Atenção")
    st.error("""
    **Dívida Previdenciária (INSS):**
    Identificamos pagamentos diretos de guias do INSS e Receita Federal com recursos de Royalties.
    Isso caracteriza **Desvio de Finalidade**, pois a verba deveria ser para investimento, não dívida.
    """)
    st.warning("""
    **Alto Custo Jurídico:**
    Os valores pagos a consultorias jurídicas superam, em muitos meses, os investimentos físicos visíveis.
    """)

# --- GRÁFICO 2: RANKING ---
st.markdown("---")
st.subheader("🏆 Ranking dos Maiores Recebedores")

# Filtrar para não mostrar o aglomerado "Diversos" no ranking nominal
df_ranking = df[df['Favorecido'] != "DIVERSOS (Centenas de Pagamentos Menores)"]
df_ranking_agg = df_ranking.groupby(['Favorecido', 'Grupo'])['Valor'].sum().reset_index().sort_values('Valor', ascending=True)

fig_bar = px.bar(
    df_ranking_agg,
    x='Valor',
    y='Favorecido',
    orientation='h',
    color='Grupo',
    text_auto='.2s',
    color_discrete_map={
        'Jurídico': '#FF4B4B',
        'Desvio de Finalidade (INSS)': '#555555',
        'Infraestrutura': '#FFA15A',
        'Pessoas Físicas': '#F9CE1D'
    }
)
st.plotly_chart(fig_bar, use_container_width=True)

# --- TABELA DE BUSCA ---
st.markdown("---")
st.subheader("🔎 Pesquisa Detalhada")

busca = st.text_input("Buscar por Favorecido:", placeholder="Digite INSS, Gustavo, Master...")

if busca:
    df_show = df[df['Favorecido'].str.contains(busca, case=False)]
else:
    df_show = df[df['Favorecido'] != "DIVERSOS (Centenas de Pagamentos Menores)"]

st.dataframe(
    df_show[['Data', 'Favorecido', 'Grupo', 'Categoria', 'Valor']].sort_values(by='Data', ascending=False),
    use_container_width=True,
    hide_index=True
)
