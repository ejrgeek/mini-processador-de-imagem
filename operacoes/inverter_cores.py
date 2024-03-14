from PIL import Image


# Função para inverter as cores da imagem pixel a pixel
def inverter_cores(imagem):
    largura, altura = imagem.size
    imagem_processada = Image.new("RGB", (largura, altura))
    pixels = imagem.load()
    pixels_processados = imagem_processada.load()

    for x in range(largura):
        for y in range(altura):
            r, g, b = pixels[x, y]
            r = 255 - r
            g = 255 - g
            b = 255 - b
            pixels_processados[x, y] = (r, g, b)

    return imagem_processada
