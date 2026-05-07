import pygame

class Player: # cria uma classe de player e como ele vai ser

    def __init__(self):

        self.image = pygame.image.load("player.png").convert_alpha() # converter o player na imagem e remover o fundo de png

        self.image = pygame.transform.scale(self.image, (64,64)) # tamanho do player

        self.x = 568 # posiçoes de spawn do player
        self.y = 418

        self.vel = 1.5 # velocidade

    def mover(self): # binds para locomoçao/movimento do player

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_a]: # esquerda
            self.x -= self.vel

        if teclas[pygame.K_d]: # direita
            self.x += self.vel

        if teclas[pygame.K_w]: # cima
            self.y -= self.vel

        if teclas[pygame.K_s]: # baixo
            self.y += self.vel

    def desenhar(self, tela): # desenha o player na tela

        tela.blit(self.image, (self.x, self.y)) # desenha/cola a imagem do player nas posiçoes de X e Y