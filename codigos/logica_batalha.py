import pygame as pg
from interface_batalha import *
from selecao import *
from personagem import *
from seta import *
class Logica:
    def __init__(self,inimigos,escolhidos=([]),evento=(None),pos_seta=(750,10)):
        self.evento = evento
        self.turno = 0
        self.turnos = []
        self.inimigos = inimigos
        self.pos_seta = pos_seta
        self.seta = Seta_baixo()
        self.alvo = 0
        for aliado in escolhidos:
            self.turno.append(aliado)
    def desenhar(self,tela):
        for i in range(self.inimigos):
            if i == self.alvo:
                self.seta.desenhar(tela,self.pos_seta)
    def atacar(self,event):
        if not self.evento == None:
            if self.evento == 0:
                self.turnos[self.turno].defesa = self.turnos[self.turno].defesa
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        self.alvo = (self.alvo + 1) % len(self.inimigos)
                    elif event.type == pg.K_UP:
                        self.alvo = (self.alvo - 1) % len(self.inimigos)
                    elif event.key == pg.K_RETURN:
                        self.turno = (self.turno + 1) % len(self.turnos)
                        return self.alvo
    def defender(self):
        if not self.evento == None:
            if self.evento == 1:
                self.turnos[self.turno].defesa = self.turnos[self.turno].defesa
                self.turnos[self.turno].defesa += 25
                self.turno = (self.turno + 1) % len(self.turnos)
    def retorna_turno(self):
        return self.turno