# main.py
import pygame as pg

from constantes import *
from menu import Menu
from selecao import *
from pos_selecao import Pos_Selecao
from interface_batalha import *
from personagem import *
from logica_batalha import *

# Configurações da Janela
LARGURA_TELA = 1280
ALTURA_TELA = 720

TITULO = "Introbattle"
FPS = 30


def main():

    pg.init()
    tela = pg.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pg.display.set_caption(TITULO)
    clock = pg.time.Clock()

    # Cria fontes
    fonte_titulo = pg.font.SysFont("Verdana",90)
    fonte_menu = pg.font.SysFont("Consolas", 60)
    fonte_selecao = pg.font.SysFont('Consolas',40)
    fonte_jogo = pg.font.SysFont('Consolas',35)
    
    # Definição dos Estados do Jogo
    ESTADO_MENU = 0
    ESTADO_SELECAO = 1
    ESTADO_OPCOES = 2
    ESTADO_POS_SELECAO = 3
    ESTADO_JOGO = 4

    estado_atual = ESTADO_MENU

    # Fundo do menu
    img_fundo_selecao = pg.transform.scale(pg.image.load("imagens/fundo_selecao2.JPG"),(1280,720))
    img_fundo_jogo = pg.transform.scale(pg.image.load('imagens/paisagem_jogo2.jpg'),(1280,720))

    #Superfície de textos:
    superficie_titulo = fonte_titulo.render('Introbattle', True, COR_BRANCA)
    superficie_aviso = fonte_selecao.render('Selecione 3 intromons, pressione "z" para confirmar',True, COR_BRANCA)
    superficie_confirmacao = fonte_menu.render('É com essa equipe que irá batalhar?',True,COR_BRANCA)
    
    #Imagem dos personagens:
    
    img_personagem1 = pg.transform.scale(pg.image.load("imagens/aisol.png"),(110,165))
    img_personagem2 = pg.transform.scale(pg.image.load("imagens/charlem.png"),(110,165))
    img_personagem3 = pg.transform.scale(pg.image.load("imagens/catershinja.png"),(110,165))
    img_personagem4 = pg.transform.scale(pg.image.load("imagens/lickisweet.png"),(110,165))
    img_personagem5 = pg.transform.scale(pg.image.load("imagens/chespult.png"),(110,165))
    img_personagem6 = pg.transform.scale(pg.image.load("imagens/weanville.png"),(110,165))
    img_personagem7 = pg.transform.scale(pg.image.load("imagens/girapup.png"),(110,165))
    img_personagem8 = pg.transform.scale(pg.image.load("imagens/azepius.png"),(110,165))
    img_inimigo1 = pg.transform.scale(pg.image.load("imagens/magnegoro.png"),(100,155))
    img_inimigo2 = pg.transform.scale(pg.image.load("imagens/karralego.png"),(100,155))
    img_inimigo3 = pg.transform.scale(pg.image.load("imagens/duskver.png"),(100,155))
    
    #Personagens
    personagem1 = Personagem('aisol',img_personagem1,('atq_1','atq_2','atq_3','atq_3'))
    personagem2 = Personagem('charlem',img_personagem2,('atq_1','atq_2','atq_3','atq_3'))
    personagem3 = Personagem('catershinja',img_personagem3,('atq_1','atq_2','atq_3','atq_3'))
    personagem4 = Personagem('lickisweet',img_personagem4,('atq_1','atq_2','atq_3','atq_3'))
    personagem5 = Personagem('chespult',img_personagem5,('atq_1','atq_2','atq_3','atq_3'))
    personagem6 = Personagem('weanville',img_personagem6,('atq_1','atq_2','atq_3','atq_3'))
    personagem7 = Personagem('girapup',img_personagem7,('atq_1','atq_2','atq_3','atq_3'))
    personagem8 = Personagem('azepius',img_personagem8,('atq_1','atq_2','atq_3','atq_3'))
    inimigo1 = Inimigos('magnegoro',img_inimigo1)
    inimigo2 = Inimigos('karralego',img_inimigo2)
    inimigo3 = Inimigos('duskver',img_inimigo3)
    
    # Inicializa Seleção
    
    selecao = Selecao((personagem1,personagem2,personagem3,personagem4,personagem5,personagem6,personagem7,personagem8),pos_inicial2=(30,150))

    # Inicializa o menu
    
    menu = Menu(img_fundo_selecao, ["Jogar", "Opções", "Sair"], fonte_menu, pos_inicial=(100, 350))
    
    # Inicializa pós_seleção
    
    pos_selecao = Pos_Selecao(['Sim','Não'],fonte_menu)
    
    # Inicializa interface do jogo
    
    interface = Interface(img_fundo_jogo,[personagem1,personagem2,personagem3,personagem4,personagem5,personagem6,personagem7,personagem8],[inimigo1,inimigo2,inimigo3],fonte_jogo)
    
    # Inicializa a lógica
    
    logica = Logica([inimigo1,inimigo2,inimigo3])

    rodando = True
    while rodando:
        clock.tick(FPS)

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                rodando = False

            # ESTADO MENU
            if estado_atual == ESTADO_MENU:
                escolha = menu.atualizar(evento)

                if escolha is not None:
                    if escolha == 0:  # Seleção
                        estado_atual = ESTADO_SELECAO
                    elif escolha == 1:  # Opções
                        estado_atual = ESTADO_OPCOES
                    elif escolha == 2:  # Sair
                        rodando = False

            # ESTADO SELEÇÃO
            elif estado_atual == ESTADO_SELECAO:
                escolhido = selecao.atualizar(evento)
                if escolhido == 1:
                    pos_selecao.img_escolhidos = (selecao.escolhidos()).copy()
                    interface.escolhidos = (selecao.escolhidos()).copy()
                    logica.escolhidos = (selecao.escolhidos()).copy
                    estado_atual = ESTADO_POS_SELECAO
                # Permite voltar ao menu com ESC
                if evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE:
                    estado_atual = ESTADO_MENU
                    selecao.reiniciar()

            # ESTADO OPÇÕES
            elif estado_atual == ESTADO_OPCOES:
                # Volta pro menu com tecla ESC
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        estado_atual = ESTADO_MENU
            # ESTADO POS_SELEÇÃO
            elif estado_atual == ESTADO_POS_SELECAO:
                opcao = pos_selecao.atualizar(evento)
                if opcao is not None:
                    if opcao == 0:  # Jogar
                        estado_atual = ESTADO_JOGO
                    elif opcao == 1:  # Voltar
                        estado_atual = ESTADO_SELECAO
                        selecao.reiniciar()
                        pos_selecao.reiniciar()

                # Volta pra seleção com a tecla ESC
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        estado_atual = ESTADO_SELECAO
                        selecao.reiniciar()
                        pos_selecao.reiniciar()
            # ESTADO JOGO:
            elif estado_atual == ESTADO_JOGO:
                escolha = interface.atualizar(evento)
                if escolha == 0 or escolha == 1:
                    logica.evento = escolha
                    logica.atacar
                    logica.defender
                # Volta pro menu com tecla ESC
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        estado_atual = ESTADO_MENU
                        selecao.reiniciar()

        # Renderização e atualização lógica dependendo do estado
        if estado_atual == ESTADO_MENU:
            menu.desenhar(tela)
            tela.blit(superficie_titulo, (100,100))

        elif estado_atual == ESTADO_SELECAO:
            selecao.desenhar(tela)
            tela.blit(superficie_aviso,(30,10))

        elif estado_atual == ESTADO_OPCOES:
            # Tela simples de opções
            tela.fill(COR_PRETA)
            fonte_op = pg.font.SysFont("Arial", 25)
            linhas = [
                "Opções do Jogo",
                "",
                "Som: Ligado",
                "Dificuldade: Normal",
                "",
                "Pressione ESC para voltar",
            ]
            y = 50
            for linha in linhas:
                txt = fonte_op.render(linha, True, COR_BRANCA)
                tela.blit(txt, (LARGURA_TELA // 2 - txt.get_width() // 2, y))
                y += 35
        elif estado_atual == ESTADO_POS_SELECAO:
            pos_selecao.desenhar(tela)
            tela.blit(superficie_confirmacao,(20,10))
        elif estado_atual == ESTADO_JOGO:
            tela.fill(COR_PRETA)
            interface.desenhar(tela)

        pg.display.flip()

    pg.quit()


if __name__ == "__main__":
    main()