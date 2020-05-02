import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
#aqui cria uma janela 500 por 500

pygame.display.set_caption("Primeiro jogo")

#variaveis posicao do personagem

x = 50
y = 425
width = 20
height = 30
vel = 5

#abaixo variaveis para utilizar no personagem pulando - jump
isJump = False
jumpCount = 10

run = True
#o loop princial do jogo

while run:
        pygame.time.delay(100) #dara 0.1s de delay no jogo

        for event in pygame.event.get(): #neste loop é para pegar teclado e eventos mouse
                if event.type == pygame.QUIT:
                    run = False #termina o loop do jogo

        keys = pygame.key.get_pressed() #aqui ele pega o que for digitado

        if keys[pygame.K_LEFT] and x > vel: #a parte da condicao E é para que n passe da janela
            x -= vel

        if keys[pygame.K_RIGHT] and x < 500 - vel - width:
            x += vel

        if not(isJump): #checando se o usuario nao esta pulando

            if keys[pygame.K_UP] and y > vel: 
                    y -= vel

            if keys[pygame.K_DOWN] and y < 500 - vel - height:
                    y += vel
                    
            if keys[pygame.K_SPACE]:
                    isJump = True
        else:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
            else: #executa isso se o pulo estiver finalizado
                jumpCount = 10
                isJump = False
                #resetando as variaveis apos o pulo
        
        win.fill((0,0,0)) #preenche a tela com preto
        pygame.draw.rect(win, (255,0,0), (x, y, width, height))
        pygame.display.update() #atualiza a tela pra ver o retangulo
        
pygame.quit()
