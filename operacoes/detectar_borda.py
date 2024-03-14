from PIL import Image


# Função para detectar borda na imagem pixel a pixel
def detectar_borda(imagem):
    largura, altura = imagem.size
    imagem_processada = Image.new(
        "L", (largura, altura)
    )  # Modo "L" para imagem em escala de cinza
    pixels = imagem.load()
    pixels_processados = imagem_processada.load()

    # Kernel de Sobel para detecção de borda
    kernel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    kernel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    for x in range(largura):
        for y in range(altura):
            gradient_x = 0
            gradient_y = 0

            # Aplica a convolução utilizando o kernel de Sobel
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < largura and 0 <= y + j < altura:
                        # Calcula o gradiente nas direções x e y
                        pixel = pixels[x + i, y + j]
                        gradient_x += (
                            kernel_x[i + 1][j + 1] * pixel[0]
                        )  # Componente R do pixel
                        gradient_y += (
                            kernel_y[i + 1][j + 1] * pixel[0]
                        )  # Componente R do pixel

            # Calcula a magnitude do gradiente
            magnitude = int((gradient_x**2 + gradient_y**2) ** 0.5)

            # Define o valor da magnitude no pixel processado
            pixels_processados[x, y] = magnitude

    return imagem_processada
