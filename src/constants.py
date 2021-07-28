import pygame

# Tamanho da tela
LARGURA = 500
ALTURA = 800

# Imagens usada para o jogo
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load('./imgs/pipe.png'))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load('./imgs/base.png'))
IMAGEM_BACKGROUND = pygame.transform.scale2x(
    pygame.image.load('./imgs/bg.png'))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load('./imgs/bird1.png')),
    pygame.transform.scale2x(pygame.image.load('./imgs/bird2.png')),
    pygame.transform.scale2x(pygame.image.load('./imgs/bird3.png'))
]

# Fonte dos textos
pygame.font.init()

FONTE_PONTOS = pygame.font.SysFont('arial', 20)

# Constantes do pássaro
ROTACAO_MAXIMA = 25
VELOCIDADE_ROTACAO = 20
TEMPO_ANIMACAO = 5

# Constantes do cano
DISTANCIA_CANO = 200
VELOCIDADE_CANO = 10

# Constantes do chão
VELOCIDADE_CHAO = 5
LARGURA_CHAO = IMAGEM_CHAO.get_width()
