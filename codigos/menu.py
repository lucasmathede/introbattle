import pygame as pg

from botao import Botao
from seta import Seta

class Menu:
  def __init__(self, img_fundo, opcoes_texto, fonte, pos_inicial=(100, 210), espacamento=120):
    self.img_fundo = img_fundo

    self.botoes = [] # Lista com os botões da tela
    self.selecionado_index = 0 # Para saber qual botão deve ser exibido com cor diferente e onde a seta deve estar
    self.seta = Seta()

    x, y = pos_inicial

    # Cria os botões e salva na lista de botões
    for texto in opcoes_texto:
      botao = Botao(texto, (x, y), fonte)
      self.botoes.append(botao)
      y += espacamento

  def atualizar(self, evento):
    """
    Gerencia a navegação do teclado
    Retorna o índice do botão selecionado
    """
    # O '% len(self.botoes)' faz com que se crie um ciclo
    # Ex: Apertar seta para cima no primeiro elemento faz ele ir para o último
    if evento.type == pg.KEYDOWN:
      if evento.key == pg.K_UP:
        self.selecionado_index = (self.selecionado_index - 1) % len(self.botoes)
      elif evento.key == pg.K_DOWN:
        self.selecionado_index = (self.selecionado_index + 1) % len(self.botoes)
      elif evento.key == pg.K_RETURN:
        return self.selecionado_index

    return None

  def desenhar(self, tela):
    """Desenha fundo, botões e seta"""
    tela.blit(self.img_fundo, (0, 0))

    for i, botao in enumerate(self.botoes): # Itera com indíce e botão
      esta_ativo = i == self.selecionado_index
      botao.desenhar(tela, esta_ativo)

      if esta_ativo:
        altura_seta = botao.get_altura_centro() - (self.seta.tamanho // 2)
        self.seta.desenhar(tela, botao.pos[0] - 30, altura_seta - 30)