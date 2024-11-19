# main.py
import pygame
import sys
from consts import MUSICA_FUNDO, SOM_PASSOS  # Importa as constantes
from game import tela_inicio, carregar_recursos  # Importa a função carregar_recursos

# Inicializa o pygame
pygame.init()
pygame.mixer.init()

# Carrega a música de fundo
try:
    pygame.mixer.music.load(MUSICA_FUNDO)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)
except pygame.error as e:
    print(f"Erro ao carregar a música: {e}")

# Carrega o som dos passos
passos = pygame.mixer.Sound(SOM_PASSOS)

# Inicia o jogo com a tela de início
if __name__ == "__main__":
    recursos = carregar_recursos()  # Carrega os recursos antes de iniciar a tela
    tela_inicio(recursos)

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Se a tecla "S" for pressionada
                    if pygame.mixer.music.get_busy():  # Se a música estiver tocando
                        pygame.mixer.music.stop()  # Para a música
                    else:
                        pygame.mixer.music.play(-1)  # Se a música não estiver tocando, inicia novamente

        # Aqui você pode adicionar a lógica do jogo, como atualizar e desenhar o personagem

        pygame.display.flip()  # Atualiza a tela