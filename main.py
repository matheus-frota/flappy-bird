import pygame
import os
import random
import neat

from src.utils import desenhar_tela
from src.constants import (LARGURA, ALTURA)
from src.passaro import Passaro
from src.cano import Cano
from src.chao import Chao

ai_jogando = True
geracao = 0
melhor_pontuacao = {}


def main(genomas, config):
    global geracao, melhor_pontuacao
    if ai_jogando:
        geracao += 1
        melhor_pontuacao[geracao] = 0
        pontos = []
        redes = []
        lista_genomas = []
        passaros = []
        for _, genoma in genomas:
            rede = neat.nn.FeedForwardNetwork.create(genoma, config)
            redes.append(rede)
            genoma.fitness = 0
            lista_genomas.append(genoma)
            passaros.append(Passaro(230, 350))
            pontos.append(0)
    else:
        passaros = [Passaro(230, 350)]
        pontos = 0
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    relogio = pygame.time.Clock()
    rodando = True
    while rodando:
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()

            if not ai_jogando:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        [passaro.pular() for passaro in passaros]
        indice_cano = 0
        if len(passaros) > 0:
            if len(canos) > 1 and passaros[0].x > (
                    canos[0].x + canos[0].cano_topo.get_width()):
                indice_cano = 1
        else:
            rodando = False
            break

        for i, passaro in enumerate(passaros):
            passaro.mover()
            lista_genomas[i].fitness += 0.1
            output = redes[i].activate(
                (passaro.y, abs(passaro.y - canos[indice_cano].pos_topo),
                 abs(passaro.y - canos[indice_cano].pos_base)))

            if output[0] > 0.5:
                passaro.pular()

        [passaro.mover() for passaro in passaros]

        chao.mover()

        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                    if ai_jogando:
                        lista_genomas[i].fitness -= 1
                        lista_genomas.pop(i)
                        redes.pop(i)
                        pontos.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
            cano.mover()
            if cano.x + cano.cano_topo.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            canos.append(Cano(600))
            if ai_jogando:
                for i, genoma in enumerate(lista_genomas):
                    genoma.fitness += 1
                    pontos[i] = pontos[i] + 1
                if len(passaros) > 0:
                    melhor_pontuacao[geracao] = max(pontos)
            else:
                pontos += 1
        [canos.remove(cano) for cano in remover_canos]

        for i, passaro in enumerate(passaros):
            if (passaro.y +
                    passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                passaros.pop(i)
                if ai_jogando:
                    lista_genomas.pop(i)
                    redes.pop(i)
        if ai_jogando:
            desenhar_tela(tela, passaros, canos, chao, pontos, geracao, ai_jogando, melhor_pontuacao)
        else:
            desenhar_tela(tela, passaros, canos, chao, pontos, geracao, ai_jogando)

def rodar(caminho='./config.txt'):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                caminho)

    populacao = neat.Population(config)
    populacao.add_reporter(neat.StdOutReporter(True))
    populacao.add_reporter(neat.StatisticsReporter())
    if ai_jogando:
        populacao.run(main)
    else:
        main(None, None)


if __name__ == '__main__':
    rodar()
