import streamlit as st
import streamlit.components.v1 as components

# Configuração da página
st.set_page_config(page_title="Vídeo Aulas", page_icon=":clapper:", layout="wide")
components.iframe("https://www.youtube.com/embed/liC49Dol6OY?si=2VsirqJsLrPdGi87&amp;controls=0" , width=700, height=400)
# Mensagem inicial


st.title("🎶 Bem-vindo ao Curso de  – Flauta Doce! 🎺🥁")  

st.write(  
    """É com grande alegria que recebemos você nesta jornada musical!  
    Aqui, você terá a oportunidade de aprender, evoluir e fazer parte de um grupo que valoriza a disciplina,  
    a harmonia e o trabalho em equipe.  



    **Bem-vindo à família da Rainha da Paz!** 🎵"""  
)  



# Título da aplicação
st.title("Vídeo Aulas")

# Dados das videoaulas
videos = [
    {"titulo": "Primeiros Passos", "link": "https://www.youtube.com/watch?v=KKk5vUA_NFg&t=716s", "descricao": ""},
    {"titulo": "Era uma vez uma Joaninha", "link": "https://www.youtube.com/watch?v=KPLienSo4_8&list=RDKPLienSo4_8&start_radio=1", "descricao": "Música infantil: Era uma vez uma Joaninha."},
    {"titulo": "Músicas fáceis", "link": "https://www.youtube.com/watch?v=KPLienSo4_8&list=RDKPLienSo4_8&start_radio=1", "descricao": "Musica fáceis para flauta doce."},
    {"titulo": "Borboletinha", "link": "https://www.youtube.com/watch?v=5jnBIx3H8EY&list=RD5jnBIx3H8EY&start_radio=1", "descricao": "Música borboletinha."},
    {"titulo": "Embocadura", "link": "https://www.youtube.com/watch?v=65OBxj0uzXE", "descricao": "Técnica de sopro na flauta doce"},
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



st.title("📞 Contatos")  

st.write(" Para mais informações :")  

st.markdown("""  
📧 **E-mail:** analista.sergiosantos@gmail.com  
📱 **WhatsApp:** +55 77 99921-1063  
📍 **Endereço:**   
🌐 **Site:** [www.fanfara.com.br](https://www.linkedin.com/in/sergio-santos-20391332a/)  
""")  

st.write("Nos siga nas redes sociais para ficar por dentro das novidades!")  

st.markdown("""  
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/sergiosantos230)  
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=facebook&logoColor=white)](https://facebook.com/fanfara)  
""")  
