import pygame as pg
from botao import *
from seta import Seta_baixo
class Selecao:
    def __init__(self,opcoes_personagens,pos_inicial2=(30,100),espacamentox=(250),espacamentoy=(500)):
        self.botao_imagem = [] #Lista com opções de personagens
        self.selecionado_index = 0
        self.opcoes_personagens = opcoes_personagens
        x,y = pos_inicial2
        x_reserva = pos_inicial2[0] #Guarda o valor de x para uso futuro
        self.seta = Seta_baixo()
        self.total_selecionados = 0
        self.escolhido = []

        #Cria os botões com imagem e salva na lista
        for personagem in opcoes_personagens:
            if len(self.botao_imagem) < len(opcoes_personagens)//2:
                botao = Botao_imagem(personagem.imagem,(x+10,y+25))
                self.botao_imagem.append(botao)
                x += espacamentox
            else:
                botao = Botao_imagem(personagem.imagem,(x_reserva+10,y+50+espacamentoy))
                self.botao_imagem.append(botao)
                x_reserva += espacamentox
    def atualizar(self,evento):
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_UP:
                self.selecionado_index =  (self.selecionado_index - len(self.botao_imagem)//2) % len(self.botao_imagem)
            elif evento.key == pg.K_DOWN:
                self.selecionado_index =  (self.selecionado_index + len(self.botao_imagem)//2) % len(self.botao_imagem)
            elif evento.key == pg.K_LEFT:
                if not self.selecionado_index == 0 or not self.selecionado_index == len(self.botao_imagem)//2:
                    self.selecionado_index = (self.selecionado_index - 1) % len(self.botao_imagem)
                else:
                    self.selecionado_index = (self.selecionado_index + (len(self.botao_imagem)//2 - 1)) % len(self.botao_imagem)
            elif evento.key == pg.K_RIGHT:
                if not self.selecionado_index == len(self.botao_imagem) - 1 or not self.selecionado_index == len(self.botao_imagem)//2 - 1:
                    self.selecionado_index = (self.selecionado_index + 1) % len(self.botao_imagem)
                else:
                    self.selecionado_index = (self.selecionado_index - 2) % len(self.botao_imagem)
            # Marca os personagens selecionados e limita o máximo como 3         
            elif evento.key == pg.K_RETURN:
                if self.botao_imagem[self.selecionado_index].marcado == 0 and self.total_selecionados < 3:
                    self.botao_imagem[self.selecionado_index].marcado += 1
                    self.total_selecionados += 1
                elif self.botao_imagem[self.selecionado_index].marcado == 1:
                    self.botao_imagem[self.selecionado_index].marcado -= 1
                    self.total_selecionados -= 1
                    
            elif evento.key == pg.K_z and self.total_selecionados == 3:
                return 1
        return None
    def reiniciar(self):
        self.selecionado_index = 0
        self.total_selecionados = 0
        for botao in self.botao_imagem:
            botao.marcado = 0
        self.escolhido = []

    def desenhar(self, tela):
        """Desenha Botões com personagens"""
        tela.fill(COR_PRETA)

        for i, botao in enumerate(self.botao_imagem): # Itera com indíce e botão
            esta_ativo = i == self.selecionado_index
            botao.desenhar2(tela, esta_ativo)
            if esta_ativo:
                altura_seta = botao.get_largura_centro() - (self.seta.tamanho // 2)
                self.seta.desenhar(tela, altura_seta , botao.pos[1] - 30)
    def escolhidos(self):
        if self.escolhido == []:
            for i,opcao in enumerate(self.botao_imagem):
                if opcao.marcado == 1:
                    for n,personagem in enumerate(self.opcoes_personagens):
                        if n == i:
                            self.escolhido.append(personagem)
            return self.escolhido
        else:
            return self.escolhido