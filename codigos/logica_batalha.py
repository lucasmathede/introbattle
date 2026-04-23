import pygame as pg
from interface_batalha import *
from selecao import *
from personagem import *
from seta import *
class Logica:
    def __init__(self,inimigos,img,fonte,escolhidos=([]),escolhidos_em_ordem=([]),evento=(None)):
        self.evento = evento
        self.img = img
        self.escolhidos = escolhidos
        self.escolhidos_em_ordem = escolhidos_em_ordem
        self.fonte = fonte
        self.turno = 0
        self.velocidade = []
        self.turnos = []
        self.alvo = 0
        self.inimigos = inimigos
        self.pos_seta = (750,10)
        self.seta = Seta_baixo()
        self.seta_baixo = Seta_baixo(COR_VERMELHO,25)
    def atualiza_ordem_turno(self):
        for personagem in self.escolhidos:
            self.velocidade.append(personagem.velocidade)
        for inimigo in self.inimigos:
            self.velocidade.append(inimigo.velocidade)
        self.velocidade.sort(reverse=True)
        for velocidade in self.velocidade:
            for personagem in self.escolhidos:
                if velocidade == personagem.velocidade:
                    self.turnos.append(personagem)
                    self.escolhidos_em_ordem.append(personagem)
            for inimigo in self.inimigos:
                if velocidade == inimigo.velocidade:
                    self.turnos.append(inimigo)
        return self.escolhidos_em_ordem
    def atualiza_vivos_e_mortos(self):
        for ser_vivo in self.turnos:
            if ser_vivo.vida_atual <= 0:
                self.turnos.remove(ser_vivo)
                return ser_vivo

                    
    def atualizar(self,event):
        if self.evento == 1 and self.turnos[self.turno].verificador:
                if (self.turnos[self.turno]).defesa != (self.turnos[self.turno]).defesa_reserva:
                    (self.turnos[self.turno]).defesa -= 25
                print(self.turnos[self.turno].defesa)
                self.turnos[self.turno].defesa += 25
                self.turno = (self.turno + 1) % len(self.turnos)
                print(self.turnos[self.turno].defesa)
                return [True]
        elif self.evento == 0 and self.turnos[self.turno].verificador:
                if (self.turnos[self.turno]).defesa != (self.turnos[self.turno]).defesa_reserva:
                    (self.turnos[self.turno]).defesa -= 25
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        self.alvo = (self.alvo + 1) % len(self.inimigos)
                    elif event.key == pg.K_UP:
                        self.alvo = (self.alvo - 1) % len(self.inimigos)
                    elif event.key == pg.K_RETURN:
                        self.turno = (self.turno + 1) % len(self.turnos)
                        return [True,self.alvo]
        elif not self.turnos[self.turno].verificador:
            if event.key == pg.K_RETURN:
                self.turnos[0].vida_atual -= 10
                self.turno = (self.turno + 1) % len(self.turnos)
 
    def retorna_turno(self):
        return self.turno
    def desenhar(self,tela):
        tela.blit(self.img,(0,-220))
        pg.draw.rect(tela,COR_LARANJA,((0,500), (1280,310)), 0)
        pg.draw.rect(tela,COR_CINZA,((5,505), (1270,300)), 0)
        pg.draw.rect(tela,COR_LARANJA,((900,0),(1280,310)),0)
        pg.draw.rect(tela,COR_CINZA,((905,5),(1200,300)),0)
        pg.draw.line(tela,COR_LARANJA,(800,505),(800,720),5)
        x1,y1 = (50,40)
        x2,y2 = (700,40)
        x3,y3 = (925,30)
        x4,y4 = (220,625)
        if self.turnos[self.turno].verificador:
            for i,personagem in enumerate(self.turnos):
                if i == self.turno:
                    tela.blit(personagem.imagem,(50,540))
                    tela.blit(self.fonte.render('Vez de {}'.format(personagem.nome),True,COR_BRANCA),(x4,y4 - 100))
                    tela.blit(self.fonte.render('Escolha o alvo',True,COR_BRANCA),(x4,y4))
        else:
            for i,inimigo in enumerate(self.turnos):
                if i == self.turno:
                    tela.blit(inimigo.imagem,(50,540))
                    tela.blit(self.fonte.render('Vez de {}'.format(inimigo.nome),True,COR_BRANCA),(x4,y4 - 100))
                    tela.blit(self.fonte.render('Escolhendo o alvo',True,COR_BRANCA),(x4,y4))
        for personagem in self.escolhidos:
            tela.blit((self.fonte.render('{}: {}/{}'.format(personagem.nome,personagem.vida_atual,personagem.vida_max),True,COR_BRANCA)),(x4+650,y4-100))
            y4 += 75
        for i,personagem in enumerate(self.escolhidos_em_ordem):
            tela.blit((pg.transform.scale(personagem.imagem,(100,155))),(x1,y1))
            if i == self.turno:
                # largura = ponto inicial + metade da largura da imagem
                largura_seta = x1 + 50
                self.seta_baixo.desenhar(tela, largura_seta, y1-30)
            if x1 == 50:
                x1 += 150
                y1 += 140
            else:
                x1 -= 150
                y1 += 140
        for i,inimigo in enumerate(self.inimigos):
            tela.blit(inimigo.imagem,(x2,y2))
            if x2 == 700:
                x2 -= 150
                y2 += 140
            else:
                x2 += 150
                y2 += 140
            tela.blit((self.fonte.render('{}: {}/{}'.format(inimigo.nome,inimigo.vida_atual,inimigo.vida_max),True,COR_BRANCA)),(x3,y3))
            y3 += 100
        x,y = self.pos_seta
        if self.evento == 0:
            for i in range(len(self.inimigos)):
                esta_selecionado = i == self.alvo
                if esta_selecionado:
                    if self.alvo != 1:
                        self.seta.desenhar(tela,x,y + self.alvo * 150)
                    else:
                        self.seta.desenhar(tela,x - 150,y + self.alvo * 150)
    def status(self,alvo):
        if self.turnos[self.turno].verificador:
            self.inimigos[alvo].vida_atual -= int(((self.turnos[self.turno].ataque / 50 * 10) / (self.inimigos[alvo].defesa / 50)))