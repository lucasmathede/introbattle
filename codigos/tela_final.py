from botao import *
from seta import *
class Tela_final:
    def __init__(self, opcoes_texto, fonte, resultado = (None), pos_inicial=(500, 300), espacamento=100):
        self.botoes = [] # Lista com os botões da tela
        self.selecionado_index = 0 # Para saber qual botão deve ser exibido com cor diferente e onde a seta deve estar
        self.seta = Seta()
        self.resultado = resultado
        self.imagemx =  650
        self.espacamento2 = 250
        x, y = pos_inicial

        # Cria os botões e salva na lista de botões
        for texto in opcoes_texto:
            botao = Botao(texto, (x, y), fonte)
            self.botoes.append(botao)
            y += espacamento
        self.superficie_vitoria = fonte.render('Vitória',True,COR_BRANCA)
        self.superficie_derrota = fonte.render('Derrota',True,COR_BRANCA)
        self.superficie_duvida = fonte.render('Quer tentar novamente?',True,COR_BRANCA)

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
        espacamentox = 200
        x = 650
        tela.fill(COR_PRETA)
        if self.resultado is not None:
            if self.resultado:
                tela.blit(self.superficie_vitoria,(500,60))
            else:
                tela.blit(self.superficie_derrota,(500,60))
        tela.blit(self.superficie_duvida,(300,120))
        

        for i, botao in enumerate(self.botoes): # Itera com indíce e botão
          esta_ativo = i == self.selecionado_index
          botao.desenhar(tela, esta_ativo)

          if esta_ativo:
            altura_seta = botao.get_altura_centro() - (self.seta.tamanho // 2)
            self.seta.desenhar(tela, botao.pos[0] - 30, altura_seta - 45)
    def reiniciar(self):
        self.selecionado_index = 0