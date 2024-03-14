from PIL import Image


# Função para inverter verticalmente a imagem pixel a pixel
def inverter_verticalmente(imagem):
    largura, altura = imagem.size
    imagem_processada = Image.new("RGB", (largura, altura))
    pixels = imagem.load()
    pixels_processados = imagem_processada.load()

    for x in range(largura):
        for y in range(altura):
            # Obter o valor do pixel correspondente na posição invertida verticalmente
            pixel_invertido = pixels[x, altura - y - 1]

            # Copiar o pixel invertido para a imagem processada
            pixels_processados[x, y] = pixel_invertido

    return imagem_processada
