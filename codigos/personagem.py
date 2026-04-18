from constantes import *

class Personagem:
    def __init__(self,nome, imagem,opcoes_ataque,vida_atual=(100),vida_max=(100),ataque=(50),defesa=(50),velocidade =(50)):
        self.nome = nome
        self.imagem = imagem
        self.opcoes_ataque = opcoes_ataque
        self.vida_atual = vida_atual
        self.vida_max = vida_max
class Inimigos:
    def __init__(self,nome, imagem,vida_atual=(100),vida_max=(100),ataque=(50),defesa=(50),velocidade=(50)):
        self.nome = nome
        self.imagem = imagem
        self.vida_atual = vida_atual
        self.vida_max = vida_max