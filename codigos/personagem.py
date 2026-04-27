from constantes import *

class Personagem:
    def __init__(self,nome, imagem,ataque=(50),defesa=(50),vida_max=(100),velocidade =(50)):
        self.nome = nome
        self.imagem = imagem
        self.verificador = True
        self.defesa = defesa
        self.defesa_reserva = defesa
        self.ataque = ataque
        self.vida_atual = vida_max
        self.vida_max = vida_max
        self.velocidade = velocidade
        if self.vida_atual < 0:
            self.vida_atual = 0
class Inimigos:
    def __init__(self,nome, imagem,vida_max=(100),ataque=(50),defesa=(50),velocidade=(50)):
        self.nome = nome
        self.verificador = False
        self.imagem = imagem
        self.defesa = defesa
        self.ataque = ataque
        self.vida_atual = vida_max
        self.vida_max = vida_max
        self.velocidade = velocidade
        if self.vida_atual < 0:
            self.vida_atual = 0