import streamlit as st
title_page_web='¡Confía!' #Título del Dashboard
st.set_page_config(page_title = title_page_web, #Nombre de la pagina, sale arriba cuando se carga streamlit
                   page_icon = '💖', # https://www.webfx.com/tools/emoji-cheat-sheet/
                   layout="wide")

def main():
    st.title("EL AMOR NO ES UN JUEGO, Y TÚ TAMPOCO 💖")

    # Carga y muestra la imagen

    col1, col2, col3 = st.columns([2,1.8,2]) #Centrar el botón
    with col1:
        # Dibuja un corazón con destello
        st.markdown(
            """<svg height="200" width="200" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 187.5 C10 100, 10 60, 100 10 C190 60, 190 100, 100 187.5" fill="red" />
                <text x="50%" y="50%" font-size="24" text-anchor="middle" fill="white" font-style="italic">G&S</text>
            </svg>
            <style>
                svg {
                    animation: pulse 2s infinite;
                }
                @keyframes pulse {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.2); }
                    100% { transform: scale(1); }
                }
            </style>""",
            unsafe_allow_html=True
        )
    with col2:
        st.image("Imagen1.jpg", use_column_width=True, width=None)

    with col3:
        st.image("Imagen.jpg", use_column_width=True, width=None)
    

    # Muestra el texto adicional en el interior del corazón
    st.markdown(
        """<p style='font-size:24px; font-style:italic; text-align:center;'>
            Confía en todo lo que planeamos<br>
            y a seguir para adelante
        </p>""",
        unsafe_allow_html=True
    )

    # Agrega un enlace para descargar la música
    st.audio("Music.mp3", format="audio/mp3", start_time=0)

if __name__ == "__main__":
    main()
