# personagem.py
import pygame
from consts import PERSONAGEM_X, PERSONAGEM_Y, PERSONAGEM_LARGURA, PERSONAGEM_ALTURA

class Personagem:
    def __init__(self, x=PERSONAGEM_X, y=PERSONAGEM_Y):
        self.x = x
        self.y = y
        self.velocidade = 5
        self.direcao = 'direita'
        self.moving = False

        # Carregar as imagens do personagem
        self.sprite_parado = pygame.image.load("assets/Recursos/sprites_Ella_prota-standing.png")
        self.sprite_moving1 = pygame.image.load("assets/Recursos/sprites_Ella_prota-moving1.png")
        self.sprite_moving2 = pygame.image.load("assets/Recursos/sprites_Ella_prota-moving2.png")
        self.sprites_direita = [self.sprite_moving1, self.sprite_moving2]
        self.sprites_esquerda = [pygame.transform.flip(self.sprite_moving1, True, False),
                                 pygame.transform.flip(self.sprite_moving2, True, False)]

        self.sprite_atual = self.sprite_parado
        self.frame_index = 0
        self.tempo_anterior = pygame.time.get_ticks()
        self.frame_rate = 200
        self.rect = pygame.Rect(self.x, self.y, PERSONAGEM_LARGURA, PERSONAGEM_ALTURA)

    def atualizar(self, teclas):
        if teclas[pygame.K_LEFT]:  # Seta esquerda
            self.x -= self.velocidade
            self.direcao = 'esquerda'
            self.moving = True
        elif teclas[pygame.K_RIGHT]:  # Seta direita
            self.x += self.velocidade
            self.direcao = 'direita'
            self.moving = True
        else:
            self.moving = False

        self.animar()
        self.rect.topleft = (self.x, self.y)  # Atualiza a posição do retângulo do personagem

    def animar(self):
        agora = pygame.time.get_ticks()
        if self.moving:
            if agora - self.tempo_anterior > self.frame_rate:
                self.tempo_anterior = agora
                self.frame_index = (self.frame_index + 1) % 2
                self.sprite_atual = self.sprites_direita[self.frame_index] if self.direcao == 'direita' else self.sprites_esquerda[self.frame_index]
        else:
            self.sprite_atual = self.sprite_parado

    def desenhar(self, tela):
        tela.blit(self.sprite_atual, (self.x, self.y))