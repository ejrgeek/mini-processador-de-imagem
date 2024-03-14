import math
from PIL import Image


# Função para rotacionar a imagem pixel a pixel
def rotacionar_imagem(imagem, angulo):
    largura, altura = imagem.size
    imagem_processada = Image.new("RGB", (largura, altura))
    pixels = imagem.load()
    pixels_processados = imagem_processada.load()

    centro_x = largura / 2
    centro_y = altura / 2

    # Converter o ângulo para radianos
    angulo_rad = math.radians(angulo)

    for x in range(largura):
        for y in range(altura):
            # Deslocar o ponto atual para o centro da imagem
            ponto_x = x - centro_x
            ponto_y = y - centro_y

            # Aplicar a rotação no ponto atual
            novo_x = (
                int(ponto_x * math.cos(angulo_rad) - ponto_y * math.sin(angulo_rad))
                + centro_x
            )
            novo_y = (
                int(ponto_x * math.sin(angulo_rad) + ponto_y * math.cos(angulo_rad))
                + centro_y
            )

            # Verificar se as coordenadas resultantes estão dentro dos limites da imagem
            if 0 <= novo_x < largura and 0 <= novo_y < altura:
                # Copiar o pixel da imagem original para a imagem processada
                pixels_processados[x, y] = pixels[novo_x, novo_y]
            else:
                # Preencher com a cor de fundo
                pixels_processados[x, y] = (255, 255, 255)  # Cor branca

    return imagem_processada
