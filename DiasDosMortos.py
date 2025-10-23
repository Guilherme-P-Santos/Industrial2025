import  pygame as pg 
import time 
import os 

os.system("cls")

pg.init()
pg.mixer.init() 

pg.mixer.music.load('MusicaFundo.mp3')
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
vel_inimigo = velocidade / 3

jY = 500
jX = 500

jogador = pg.Rect(jX,jY, 100, 100)

fonte = pg.font.SysFont('Arial', 30)

mapa = [{"saidas" : {"S1Cima" : pg.Rect(0,0,tamanhoTela[x],1),"S1Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]), 
                      pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.03 ,1600, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)]},

        {"saidas" : {"S2Cima" : pg.Rect(0,0,tamanhoTela[x],1),"S2Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(0, tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4),
                      pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.03 ,1600, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y]),],
        "esqueleto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05)},

        {"saidas": {"S3Cima" : pg.Rect(0,0,tamanhoTela[x],1)}, 
         "paredes": [pg.Rect(0, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                     pg.Rect(tamanhoTela[x] * 0.6, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                     pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]),
                     pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.03 ,1600, tamanhoTela[x] * 0.03), 
                     pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y])],
         "objeto" :  pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
         "enigma" : "Enigma 1"
         },

        {"saidas": {"S4Cima" : pg.Rect(0,0,tamanhoTela[x],1)}, 
         "paredes": [pg.Rect(0, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                    pg.Rect(tamanhoTela[x] * 0.6, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                    pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]),
                    pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.03 ,1600, tamanhoTela[x] * 0.03), 
                    pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y])],
         "objeto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
         "enigma" : "Enigma 2"
         },

        {"saidas" : {"S5Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),"S5Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]), 
                      pg.Rect(0,0,1600, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)],
        "objeto" :  pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : "Enigma 3"
         },

        {"saidas" : {"S6Cima" : pg.Rect(0,0,tamanhoTela[x],1),
                     "S6Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),
                     "S6Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),
                     "S6Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(0 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)],
        "objeto" :  pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : "Enigma 4"
         },

        {"saidas" : {"S7Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),
                     "S7Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),
                     "S7Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(0 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)],
         "esqueleto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05)},
        
        {"saidas" : {"S8Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),
                     "S8Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(0 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y])],
        "objeto" :  pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : "Enigma 5"
         },

        {"saidas" : {"S9TP" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05)},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]),
                      pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.03 ,1600, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y])],
        "objeto" :  pg.Rect(tamanhoTela[x] * 0.3, tamanhoTela[y] * 0.3, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : "Enigma 6"
         },

        {"saidas" : {"S10Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),"S10Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]), 
                      pg.Rect(0,0,1600, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)],
         "esqueleto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05)},

        {"saidas" : {"S11Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]), 
                     "S11Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),
                     "S11TP" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05)},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(0 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)],
         "esqueleto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05)},

        {"saidas" : {"S12Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(0 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y])],
        "objeto" :  pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "esqueleto" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05),
        "enigma" : "Enigma 7"
         },
]

add = janela.fill
loop = True
clock = pg.time.Clock()

vida = 3

mapaAtual = 0

colisaoTp9 = colisaoTp11 = False
tempoMinTp = 0.5

enig = False

texto = ""

while loop:
    clock.tick(60)
    teclas = pg.key.get_pressed()
    eventos = pg.event.get()

    for evento in eventos:
        if evento.type == pg.QUIT or teclas[pg.K_x] or vida == 0:
            loop = False

    if not enig:
        add((0,0,0))

        add((255,255,255),jogador)

        colisaoCima = False
        colisaoBaixo = False
        colisaoDireita = False
        colisaoEsquerdo = False

        if "esqueleto" in mapa[mapaAtual]: 
            esqueleto = mapa[mapaAtual]["esqueleto"]
            dx = jogador.centerx - esqueleto.centerx
            dy = jogador.centery - esqueleto.centery
            dist = (dx**2 + dy**2) ** 0.5
            if dist != 0 and enig == False:
                dx /= dist
                dy /= dist
                esqueleto.x += dx * vel_inimigo
                esqueleto.y += dy * vel_inimigo
            add((255, 255, 0), esqueleto)
            if jogador.colliderect(mapa[mapaAtual]["esqueleto"]):
                risada.play()
                overlay = pg.Surface(tamanhoTela)
                overlay.fill((255, 0, 0))
                janela.blit(overlay, (0, 0))
                pg.display.flip() 
                pg.time.delay(500) 
                mapa[mapaAtual].pop("esqueleto")
                vida -= 1

        if "objeto" in mapa[mapaAtual]:
            add((255, 165, 0), mapa[mapaAtual]["objeto"])
            if jogador.colliderect(mapa[mapaAtual]["objeto"]):
                mapa[mapaAtual].pop("objeto")
                enig = True
                
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
    else:
        overlay = pg.Surface(tamanhoTela)
        overlay.fill((0, 0, 0))
        janela.blit(overlay, (0, 0))

        txt = fonte.render(texto, True, (255,255,255))
        janela.blit(txt, (tamanhoTela[x]*0.5, tamanhoTela[y]*0.7))

        
        enigma = fonte.render(mapa[mapaAtual]["enigma"], True, (255,255,255))
        janela.blit(enigma, (tamanhoTela[x]*0.5, tamanhoTela[y]*0.5))

        
        #capturar texto digitado
        #print(eventos)
        for evento in eventos:
            if evento.type == pg.KEYDOWN:
                print("a")
                texto += evento.unicode
            
            
                

        pg.display.flip() 

    if teclas[pg.K_UP] and not colisaoCima:
        jogador.y -= velocidade
    if teclas[pg.K_DOWN] and not colisaoBaixo:
        jogador.y += velocidade
    if teclas[pg.K_RIGHT] and not colisaoDireita:
        jogador.x += velocidade 
    if teclas[pg.K_LEFT] and not colisaoEsquerdo:
        jogador.x -= velocidade
    if teclas[pg.K_k]:
        enig = False

    pg.display.flip()

