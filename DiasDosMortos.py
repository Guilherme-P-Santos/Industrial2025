import  pygame as pg 

janelaY = 850
janelaX = 1500

x = 0
y = 1

pg.init()
tamanhoTela = pg.display.get_desktop_sizes()[0]
print(tamanhoTela)
janela = pg.display.set_mode(tamanhoTela)

velocidade = 9
jY = 500
jX = 500

jogador = pg.Rect(jX,jY, 100, 100)

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
                      pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y]),]},

        {"saidas": {"S3Cima" : pg.Rect(0,0,tamanhoTela[x],1)}, 
          "paredes": [pg.Rect(0, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]),
                      pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.03 ,1600, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y])]},

        {"saidas": {"S4Cima" : pg.Rect(0,0,tamanhoTela[x],1)}, 
          "paredes": [pg.Rect(0, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, 0, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]),
                      pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.03 ,1600, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y])]},


        {"saidas" : {"S5Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),"S5Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]), 
                      pg.Rect(0,0,1600, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)]},

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
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)]},

        {"saidas" : {"S7Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),
                     "S7Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),
                     "S7Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(0 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)]},
        
        {"saidas" : {"S8Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),
                     "S8Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(0 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y])]},

        {"saidas" : {"S9TP" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05)},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]),
                      pg.Rect(0,tamanhoTela[y] - tamanhoTela[x] * 0.03 ,1600, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.97,0,tamanhoTela[x] * 0.03, tamanhoTela[y])]},

        {"saidas" : {"S10Baixo" : pg.Rect(0,tamanhoTela[y],tamanhoTela[x],1),"S10Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0,0,tamanhoTela[x] * 0.03, tamanhoTela[y]), 
                      pg.Rect(0,0,1600, tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)]},

        {"saidas" : {"S11Direita" : pg.Rect(tamanhoTela[x], 0, 1, tamanhoTela[y]), 
                     "S11Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),
                     "S11TP" : pg.Rect(tamanhoTela[x] * 0.5, tamanhoTela[y] * 0.5, tamanhoTela[x]*0.05, tamanhoTela[x] * 0.05)},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(0 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(tamanhoTela[x] * 0.97 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4)]},

        {"saidas" : {"S12Esquerda" : pg.Rect(0, 0, 1, tamanhoTela[y]),},
         "paredes" : [pg.Rect(0, 0, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(0, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x], tamanhoTela[x] * 0.03), 
                      pg.Rect(tamanhoTela[x] * 0.6, tamanhoTela[y] - tamanhoTela[x] * 0.03, tamanhoTela[x] * 0.4, tamanhoTela[x] * 0.03), 
                      pg.Rect(0 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.3), 
                      pg.Rect(0 , tamanhoTela[y] * 0.6, tamanhoTela[x] * 0.03, tamanhoTela[y] * 0.4),
                      pg.Rect(tamanhoTela[x] * 0.97 , 0, tamanhoTela[x] * 0.03, tamanhoTela[y])]},
        
        
]

add = janela.fill
loop = True
clock = pg.time.Clock()


mapaAtual = 0

while loop:
    clock.tick(60)
    teclas = pg.key.get_pressed()


    for evento in pg.event.get():
        if evento.type == pg.QUIT or teclas[pg.K_x]:
            loop = False

    add((0,0,0))

    add((255,255,255),jogador)

    colisaoCima = False
    colisaoBaixo = False
    colisaoDireita = False
    colisaoEsquerdo = False

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

            elif k == "S9TP":
                mapaAtual = 10

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
            elif k == "S11TP":
                mapaAtual = 8

            elif k == "S12Esquerda":
                mapaAtual = 10
                jogador.x = tamanhoTela[x] - 100
            
            

    for saida in mapa[mapaAtual]["saidas"].values():
        add((0,255,0), saida)

    

    if teclas[pg.K_UP] and not colisaoCima:
        jogador.y -= velocidade
    if teclas[pg.K_DOWN] and not colisaoBaixo:
        jogador.y += velocidade
    if teclas[pg.K_RIGHT] and not colisaoDireita:
        jogador.x += velocidade 
    if teclas[pg.K_LEFT] and not colisaoEsquerdo:
        jogador.x -= velocidade

    pg.display.flip()
