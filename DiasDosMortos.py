import pygame as pg 
import time 
import os 
from PIL import Image, ImageSequence

os.system("cls")

pg.init()
pg.mixer.init() 

pg.mixer.music.load('Fundos.mp3')
pg.mixer.music.play(-1)

risada = pg.mixer.Sound('Risada.wav')

janelaY = 850
janelaX = 1500

x = 0
y = 1

pg.init()
tamanhoTela = pg.display.get_desktop_sizes()[0]
print(tamanhoTela)
janela = pg.display.set_mode(tamanhoTela)

velocidade = 9
vel_inimigo = 4

jY = 500
jX = 500

jogador = pg.Rect(jX,jY, 100, 100)



coracoes = [
    pg.Rect(tamanhoTela[x] * 0.8, tamanhoTela[x] * 0.0025, tamanhoTela[x] * 0.025, tamanhoTela[x] * 0.025),
    pg.Rect(tamanhoTela[x] * 0.835, tamanhoTela[x] * 0.0025, tamanhoTela[x] * 0.025, tamanhoTela[x] * 0.025),
    pg.Rect(tamanhoTela[x] * 0.87, tamanhoTela[x] * 0.0025, tamanhoTela[x] * 0.025, tamanhoTela[x] * 0.025)
]

fonte = pg.font.SysFont('Arial', 30)

mapa = [{"saidas" : {"S1Cima" : pg.Rect(0,0,tamanhoTela[x],1),"S1Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.10), 
                      pg.Rect(tamanhoTela[x] * 0.58, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.10), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.04, tamanhoTela[y]), 
                      pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.1 ,1600, tamanhoTela[x] * 0.11), 
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.25), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.47, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)
                      ],
         "mapa": pg.image.load("mapaa9.png")},

        {"saidas" : {"S2Cima" : pg.Rect(0,0,tamanhoTela[x],1),"S2Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.10), 
                      pg.Rect(tamanhoTela[x] * 0.58, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.10), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.034, tamanhoTela[y] * 0.24), 
                      pg.Rect(0, tamanhoTela[y] * 0.46, tamanhoTela[x] * 0.034, tamanhoTela[y] * 0.45),
                      pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.1 ,1600, tamanhoTela[x] * 0.11), 
                      pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y]),
                      ],
        "esqueleto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "mapa": pg.image.load("mapaa10.png")},

        {"saidas": {"S3Cima" : pg.Rect(0,0,tamanhoTela[x],1)}, 
         "paredes": [pg.Rect(0, 0, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.10), 
                     pg.Rect(tamanhoTela[x] * 0.58, 0, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.10), 
                     pg.Rect(0,0,tamanhoTela[x] * 0.04, tamanhoTela[y]),
                     pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.09 ,1600, tamanhoTela[x] * 0.03), 
                     pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y])
                     ],
         "objeto" :  pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : pg.image.load("eTERCOo.png"),
         "Resposta" : "terço",
         "mapa": pg.image.load("mapaa11.png")
         },

        {"saidas": {"S4Cima" : pg.Rect(0,0,tamanhoTela[x],1)}, 
         "paredes": [pg.Rect(0, 0, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.10), 
                     pg.Rect(tamanhoTela[x] * 0.58, 0, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.10), 
                     pg.Rect(0,0,tamanhoTela[x] * 0.04, tamanhoTela[y]),
                     pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.09 ,1600, tamanhoTela[x] * 0.03), 
                     pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y])
                     ],
         "objeto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : pg.image.load("eFOOTO.png"),
         "Resposta" : "fotos",
         "mapa": pg.image.load("mapaa12.png")
         },

        {"saidas" : {"S5Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),"S5Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.1, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.10), 
                      pg.Rect(tamanhoTela[x] * 0.59, tamanhoTela[y] - tamanhoTela[x] * 0.1, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.10), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.04, tamanhoTela[y]), 
                      pg.Rect(0,0,1600, tamanhoTela[x] * 0.09), 
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.25), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.45, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)
                      ],
        "objeto" :  pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : pg.image.load("eFLOR.png"),
        "Resposta" : "flores",
        "mapa": pg.image.load("mapaa5.png")
         },

        {"saidas" : {"S6Cima" : pg.Rect(0,0,tamanhoTela[x],1),
                     "S6Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),
                     "S6Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),
                     "S6Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.10), 
                      pg.Rect(tamanhoTela[x] * 0.59, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.10), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.09, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.1), 
                      pg.Rect(tamanhoTela[x] * 0.59, tamanhoTela[y] - tamanhoTela[x] * 0.09, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.1), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.04, tamanhoTela[y] * 0.25), 
                      pg.Rect(0 , tamanhoTela[y] * 0.46, tamanhoTela[x] * 0.04, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.25), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.47, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)
                      ],
        "objeto" :  pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : pg.image.load("eVELA.png"),
        "Resposta" : "velas",
        "mapa": pg.image.load("mapaa6.png")
         },

        {"saidas" : {"S7Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),
                     "S7Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),
                     "S7Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.1), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.092, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.2), 
                      pg.Rect(tamanhoTela[x] * 0.59, tamanhoTela[y] - tamanhoTela[x] * 0.092, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.11), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.04, tamanhoTela[y] * 0.26), 
                      pg.Rect(0 , tamanhoTela[y] * 0.47, tamanhoTela[x] * 0.04, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.25), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.47, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)
                      ],
         "esqueleto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
         "mapa": pg.image.load("mapaa7.png")},
        
        {"saidas" : {"S8Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),
                     "S8Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.1), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.09, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.1), 
                      pg.Rect(tamanhoTela[x] * 0.59, tamanhoTela[y] - tamanhoTela[x] * 0.09, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.1), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.04, tamanhoTela[y] * 0.25), 
                      pg.Rect(0 , tamanhoTela[y] * 0.47, tamanhoTela[x] * 0.04, tamanhoTela[y] * 0.6),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y])
                      ],
        "objeto" :  pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : pg.image.load("eCAVEIRA.png"),
        "Resposta" : "caveiras",
        "mapa": pg.image.load("mapaa8.png")
         },

        {"saidas" : {"S9TP" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05)},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.11), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]),
                      pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.09 ,1600, tamanhoTela[x] * 0.11), 
                      pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y])],
        "objeto" :  pg.Rect(tamanhoTela[x] * 0.3, tamanhoTela[y] * 0.3, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : pg.image.load("eBEBIDA.png"),
        "Resposta" : "bebidas",
        "mapa": pg.image.load("mapa1.png")
         },

        {"saidas" : {"S10Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),"S10Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.092, tamanhoTela[x] * 0.42, tamanhoTela[x] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.59, tamanhoTela[y] - tamanhoTela[x] * 0.092, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.3), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.04, tamanhoTela[y]), 
                      pg.Rect(0,0,1600, tamanhoTela[x] * 0.1), 
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.26), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.47, tamanhoTela[x] * 0.03, tamanhoTela[y])
                      ],
         "esqueleto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
         "mapa": pg.image.load("mapa2.png")},
         

        {"saidas" : {"S11Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]), 
                     "S11Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),
                     "S11TP" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05)},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.1), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.092, tamanhoTela[x], tamanhoTela[x]), 
                      pg.Rect(tamanhoTela[x] * 0.97, 0 , tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.25), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.04, tamanhoTela[y] * 0.26), 
                      pg.Rect(0 , tamanhoTela[y] * 0.47, tamanhoTela[x] * 0.04, tamanhoTela[y]),
                      #pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.47, tamanhoTela[x] * 0.4, tamanhoTela[y])
                      ],
         "esqueleto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
         "mapa": pg.image.load("mapa3.png")},

        {"saidas" : {"S12Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.1), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.092, tamanhoTela[x], tamanhoTela[x]), 
                      #pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x]), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.04, tamanhoTela[y] * 0.26), 
                      pg.Rect(0 , tamanhoTela[y] * 0.47, tamanhoTela[x] * 0.04, tamanhoTela[y]),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y])
                      ],
        "objeto" :  pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "esqueleto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : pg.image.load("ePAO.png"),
        "Resposta" : "pao dos muertos",
        "mapa": pg.image.load("mapaa4.png")
         },
]

mapaAtual = 0

salasComitem = [2, 3, 4, 5, 7, 8, 11] # considerando a 1a sala como 0

imgItens = [
    pg.image.load("terço.png").convert_alpha(),
    pg.image.load("retrato.png").convert_alpha(),
    pg.image.load("flor.png").convert_alpha(),
    pg.image.load("vela.png").convert_alpha(),
    pg.image.load("caveiraMexicana.png").convert_alpha(),
    pg.image.load("tequila.png").convert_alpha(),
    pg.image.load("pãodMuerto.png").convert_alpha(),
] 

for i in range(len(imgItens)):
    imgItens[i] = pg.transform.scale(imgItens[i], (int(tamanhoTela[y] * 0.1), int(tamanhoTela[y] * 0.1)))

imgGreyItens = [
    pg.image.load("terçoGREY.png").convert_alpha(),
    pg.image.load("retratoGREY.png").convert_alpha(),
    pg.image.load("florGREY.png").convert_alpha(),
    pg.image.load("velaGREY.png").convert_alpha(),
    pg.image.load("caveMexiGREY.png").convert_alpha(),
    pg.image.load("tequilaGREY.png").convert_alpha(),
    pg.image.load("pãoGREY.png").convert_alpha(),
] 

for i in range(len(imgGreyItens)):
    imgGreyItens[i] = pg.transform.scale(imgGreyItens[i], (int(tamanhoTela[y] * 0.1), int(tamanhoTela[y] * 0.1)))

add = janela.fill
loop = True
clock = pg.time.Clock()


vida = 3
itens = 14

colisaoTp9 = colisaoTp11 = False
tempoMinTp = 0.5

enig = False
mostrar_erro = False

texto = ""

textoItens = fonte.render("Itens: ", True, (255, 255, 255))
largTextoItens = textoItens.get_width()

sepItens = fonte.render(" ", True, (255, 255, 255))
largSepItens = sepItens.get_width()

coracaoImg = pg.image.load("coração.png").convert_alpha()
coracaoImg = pg.transform.scale(coracaoImg, (int(tamanhoTela[1] * 0.1), int(tamanhoTela[1] * 0.1)))

coracaoGreyImg = pg.image.load("coracaoPRETO.png").convert_alpha()
coracaoGreyImg = pg.transform.scale(coracaoGreyImg, (int(tamanhoTela[1] * 0.1), int(tamanhoTela[1] * 0.1)))

corJogador = (255,255,255)

gifCavRindo = Image.open("caveRindo.gif")
frameAtual = 0

mov = False
while loop:
    clock.tick(60)
    teclas = pg.key.get_pressed()
    eventos = pg.event.get()

    if not enig:
        for evento in eventos:
            if evento.type == pg.QUIT or teclas[pg.K_x] and teclas[pg.K_i] and teclas[pg.K_e] and teclas[pg.K_t]:
                loop = False

        for parede in mapa[mapaAtual]["paredes"]:
            add((255,0,0),parede)
            if jogador.colliderect(parede):
                distXD = jogador.right - parede.left # direita do jogador
                distXE = jogador.left - parede.right
                distYC = jogador.top - parede.bottom # cima do jogador
                distYB = jogador.bottom - parede.top

                distXE = distXE * -1 if distXE <= 0 else distXE
                distXD = distXD * -1 if distXD <= 0 else distXD
                distYB = distYB * -1 if distYB <= 0 else distYB
                distYC = distYC * -1 if distYC <= 0 else distYC

                if distXD < distXE:
                    menorSpX = distXD
                else:
                    menorSpX = distXE

                if distYC < distYB:
                    menorSpY = distYC
                else:
                    menorSpY = distYB

                if menorSpX < menorSpY:
                    if menorSpX == distXD:
                        colisaoDireita = True
                    else:
                        colisaoEsquerdo = True
                else:
                    if menorSpY == distYB:
                        colisaoBaixo = True
                    else:
                        colisaoCima = True

        mapaFundo = pg.transform.scale(mapa[mapaAtual]["mapa"], (int(tamanhoTela[x]), int(tamanhoTela[y])))
        janela.blit(mapaFundo, (0,0))

        mov = False
        if teclas[pg.K_UP] and not colisaoCima:
            jogador.y -= velocidade
            corJogador = (255,0,0)
            mov = True
        if teclas[pg.K_DOWN] and not colisaoBaixo:
            jogador.y += velocidade
            corJogador = (0,255,0)
            mov = True
        if teclas[pg.K_RIGHT] and not colisaoDireita:
            jogador.x += velocidade 
            corJogador = (0,0,255)
            mov = True
        if teclas[pg.K_LEFT] and not colisaoEsquerdo:
            jogador.x -= velocidade
            corJogador = (255,255,0)
            mov = True
        if not mov:
            corJogador = (255,255,255) 

        pg.draw.rect(janela, corJogador, jogador)

        colisaoCima = False
        colisaoBaixo = False
        colisaoDireita = False
        colisaoEsquerdo = False

        if "esqueleto" in mapa[mapaAtual]: 
            esqueleto = mapa[mapaAtual]["esqueleto"]
            dx = jogador.centerx - esqueleto.centerx
            dy = jogador.centery - esqueleto.centery
            dist = (dx**2 + dy**2) ** 0.5
            if dist != 0 and enig == False and itens != 0:
                dx /= dist
                dy /= dist
                esqueleto.x += dx * vel_inimigo
                esqueleto.y += dy * vel_inimigo
            add((255, 255, 0), esqueleto)
            if jogador.colliderect(mapa[mapaAtual]["esqueleto"]):
                risada.play()
                for _ in range(2):
                    for frame in ImageSequence.Iterator(gifCavRindo):
                        frame = frame.convert("RGBA")
                        frame = frame.resize((tamanhoTela[x], tamanhoTela[y]))
                        modo, tamanho, dados = frame.mode, frame.size, frame.tobytes()
                        sustoFrame = pg.image.fromstring(dados, tamanho, modo)
                        janela.blit(sustoFrame, (0, 0))
                        pg.display.flip() 
                        pg.time.delay(50) 

                mapa[mapaAtual].pop("esqueleto")
                vida -= 1


        if "objeto" in mapa[mapaAtual]:
            add((255, 165, 0), mapa[mapaAtual]["objeto"])
            if jogador.colliderect(mapa[mapaAtual]["objeto"]):
                itens -= 1
                mapa[mapaAtual].pop("objeto")
                texto = ""
                enig = True

        for k,v in mapa[mapaAtual]["saidas"].items():
            if jogador.colliderect(v):
                if k == "S1Cima":
                    mapaAtual = 4
                    jogador.y = tamanhoTela[y] - 100
                elif k == "S1Direita":
                    mapaAtual = 1
                    jogador.x = 0


                elif k == "S2Esquerda":
                    mapaAtual = 0
                    jogador.x = tamanhoTela[x] - 100
                elif k == "S2Cima":
                    mapaAtual = 5
                    jogador.y = tamanhoTela[y] - 100

                elif k == "S3Cima":
                    mapaAtual = 6
                    jogador.y = tamanhoTela[y] - 100

                elif k == "S4Cima":
                    mapaAtual = 7
                    jogador.y = tamanhoTela[y] - 100

                elif k == "S5Direita":
                    mapaAtual = 5
                    jogador.x = 0
                elif k == "S5Baixo":
                    mapaAtual = 0
                    jogador.y = 0

                elif k == "S6Direita":
                    mapaAtual = 6
                    jogador.x = 100
                elif k == "S6Baixo":
                    mapaAtual = 1
                    jogador.y = 0
                elif k == "S6Cima":
                    mapaAtual = 9
                    jogador.y = tamanhoTela[y] - 100
                elif k == "S6Esquerda":
                    mapaAtual = 4
                    jogador.x = tamanhoTela[x] - 100

                elif k == "S7Baixo":
                    mapaAtual = 2
                    jogador.y = 0
                elif k == "S7Direita":
                    mapaAtual = 7
                    jogador.x = 100 
                elif k == "S7Esquerda":
                    mapaAtual = 5
                    jogador.x = tamanhoTela[x] - 100

                elif k == "S8Baixo":
                    mapaAtual = 3
                    jogador.y = 0
                elif k == "S8Esquerda":
                    mapaAtual = 6
                    jogador.x = tamanhoTela[x] - 100

                elif k == "S10Direita":
                    mapaAtual = 10
                    jogador.x = 0
                elif k == "S10Baixo":
                    mapaAtual = 5
                    jogador.y = 0

                elif k == "S11Direita":
                    mapaAtual = 11
                    jogador.x = 100 
                elif k == "S11Esquerda":
                    mapaAtual = 9
                    jogador.x = tamanhoTela[x] - 100

                elif k == "S12Esquerda":
                    mapaAtual = 10
                    jogador.x = tamanhoTela[x] - 100
                
        if mapaAtual == 8:
            if jogador.colliderect(mapa[mapaAtual]["saidas"]["S9TP"]) and not colisaoTp9:
                colisaoTp9 = True
                inicioColisao = time.gmtime(time.time())[5]
            elif jogador.colliderect(mapa[mapaAtual]["saidas"]["S9TP"]) and colisaoTp9:
                segsAtuais = time.gmtime(time.time())[5]
                if segsAtuais - inicioColisao >= tempoMinTp or (segsAtuais - inicioColisao < 0 and segsAtuais - inicioColisao >= tempoMinTp - 60):
                    mapaAtual = 10
                    colisaoTp9 = False
            elif not jogador.colliderect(mapa[mapaAtual]["saidas"]["S9TP"]) and colisaoTp9:
                colisaoTp9 = False
            
        elif mapaAtual == 10:
            if jogador.colliderect(mapa[mapaAtual]["saidas"]["S11TP"]) and not colisaoTp11:
                colisaoTp11 = True
                inicioColisao = time.gmtime(time.time())[5]
            elif jogador.colliderect(mapa[mapaAtual]["saidas"]["S11TP"]) and colisaoTp11:
                segsAtuais = time.gmtime(time.time())[5]
                if segsAtuais - inicioColisao >= tempoMinTp or (segsAtuais - inicioColisao < 0 and segsAtuais - inicioColisao <= tempoMinTp - 60):
                    mapaAtual = 8
                    colisaoTp11 = False
            elif not jogador.colliderect(mapa[mapaAtual]["saidas"]["S11TP"]) and colisaoTp11:
                colisaoTp11 = False

        for saida in mapa[mapaAtual]["saidas"].values():
            add((0,255,0), saida)

        # exibir itens que faltam
        janela.blit(fonte.render("Itens: ", True, (255, 255, 255)), (tamanhoTela[x] * 0.05, tamanhoTela[x] * 0.0025))
        i = 0 # de 0 até 6
        somaLarguras = largTextoItens

        for indexSala in salasComitem:
            if mapa[indexSala].get("enigma"): # Item ainda não obtido (agora o enigma é excluído quando a pessoa acerta)
                item = imgGreyItens[i]
            else: # item já obtido
                item = imgItens[i]

            janela.blit(item, (tamanhoTela[x] * 0.05 + somaLarguras, tamanhoTela[x] * 0.0025))
            

            somaLarguras += item.get_width()
            if i < 6:
                janela.blit(sepItens, (tamanhoTela[x] * 0.05 + somaLarguras, tamanhoTela[x] * 0.0025))
                somaLarguras += largSepItens
            i+=1

        # exibir vidas 
        for i in range(3, 0, -1): # 3 2 1
            j = 3 - i # 0 1 2
            if i > vida:
                janela.blit(coracaoGreyImg, coracoes[j])
            else:
                janela.blit(coracaoImg, coracoes[j])

    else:
        overlay = pg.Surface(tamanhoTela)
        overlay.fill((0, 0, 0))
        janela.blit(overlay, (0, 0))

        
        
        enigma = pg.transform.scale(mapa[mapaAtual]["enigma"], (int(tamanhoTela[x]), int(tamanhoTela[y])))
        janela.blit(enigma, (0, 0))

        txt = fonte.render(texto, True, (0,0,0))
        janela.blit(txt, (tamanhoTela[x]*0.4, tamanhoTela[y]*0.7))
        txt2 = texto.lower()


        for evento in eventos:
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN:
                    if mapa[mapaAtual]["Resposta"]:
                        if mapa[mapaAtual]["Resposta"] == txt2:
                            itens -= 1
                            enig = False
                            mapa[mapaAtual].pop("enigma")
                        else:
                            inicio = pg.time.get_ticks()
                            espera = 500

                            mostrar_erro = True

                elif evento.key == pg.K_BACKSPACE:
                    texto = texto[:-1]
                else:
                    texto += evento.unicode
        
        if mostrar_erro:
            agora = pg.time.get_ticks()
            if agora - inicio < espera:
                erro = fonte.render("Resposta Errada", True, (255,0,0))
                janela.blit(erro, (tamanhoTela[x]*0.5, tamanhoTela[y]*0.6))
            else:
                mostrar_erro = False

            
        pg.display.flip() 
    
    if vida == 0:
        overlay = pg.Surface(tamanhoTela)
        overlay.fill((255, 0, 0))
        janela.blit(overlay, (0, 0))
    elif itens == 0:
        overlay = pg.Surface(tamanhoTela)
        overlay.fill((0, 255, 0))
        janela.blit(overlay, (0, 0))

    pg.display.flip()
