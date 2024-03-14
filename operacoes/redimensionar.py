from PIL import Image


def redimensionar_imagem(imagem, tamanho):
    largura_original, altura_original = imagem.size
    proporcao = tamanho / max(largura_original, altura_original)
    nova_largura = round(largura_original * proporcao)
    nova_altura = round(altura_original * proporcao)

    nova_imagem = Image.new(imagem.mode, (nova_largura, nova_altura))
    pixels_nova_imagem = nova_imagem.load()

    pixels_imagem_original = imagem.load()
    for x in range(nova_largura):
        for y in range(nova_altura):
            pixel_original_x = round(x / proporcao)
            pixel_original_y = round(y / proporcao)
            pixels_nova_imagem[x, y] = pixels_imagem_original[
                pixel_original_x, pixel_original_y
            ]

    return nova_imagem
