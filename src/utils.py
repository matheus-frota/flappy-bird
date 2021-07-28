import pygame

from src.constants import (LARGURA, ALTURA, IMAGEM_BACKGROUND, FONTE_PONTOS)


def get_max_dict(dicio):
    key = max(dicio, key=dicio.get)
    value = dicio[key]
    return key, value


def desenhar_tela(tela, passaros, canos, chao, pontos, geracao, ai_jogando, melhor_pontuacao=False):
    tela.blit(IMAGEM_BACKGROUND, (0, 0))
    [passaro.desenhar(tela) for passaro in passaros]
    [cano.desenhar(tela) for cano in canos]

    if ai_jogando:
        g, max_pontuacao = get_max_dict(melhor_pontuacao)
        texto = FONTE_PONTOS.render(f"Pontuação: {max(pontos)}", 1, (255, 255, 255))
        tela.blit(texto, (LARGURA - 10 - texto.get_width(), 10))
        texto = FONTE_PONTOS.render(f"Geração: {geracao}", 1, (255, 255, 255))
        tela.blit(texto, (10, 10))
        texto = FONTE_PONTOS.render(f"Pássaros vivos: {len(passaros)}", 1, (255, 255, 255))
        tela.blit(texto, (10, 40))
        texto = FONTE_PONTOS.render(f"Melhor Resultado: Geração - {g} | Pontuação - {max_pontuacao}", 1, (255, 255, 255))
        tela.blit(texto, (10, 70))
    else:
        texto = FONTE_PONTOS.render(f"Pontuação: {pontos}", 1, (255, 255, 255))
        tela.blit(texto, (LARGURA - 10 - texto.get_width(), 10))

    chao.desenhar(tela)

    pygame.display.update()
