import pygame as pg

from constantes import COR_BRANCA


class Seta:
    """
    Desenha o indicador do botão selecionado
    """

    def __init__(self, tamanho=20, cor=COR_BRANCA):
        self.cor = cor
        self.tamanho = tamanho

        # Criar superficie uma unica vez para poupar recursos
        self.imagem = pg.Surface((tamanho, tamanho), pg.SRCALPHA)

        # Cria triângulo
        pontos = [(0, 0), (0, tamanho), (tamanho, tamanho // 2)]
        pg.draw.polygon(self.imagem, self.cor, pontos)

    def desenhar(self, tela, pos_x, pos_y):
        """Desenha a seta na posição especificada"""
        tela.blit(self.imagem, (pos_x, pos_y))
class Seta_baixo:
    def __init__(self, cor=COR_BRANCA, tamanho=20):
        self.cor = cor
        self.tamanho = tamanho

        # Criar superficie uma unica vez para poupar recursos
        self.imagem = pg.Surface((tamanho, tamanho), pg.SRCALPHA)

        # Cria triângulo
        pontos = [(0, 0), (tamanho,0), (tamanho // 2, tamanho)]
        pg.draw.polygon(self.imagem, self.cor, pontos)

    def desenhar(self, tela, pos_x, pos_y):
        """Desenha a seta na posição especificada"""
        tela.blit(self.imagem, (pos_x, pos_y))