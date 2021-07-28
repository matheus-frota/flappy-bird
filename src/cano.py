import pygame
import random

from src.constants import (IMAGEM_CANO, DISTANCIA_CANO, VELOCIDADE_CANO)


class Cano:

    def __init__(self, x):
        self.x = x
        self.altura_cano = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.cano_base = IMAGEM_CANO
        self.cano_topo = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.passou = False
        self.definir_altura()

    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.cano_topo.get_height()
        self.pos_base = self.altura + DISTANCIA_CANO

    def mover(self):
        self.x -= VELOCIDADE_CANO

    def desenhar(self, tela):
        tela.blit(self.cano_topo, (self.x, self.pos_topo))
        tela.blit(self.cano_base, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.cano_topo)
        base_mask = pygame.mask.from_surface(self.cano_base)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
        base_ponto = passaro_mask.overlap(base_mask, distancia_base)

        if base_ponto or topo_ponto:
            return True
        else:
            return False
