from selecao import *
from botao import *
from seta import *
from personagem import *
class Interface:
    def __init__(self,img_fundo,personagens,inimigos,fonte,escolhidos=(None),turnos=(None),pos_personagem=(50,40),pos_inimigos=(700,40),pos_botoes=(220,625),espacamento_botaox = (225)):
        self.img_fundo = img_fundo
        self.personagens = personagens
        self.inimigos = inimigos
        self.escolhidos = escolhidos
        self.turnos = turnos
        self.fonte = fonte
        self.selecionado_index = 0
        self.seta = Seta()
        self.seta_baixo = Seta_baixo(COR_VERMELHO,25)
        self.pos_personagem = pos_personagem
        self.pos_inimigos = pos_inimigos
        x3,y3 = pos_botoes
        self.pos_botoes = pos_botoes
        self.turno = 0
        self.acoes_texto = ['Atacar','Defender']
        self.acoes = []
        self.personagens_selecionados = []
        for texto in self.acoes_texto:
            botao = Botao(texto,(x3,y3),fonte)
            self.acoes.append(botao)
            x3 += espacamento_botaox
    def atualizar(self, evento):
        """
        Gerencia a navegação do teclado
        Retorna o índice do botão selecionado
        """
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_LEFT:
                if not self.selecionado_index == 0 or not self.selecionado_index == len(self.acoes)//2:
                    self.selecionado_index = (self.selecionado_index - 1) % len(self.acoes)
                else:
                    self.selecionado_index = (self.selecionado_index + (len(self.acoes)//2 - 1)) % len(self.acoes)
            elif evento.key == pg.K_RIGHT:
                if not self.selecionado_index == len(self.acoes) - 1 or not self.selecionado_index == len(self.acoes)//2 - 1:
                    self.selecionado_index = (self.selecionado_index + 1) % len(self.acoes)
                else:
                    self.selecionado_index = (self.selecionado_index - 2) % len(self.acoes)
            elif evento.key == pg.K_RETURN:
                return self.selecionado_index
    def desenhar(self, tela):
        """Desenha Botões"""
        tela.blit(self.img_fundo,(0,-220))
        pg.draw.rect(tela,COR_LARANJA,((0,500), (1280,310)), 0)
        pg.draw.rect(tela,COR_CINZA,((5,505), (1270,300)), 0)
        pg.draw.rect(tela,COR_LARANJA,((900,0),(1280,310)),0)
        pg.draw.rect(tela,COR_CINZA,((905,5),(1200,300)),0)
        pg.draw.line(tela,COR_LARANJA,(800,505),(800,720),5)
        x1,y1 = self.pos_personagem
        x2,y2 = self.pos_inimigos
        x3,y3 = (925,30)
        x4,y4 = self.pos_botoes
        for i, botao in enumerate(self.acoes): # Itera com indíce e botão
            esta_ativo = i == self.selecionado_index
            botao.desenhar(tela, esta_ativo)
            if esta_ativo:
                altura_seta = botao.get_altura_centro() - (self.seta.tamanho)
                self.seta.desenhar(tela, botao.pos[0] - 30, altura_seta - 45)
        if self.turnos[self.turno].verificador:
            for i,personagem in enumerate(self.turnos):
                if i == self.turno:
                    tela.blit(personagem.imagem,(50,540))
                    tela.blit(self.fonte.render('Vez de {}'.format(personagem.nome),True,COR_BRANCA),(x4,y4 - 100))
        else:
            for i,inimigo in enumerate(self.turnos):
                if i == self.turno:
                    tela.blit(inimigo.imagem,(50,540))
                    tela.blit(self.fonte.render('Vez de {}'.format(inimigo.nome),True,COR_BRANCA),(x4,y4 - 100))
                    tela.blit(self.fonte.render('Escolhendo o alvo',True,COR_BRANCA),(x4,y4))
        for personagem in self.escolhidos:
            tela.blit((self.fonte.render('{}: {}/{}'.format(personagem.nome,personagem.vida_atual,personagem.vida_max),True,COR_BRANCA)),(x4+650,y4-100))
            y4 += 75
        for i,personagem in enumerate(self.escolhidos):
            tela.blit((pg.transform.scale(personagem.imagem,(100,155))),(x1,y1))
            if i == self.turno:
                # largura = ponto inicial + metade da largura da imagem
                largura_seta = x1 + 50
                self.seta_baixo.desenhar(tela, largura_seta, y1-30)
            if x1 == self.pos_personagem[0]:
                x1 += 150
                y1 += 140
            else:
                x1 -= 150
                y1 += 140
        for i,inimigo in enumerate(self.inimigos):
            tela.blit(inimigo.imagem,(x2,y2))
            if x2 == self.pos_inimigos[0]:
                x2 -= 150
                y2 += 140
            else:
                x2 += 150
                y2 += 140
            tela.blit((self.fonte.render('{}: {}/{}'.format(inimigo.nome,inimigo.vida_atual,inimigo.vida_max),True,COR_BRANCA)),(x3,y3))
            y3 += 100