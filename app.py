from PIL import Image
import streamlit as st

from operacoes import *


# Função principal
def main():
    # Título e descrição da aplicação
    st.title("Operações simples em Imagens")
    st.write(
        "Envie uma imagem e selecione as opções de processamento na barra lateral."
    )

    # Carregar a imagem
    imagem = st.sidebar.file_uploader(
        "Selecione uma imagem", type=["jpg", "jpeg", "png"]
    )

    if imagem is not None:
        # Carregar a imagem usando o Pillow
        imagem_pil = Image.open(imagem)

        # Redimensionar a imagem proporcionalmente
        tamanho_redimensionado = st.sidebar.slider("Redimensionar", 100, 1000, 500)
        imagem_pil = redimensionar_imagem(imagem_pil, tamanho_redimensionado)

        # Inverter as cores
        inverter_cores_checkbox = st.sidebar.checkbox("Inverter Cores")
        if inverter_cores_checkbox:
            imagem_pil = inverter_cores(imagem_pil)

        # Aplicar detecção de borda
        deteccao_borda_checkbox = st.sidebar.checkbox("Detecção de Borda")
        if deteccao_borda_checkbox:
            imagem_pil = detectar_borda(imagem_pil)

        # Rotacionar a imagem
        angulo_rotacao = st.sidebar.slider("Ângulo de Rotação", -180, 180, 0)
        imagem_pil = rotacionar_imagem(imagem_pil, angulo_rotacao)

        # Inverter horizontalmente
        inverter_horizontalmente_checkbox = st.sidebar.checkbox(
            "Inverter Horizontalmente"
        )
        if inverter_horizontalmente_checkbox:
            imagem_pil = inverter_horizontalmente(imagem_pil)

        # Inverter verticalmente
        inverter_verticalmente_checkbox = st.sidebar.checkbox("Inverter Verticalmente")
        if inverter_verticalmente_checkbox:
            imagem_pil = inverter_verticalmente(imagem_pil)

        # Exibir a imagem processada
        st.image(imagem_pil)


# Executar a função principal
if __name__ == "__main__":
    main()
