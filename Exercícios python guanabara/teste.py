import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Obtenha as dimensões da tela do dispositivo
largura, altura = pygame.display.Info().current_w, pygame.display.Info().current_h

# Configurações da tela em modo de tela cheia
tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
pygame.display.set_caption("Animação de Bomba Explodindo")

# Cores
preto = (0, 0, 0)

# Carregue imagens da explosão (você precisa de imagens reais para isso)
explosao_frames = []
for i in range(1, 6):
    img = pygame.image.load(f'bomba.png')  # Substitua pelos nomes reais dos arquivos
    explosao_frames.append(img)

frame_atual = 0
tempo_anterior = pygame.time.get_ticks()

# Loop principal
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:  # Pressionar a tecla "Esc" para sair
                running = False

    tempo_atual = pygame.time.get_ticks()

    if tempo_atual - tempo_anterior > 100:  # Controla a taxa de quadros (100 milissegundos)
        tela.fill(preto)  # Preenche a tela com preto
        tela.blit(explosao_frames[frame_atual], (100, 100))  # Desenha o quadro atual
        pygame.display.flip()  # Atualiza a tela
        frame_atual += 1
        if frame_atual >= len(explosao_frames):
            frame_atual = 0
        tempo_anterior = tempo_atual

# Encerra o Pygame e fecha a janela
pygame.quit()
sys.exit()
