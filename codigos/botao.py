# botao.py
import pygame as pg
from constantes import *

class Botao:
    def __init__(self, texto, pos, fonte): #def __init__(self, texto, pos):
        self.text = texto
        self.pos = pos
        self.rect = pg.rect.Rect(self.pos[0], self.pos[1], 280, 140)

        # Renderizamos apenas uma vez para poupar recurso
        # Melhor que renderizar todo frame
        self.surface_normal = fonte.render(texto, True, COR_BRANCA)
        self.surface_destaque = fonte.render(texto, True, COR_LARANJA)

    def desenhar(self, tela, selecionado):
        """Desenha o botão na tela"""
        # Verificação para exibir o botão com cores diferentes caso ele esteja selecionado
        # Apenas para dar um efeito visual de qual está selecionado
        if selecionado:
            tela.blit(self.surface_destaque, self.rect)
        else:
            tela.blit(self.surface_normal, self.rect)

    def checa_clique(self):
        """Checa se botão foi clicado com o mouse"""
        if self.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            return True
        else:
            return False

    def get_altura_centro(self):
        """Retorna o y centralizado para posicionar a seta corretamente"""
        return self.rect.centery
    def get_largura_centro(self):
        return self.rect.centerx
class Botao_imagem:
    def __init__(self,img , pos):
        self.img = img
        self.pos = pos
        self.rect = pg.Rect(self.pos[0],self.pos[1],130,175)
        #indica se o botão está selecionado
        self.marcado = 0
        self.total_marcado = 0
    def desenhar2(self,tela,selecionado):
        """ Desenha Botão com imagem na tela """
        # Verificação para exibir o botão com cores diferentes caso ele esteja selecionado
        # Apenas para dar um efeito visual de qual está selecionado
        if selecionado and self.marcado == 0:
            pg.draw.rect(tela,COR_LARANJA,self.rect)
            tela.blit(self.img,(self.pos[0]+5,self.pos[1]+5))
        elif self.marcado == 1:
            pg.draw.rect(tela,COR_VERDE,self.rect)
            tela.blit(self.img,(self.pos[0]+5,self.pos[1]+5))
        else:
            pg.draw.rect(tela,COR_PRETA,self.rect)
            tela.blit(self.img,(self.pos[0]+5 ,self.pos[1]+5))
    def get_largura_centro(self):
        """Retorna o x centralizado para posicionar a seta corretamente"""
        return self.rect.centerx