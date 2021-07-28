import pygame

from src.constants import (IMAGEM_CHAO, VELOCIDADE_CHAO, LARGURA_CHAO)


class Chao:

    def __init__(self, y):
        self.y = y
        self.x0 = 0
        self.x1 = LARGURA_CHAO

    def mover(self):
        self.x0 -= VELOCIDADE_CHAO
        self.x1 -= VELOCIDADE_CHAO

        if self.x0 + LARGURA_CHAO < 0:
            self.x0 = self.x1 + LARGURA_CHAO

        if self.x1 + LARGURA_CHAO < 0:
            self.x1 = self.x0 + LARGURA_CHAO

    def desenhar(self, tela):
        tela.blit(IMAGEM_CHAO, (self.x0, self.y))
        tela.blit(IMAGEM_CHAO, (self.x1, self.y))
