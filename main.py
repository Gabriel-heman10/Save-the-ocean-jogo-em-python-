#BIBLIOTECAS PYGAME
from pygame import mixer
import pygame
import math
import random

#INICIALIZANDO JANELA
pygame.init()

#DISPLAY COM ALTURA E LARGURA
display = pygame.display.set_mode((900,600))

#NOME DA JANELA
pygame.display.set_caption("Save the Ocean")

#IMAGEM MENU INICIAL
inicial = pygame.image.load("imagem/menu.png")

#IMAGEM DE FUNDO DO JOGO
fundo = pygame.image.load("imagem/fundo.png")

#IMAGEM DO GAMEROVER
final = pygame.image.load("imagem/gameover.png")

#IMAGEM BOTAO DE JOGAR MENU INCIAL
botaojogar = pygame.image.load("imagem/botao jogar.png")

#IMAGEM BOTAO DE SAIR MENU INCIAL
botaosair = pygame.image.load("imagem/botao sair.png")

#IMAGEM BOTAO DE JOGAR NOVAMENTE
botaonovamente = pygame.image.load("imagem/botaonovamente.png")
botaosair2 = pygame.image.load("imagem/botaosair2.png")

#IMAGEM ICONE DA JANELA
icone = pygame.image.load("imagem/icon.png")
pygame.display.set_icon(icone)

#CORES
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

#FUNSSAO INCIAMENTO DO MENU INICIAL
def start_interface():
    while True:
        display.fill((0, 0, 0))

        display.blit(inicial, (0, 0))
        display.blit(botaojogar,(380,326))
        display.blit(botaosair,(400,454))
        mixer.music.stop()

        for event in pygame.event.get():

#MOUSE E BOTAO INICIAR JOGO NO MENU INICIAL
            mouse=pygame.mouse.get_pos()
            if 380+250 > mouse[0] > 380 and 326+40 > mouse[1] > 326:
                display.blit(botaojogar,(380,326))
                if pygame.mouse.get_pressed()[0]:
                    print("inicio jogo")
                    start_game()
            else:
                display.blit(botaojogar,(380,326))

#MOUSE E BOTAO SAIR DO JOGO NO MENU INICIAL
            mouse=pygame.mouse.get_pos()
            if 400+210 > mouse[0] > 400 and 454+50 > mouse[1] > 454:
                display.blit(botaosair,(400, 454))
                if pygame.mouse.get_pressed()[0]:
                    print("sair")
                    pygame.quit()

        pygame.display.update()

#FUNSSAO INICIAMENTO DA TELA FINAL GAMEOVER

def game_over():
    while True:
        display.fill((0, 0, 0))
        display.blit(final, (0, 0))
        display.blit(botaonovamente, (320,400))
        display.blit(botaosair2, (290,480))

        for event in pygame.event.get():

#MOUSE E BOTAOR INICIAR JOGO NOVAMENTE NO GAMEOVER
            mouse = pygame.mouse.get_pos()
            if 320 + 210 > mouse[0] > 320 and 400 + 40 > mouse[1] > 400:
                display.blit(botaonovamente, (320, 400))
                if pygame.mouse.get_pressed()[0]:
                    print("jogar novamente")
                    start_game()

#MOUSE E BOTAO SAIR NA JANELA GAMEROVER
            mouse = pygame.mouse.get_pos()
            if 290 + 210 > mouse[0] > 290 and 480 + 50 > mouse[1] > 480:
                display.blit(botaosair2, (290, 480))
                if pygame.mouse.get_pressed()[0]:
                    print("sair")
                    pygame.quit()

        pygame.display.update()

#FUNSSAO INICIO DO GAME

def start_game():

#LOOO PARA INICIAR O JOGO
    clock = pygame.time.Clock()

    current_time = 0

#VARIAVEL VIDA DO JOGADOR

    vida_value = 200

#VARIAVEL MULTIPLICADOR DE PONTOS

    multiplicador = 1

#VARIAVEL CONTENTO O VALOR DE PONTOS

    score_value = 0

#FONTE DAS LETRAS

    font = pygame.font.Font('freesansbold.ttf', 32)

#ONDE FICARA CADA FUNDAMENTO EM PIXELS

    scoreX = 10
    scoreY = 50

    vidaX = 10
    vidaY = 10

#VARIAVEL COM imagem, velocidade e posisao lixeira

    lixeiraImg = pygame.image.load('imagem/lixeira2.png')
    lixeiraImg = pygame.transform.scale(lixeiraImg, (130, 130))
    lixeiraX = 400
    lixeiraY = 480
    lixeiraX_change = 0

#VARIAVEL COM imagem, velocidade e posisao peixe

    peixeImg = pygame.image.load('imagem/fish.png')
    peixeImg = pygame.transform.scale(peixeImg, (50, 50))
    peixeX = random.randint(0, 700)
    peixeY = -15000
    peixeY_change = 2.5

#VARIAVEL COM imagem, velocidade e posisao lata

    lataImg = pygame.image.load('imagem/lata.png')
    lataImg = pygame.transform.scale(lataImg, (50, 50))
    lataX = random.randint(0, 700)
    lataY = -60
    lataY_change = 1.5

#VARIAVEL COM imagem, velocidade e posisao garrafa

    garrafaImg = pygame.image.load('imagem/garrafa.png')
    garrafaImg = pygame.transform.scale(garrafaImg, (50, 50))
    garrafaX = random.randint(0, 700)
    garrafaY = -3000
    garrafaY_change = 2

#VARIAVEL COM imagem, velocidade e posisao caixa
    caixaImg = pygame.image.load('imagem/caixa.png')
    caixaImg = pygame.transform.scale(caixaImg, (50, 50))
    caixaX = random.randint(0, 700)
    caixaY = -8000
    caixaY_change = 2.5

#SONS DO GAME
    mixer.music.load("som/musicafundo.wav")
    mixer.music.play(-1)
    colissao = pygame.mixer.Sound("som/colissao.wav")
    dano = pygame.mixer.Sound("som/dano.wav")
    gameover = pygame.mixer.Sound("som/gameover.wav")

#FUNSAO QUE ADICIONA PONTUASAO NO GAME
    def show_score(x, y):
        score = font.render("Pontos: " + str(score_value), True, (5, 5, 5))
        display.blit(score, (x, y))

# FUNSAO QUE ADICIONA VIDA NO GAME

    def show_vida(x, y):
        vida = font.render("Vida: ", True, (5, 5, 5))
        display.blit(vida, (x, y))

#FUNSAO QUE ADICIONA A LIXEIRA NO GAME

    def lixeira(x, y):
        display.blit(lixeiraImg, (x, y))

#FUNSSAO QUE ADICIONA A LIXEIRA NO GAME
    def peixe(x, y):
        display.blit(peixeImg, (x, y))

#FUNSAO QUE ADICIONA A LATA NO GAME

    def lata(x, y):
        display.blit(lataImg, (x, y))

#FUNSAO QUE ADICIONA A GARRAFA NO GAME

    def garrafa(x, y):
        display.blit(garrafaImg, (x, y))

#FUNSAO QUE ADICIONA A CAIXA NO GAME

    def caixa(x, y):
        display.blit(caixaImg, (x, y))

# FUNSAO colissao peixe e lixeira

    def isCollisionPeixe(lixeiraX, lixeiraY, peixeX, peixeY):
        distance = math.sqrt((math.pow(lixeiraX-peixeX,2)) + (math.pow(lixeiraY-peixeY,2)))
        if distance < 65:
            dano.play()
            return True
        else:
            return False

#FUNSAO colissao lata e lixeira
    def isCollisionLata(lixeiraX, lixeiraY, lataX, lataY):
        distance = math.sqrt((math.pow(lixeiraX-lataX,2)) + (math.pow(lixeiraY-lataY,2)))
        if distance < 65:
            colissao.play()
            return True
        else:
            return False

#FUNSAO colissao garrafa e lixeira
    def isCollisionGarrafa(lixeiraX, lixeiraY, garrafaX, garrafaY):
        distance = math.sqrt((math.pow(lixeiraX-garrafaX,2)) + (math.pow(lixeiraY-garrafaY,2)))
        if distance < 65:
            colissao.play()
            return True
        else:
            return False

#FUNSAO colissao caixa e lixeira
    def isCollisionCaixa(lixeiraX, lixeiraY, caixaX, caixaY):
        distance = math.sqrt((math.pow(lixeiraX-caixaX,2)) + (math.pow(lixeiraY-caixaY,2)))
        if distance < 65:
            colissao.play()
            return True
        else:
            return False


 #loop iniciar aplicativo
    while True:

        pygame.draw.rect(fundo, vermelho, (100, 15, 200, 20))
        pygame.draw.rect(fundo, verde, (100, 15, vida_value, 20))

# Define a cor do fundo.

        display.fill((0, 0, 0))

# Define o background como fundo.

        display.blit(fundo, (0, 0))

# Loop que espera um evento acontecer para realizar uma determinada

        for event in pygame.event.get():

            # Espera o evento quit, e entao fecha o jogo

            if event.type == pygame.QUIT:
                pygame.quit()
            #Espera o evento keydown, que  quando um tecla  pressionada.

            if event.type == pygame.KEYDOWN:

                # Move o player em 5 pontos de velocidade para a esquerda, caso a seta esquerda seja pressionada.

                if event.key == pygame.K_LEFT:
                    lixeiraX_change = -10

                # Move o player em 5 pontos de velocidade para a direita, cas    o a seta direita seja pressionada.

                if event.key == pygame.K_RIGHT:
                    lixeiraX_change = 10

                if event.key == pygame.K_SPACE:
                    lataY_change = lataY_change / 3
                    garrafaY_change = garrafaY_change / 3
                    caixaY_change = caixaY_change / 3
                    clock.tick()
                    clock.get_time()

            # Retira a velocidade do player, deixando-o parado, caso pare de pressionar a tecla esquerda ou tecla direita.

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lixeiraX_change = 0
                if event.key == pygame.K_SPACE:
                    lataY_change = lataY_change * 3
                    garrafaY_change = garrafaY_change * 3
                    caixaY_change = caixaY_change * 3
                    clock.tick()

        if vida_value == 0:
                    mixer.music.pause()
                    gameover.play()
                    game_over()
            # Recebe o tempo que se passou durante o loop.
        current_time = pygame.time.get_ticks()

        #Adiciona valores na localizacao vertircal e horizontal de cada item, fazendo les irem para esquerda, direita, ou para baixo.
        peixeY += peixeY_change
        lataY += lataY_change
        garrafaY += garrafaY_change
        caixaY += caixaY_change
        lixeiraX += lixeiraX_change

        #TRAVA A LOCALIZACAO DA LIXEIRA EM 0 PIXELS NA HORIZONTAL, PARA QUE O MESMO NAO SAIA DA TELA

        if lixeiraX <= 0:
            lixeiraX = 0

        #TRAVA A LOCALIZACAO DA LIXEIRA EM 800 PIXELS HORIZONTAL, PARA QUE O MESMO NAO SAIA DA TELA

        elif lixeiraX >= 800:
            lixeiraX = 800

        #EFETUA UMA SERIA DE APLICACOES NA COLISAO DA LIXEIRA COM PEIXE, PERDA DE VIDA E ETC
        collision = isCollisionPeixe(lixeiraX, lixeiraY, peixeX, peixeY)
        if collision:
            soma_peixe = 0
            peixeMultiplicado = multiplicador * soma_peixe
            peixeX = random.randint(0, 770)
            peixeY = -60
            peixeY_change += 0.02
            score_value += peixeMultiplicado
            vida_value -= 50

#EFETUA UMA SERIE DE APLICACOES NA COLISAO DA LIXEIRA COM A LATA, VIDA E ETC
        collision = isCollisionLata(lixeiraX, lixeiraY, lataX, lataY)
        if collision:
            soma_lata = 5
            lataMultiplicado = multiplicador * soma_lata
            lataX = random.randint(0, 770)
            lataY = -60
            lataY_change += 0.02
            score_value += lataMultiplicado


            vida_value += 10

#EFETUA UMA SERIE DE APLICACOES NA COLISAO DA LIXEIRA COM A GARRAFA, VIDA E ETC
        collision = isCollisionGarrafa(lixeiraX, lixeiraY, garrafaX, garrafaY)
        if collision:
            soma_garrafa = 10
            garrafaMultiplicado = multiplicador * soma_garrafa
            garrafaX = random.randint(0, 700)
            garrafaY = -60
            garrafaY_change += 0.02
            score_value += garrafaMultiplicado


            vida_value += 20

#EFETUA UMA SERIE DE APLICACOES NA COLISAO DA LIXEIRA COM A CAIXA, VIDA E ETC
        collision = isCollisionCaixa(lixeiraX, lixeiraY, caixaX, caixaY)
        if collision:
            soma_caixa = 20
            caixaMultiplicado = multiplicador * soma_caixa
            caixaX = random.randint(0, 700)
            caixaY = -60
            caixaY_change += 0.02
            score_value += caixaMultiplicado

            vida_value += 30

#EFETUA UMA SERIE DE APLICACOES CASO O PEIXE PASSE DO JOGADOR, COMO RESETAR O MULTIPLICADOR, DIMINUIR VIDA ETC
        if peixeY >= 600:
            peixeX = random.randint(0, 700)
            peixeY = -60
            peixeY_change += 0.02

            vida_value -= 0

##EFETUA UMA SERIE DE APLICACOES CASO O LATA PASSE DO JOGADOR, COMO RESETAR O MULTIPLICADOR, DIMINUIR VIDA ETC
        if lataY >= 600:
            lataX = random.randint(0, 700)
            lataY = -60
            lataY_change += 0.02

            multiplicador = 1
            vida_value -= 10

##EFETUA UMA SERIE DE APLICACOES CASO O GARRAFA PASSE DO JOGADOR, COMO RESETAR O MULTIPLICADOR, DIMINUIR VIDA ETC
        if garrafaY >= 600:
            garrafaX = random.randint(0, 770)
            garrafaY = -60
            garrafaY_change += 0.02

            multiplicador = 1
            vida_value -= 20

##EFETUA UMA SERIE DE APLICACOES CASO O CAIXA PASSE DO JOGADOR, COMO RESETAR O MULTIPLICADOR, DIMINUIR VIDA ETC
        if caixaY >= 600:
            caixaX = random.randint(0, 770)
            caixaY = -60
            caixaY_change += 0.02

            multiplicador = 1
            vida_value -= 30

# Libera a garrafa para cair quando o tempo chegar em 10 segundos. (Medido em milisegundos)
        if current_time >= 10000:
            garrafa(garrafaX, garrafaY)

##Libera o caixa para cair quando o tempo chegar em 25 segundos. (Medido em milisegundos)
        if current_time >= 25000:
            caixa(caixaX, caixaY)

# Libera o peixe para cair quando o tempo chegar em 35 segundos. (Medido em milisegundos)

        if current_time >= 35000:
            peixe(peixeX, peixeY)

#define o maximo de vida igual a 10
        if vida_value >= 200:
            vida_value = 200

#define o maximo de vida igual a  0
        if vida_value <= 0:
            vida_value = 0

#funsoes se serem chamadas para adicionar a imagem em cada item
        peixe(peixeX, peixeY)
        lixeira(lixeiraX, lixeiraY)
        lata(lataX, lataY)
        show_score(scoreX, scoreY)
        show_vida(vidaX, vidaY)

#funsao para manter a tela atualizada a cada aplicasao
        pygame.display.update()

        print(clock.get_time())

# Inicia a interface
start_interface()










