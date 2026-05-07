import pygame
from player import Player

pygame.init() # inicia o jogo

tela = pygame.display.set_mode((1200,900))

player = Player() # cria um jogador e guarde ele na variavel player

game = True # game sendo sempre true = jogo sempre vai estar funcionando

while game:

    for evento in pygame.event.get(): # junta todos os eventos do jogo
        if evento.type == pygame.QUIT: # se o jogador do jogo clicar no X da tela
            game = False

    player.mover()

    tela.fill((0,0,0)) # executa a funçao mover do player

    player.desenhar(tela) # desenha o jogador na tela

    pygame.display.flip() # mostra na tela tudo que foi renderizado a cada comando ,tipo WASD,  naquele frame e atualiza os frames

pygame.quit()