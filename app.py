import streamlit as st
from agent import perguntar_ao_agente


st.set_page_config(
    page_title="AuraMotors - Agente de IA",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Cabeçalho e explicação sucinta
st.markdown('<p class="main-header">🤖 AuraMotors S.A.</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Central Inteligente de Operações e Manutenção</p>', unsafe_allow_html=True)

with st.expander("ℹ️ Sobre este Agente de IA", expanded=True):
    st.write("""
    Assistente virtual corporativo para o chão de fábrica e gestão.
    Consulta em tempo real nossa base de conhecimento unificada contendo manuais técnicos (PDF),
    procedimentos operacionais (DOCX/MD), tabelas de estoque (CSV/XLSX), cadastros de fornecedores (JSON),
    apresentações de metas (PPTX) e políticas internas (HTML).
    """)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.write("**Sugestões de consultas rápidas:**")

# Lista com perguntas prontas baseadas nos documentos fictícios
perguntas_sugeridas = [
    "Qual o procedimento para o erro E-102 no robô KR-500?",
    "Qual o estoque atual do sensor indutivo?",
    "Quais são os fornecedores de fixadores e seus SLAs?",
    "Qual a regra da política de requisição de peças?"
]

# Exibição dos botões lado a lado
cols = st.columns(2)
pergunta_selecionada = None

for idx, pergunta in enumerate(perguntas_sugeridas):
    col = cols[idx % 2]
    if col.button(pergunta, key=f"btn_{idx}", use_container_width=True):
        pergunta_selecionada = pergunta

# 5. Exibição do histórico de conversa
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Captura da entrada (seja pelo campo de texto ou por um botão clicado)
prompt_usuario = st.chat_input("Digite sua dúvida sobre a fábrica...") or pergunta_selecionada

if prompt_usuario:
    # Adiciona e exibe a mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt_usuario})
    with st.chat_message("user"):
        st.markdown(prompt_usuario)

    # Processa e exibe a resposta do agente
    with st.chat_message("assistant"):
        with st.spinner("Consultando base de documentos..."):
            resposta = perguntar_ao_agente(prompt_usuario)
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})