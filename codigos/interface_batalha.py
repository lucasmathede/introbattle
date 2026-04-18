from selecao import *
from botao import *
from seta import *
from personagem import *
class Interface:
    def __init__(self,img_fundo,personagens,inimigos,fonte,escolhidos=(None),pos_personagem=(100,80),pos_inimigos=(900,80),pos_botoes=(350,900),espacamentox=(125),espacamentoy=(250),espacamento_botaox = (300),espacamento_botaoy=(100)):
        self.img_fundo = img_fundo
        self.personagens = personagens
        self.inimigos = inimigos
        self.escolhidos = escolhidos
        self.fonte = fonte
        self.selecionado_index = 0
        self.seta = Seta()
        self.seta_baixo = Seta_baixo(COR_VERMELHO,30)
        self.pos_personagem = pos_personagem
        self.pos_inimigos = pos_inimigos
        x3,y3 = pos_botoes
        self.pos_botoes = pos_botoes
        self.turno = 0
        x_reserva = x3
        self.acoes_texto = ['Atacar','Defender','Info','Habilidade']
        self.acoes = []
        self.personagens_selecionados = []
        for texto in self.acoes_texto:
            if len(self.acoes) < len(self.acoes_texto)//2:
                botao = Botao(texto,(x3,y3),fonte)
                self.acoes.append(botao)
                x3 += espacamento_botaox
            else:
                botao = Botao(texto,(x_reserva,y3+espacamento_botaoy),fonte)
                self.acoes.append(botao)
                x_reserva += espacamento_botaox
    def atualizar(self, evento):
        """
        Gerencia a navegação do teclado
        Retorna o índice do botão selecionado
        """
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_UP:
                self.selecionado_index = (self.selecionado_index - len(self.acoes)//2) % len(self.acoes)
            elif evento.key == pg.K_DOWN:
                self.selecionado_index = (self.selecionado_index + len(self.acoes)//2) % len(self.acoes)
            elif evento.key == pg.K_LEFT:
                if not self.selecionado_index == 0 or not self.selecionado_index == len(self.acoes)//2:
                    self.selecionado_index = (self.selecionado_index - 1) % len(self.acoes)
                else:
                    self.selecionado_index = (self.selecionado_index + (len(self.acoes)//2 - 1)) % len(self.acoes)
            elif evento.key == pg.K_RIGHT:
                if not self.selecionado_index == len(self.acoes) - 1 or not self.selecionado_index == len(self.acoes)//2 - 1:
                    self.selecionado_index = (self.selecionado_index + 1) % len(self.acoes)
                else:
                    self.selecionado_index = (self.selecionado_index - 2) % len(self.acoes)
    def desenhar(self, tela):
        """Desenha Botões"""
        tela.blit(self.img_fundo,(0,-310))
        pg.draw.rect(tela,COR_LARANJA,((0,770), (1920,310)), 0)
        pg.draw.rect(tela,COR_CINZA,((5,775), (1910,300)), 0)
        pg.draw.rect(tela,COR_LARANJA,((1315,0),(605,310)),0)
        pg.draw.rect(tela,COR_CINZA,((1320,5),(595,300)),0)
        pg.draw.line(tela,COR_LARANJA,(1100,775),(1100,1080),10)
        x1,y1 = self.pos_personagem
        x2,y2 = self.pos_inimigos
        x3,y3 = (1360,30)
        x4,y4 = self.pos_botoes
        for i, botao in enumerate(self.acoes): # Itera com indíce e botão
            esta_ativo = i == self.selecionado_index
            botao.desenhar(tela, esta_ativo)
            if esta_ativo:
                altura_seta = botao.get_altura_centro() - (self.seta.tamanho)
                self.seta.desenhar(tela, botao.pos[0] - 30, altura_seta - 35)
        for i,personagem in enumerate(self.escolhidos):
            if i == self.turno:
                tela.blit(personagem.imagem,(75,790))
                tela.blit(self.fonte.render('Vez de {}'.format(personagem.nome),True,COR_BRANCA),(x4,y4 - 100))
        for personagem in self.escolhidos:
            tela.blit((self.fonte.render('{}: {}/{}'.format(personagem.nome,personagem.vida_atual,personagem.vida_max),True,COR_BRANCA)),(x4+800,y4-100))
            y4 += 100
        for i,personagem in enumerate(self.escolhidos):
            tela.blit(pg.transform.scale(personagem.imagem,(140,250)),(x1,y1))
            if i == self.turno:
                # largura = ponto inicial + metade da largura da imagem
                largura_seta = x1 + 70
                self.seta_baixo.desenhar(tela, largura_seta, y1-30)
            if x1 == self.pos_personagem[0]:
                x1 += 200
                y1 += 200
            else:
                x1 -= 200
                y1 += 200
        for i,inimigo in enumerate(self.inimigos):
            tela.blit(inimigo.imagem,(x2,y2))
            if x2 == self.pos_inimigos[0]:
                x2 -= 200
                y2 += 200
            else:
                x2 += 200
                y2 += 200
            tela.blit((self.fonte.render('{}: {}/{}'.format(inimigo.nome,inimigo.vida_atual,inimigo.vida_max),True,COR_BRANCA)),(x3,y3))
            y3 += 100