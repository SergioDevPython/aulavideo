import streamlit as st


# Configuração da página
st.set_page_config(page_title="Vídeo Aulas", page_icon=":clapper:", layout="wide")

# Mensagem inicial
st.warning("Por favor, procure o instrumento que você está aprendendo.")


# Título da aplicação
st.title("Vídeo Aulas")

# Dados das videoaulas
videos = [
    {"titulo": "CAIXA - Série Rítmica I para Iniciantes", "link": "https://www.youtube.com/watch?v=DkxnqK6gsVU", "descricao": "Como rufar caixa."},
    {"titulo": "CAIXA - Série Rítmica II para Iniciantes", "link": "https://www.youtube.com/watch?v=gs9bhlS_vF8", "descricao": "Exercícios de iniciação ao ritmo na caixa."},
    {"titulo": "GRUPO - Percussão, Prática em grupo ritmo: SENTA LEVANTA", "link": "https://www.youtube.com/watch?v=R97KiN0kJ94", "descricao": "Prática em grupo: SURDO, CAIXA E PRATOS."},
    {"titulo": "BUMBO - Percussão BUMBO", "link": "https://www.youtube.com/watch?v=I39EG_oRNiQ", "descricao": "Exercícios para BUMBO."},
    {"titulo": "PRATOS - Série Rítmica", "link": "https://www.youtube.com/watch?v=07tN0ghJZAU", "descricao": "Introdução à prática com pratos."},
    {"titulo": "TROMPETE - Aula I", "link": "https://www.youtube.com/watch?v=VjqgWwVNFUs", "descricao": "Aprenda os conceitos básicos sobre o trompete."},
    {"titulo": "TROMPETE - Tocando DO, RÉ, MI, FA, SOL", "link": "https://www.youtube.com/watch?v=AD-weQlmMkE", "descricao": "Tocando as notas Dó-Ré-Mi-Fá-Sol no Trompete Bb."},
    {"titulo": "EMBOCADURA - trompete, tuba, trombone, bombardino", "link": "https://www.youtube.com/watch?v=GJVBdwKrFOQ", "descricao": "Como fazer EMBOCADURA PERFEITA | trompete, tuba, trombone, bombardino."},
    {"titulo": "BOMBARDINO - Escala de Dó", "link": "https://www.youtube.com/watch?v=5ZX5Ec16bZM", "descricao": "Escala de Dó maior no Bombardino."},
]

# Função para exibir vídeos
st.subheader("Vídeos")

def exibir_videos(videos):
    num_videos = len(videos)
    cols = st.columns(2)  # Dividindo a interface em 3 colunas

    for i, video in enumerate(videos):
        col = cols[i % 2]  # Alterna entre as 3 colunas
        with col:
            if st.button(video["titulo"], key=f"btn_{i}"):
                st.session_state["video_selecionado"] = video
            st.caption(video["descricao"])

# Exibir vídeos em miniaturas
if "video_selecionado" not in st.session_state:
    st.session_state["video_selecionado"] = None

if st.session_state["video_selecionado"] is None:
    exibir_videos(videos)
else:
    video = st.session_state["video_selecionado"]
    st.video(video["link"])
    st.subheader(video["titulo"])
    st.caption(video["descricao"])

    if st.button("Voltar"):
        st.session_state["video_selecionado"] = None



