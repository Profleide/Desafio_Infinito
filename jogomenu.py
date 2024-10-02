import pygame
import random

# Inicializa o PyGame
pygame.init()

# Dimensões da tela
tela_largura = 800
tela_altura = 600
tela = pygame.display.set_mode((tela_largura, tela_altura))

# Título da janela
pygame.display.set_caption('Desafio Infinito')

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)  # Cor do jogador
VERMELHO = (255, 0, 0)  # Cor dos inimigos
PRETO = (0, 0, 0)

# Relógio para controlar FPS
clock = pygame.time.Clock()

# Fonte para exibir o texto na tela
fonte = pygame.font.SysFont(None, 55)

# Função para desenhar o jogador
def desenhar_jogador(x, y):
    pygame.draw.rect(tela, AZUL, [x, y, 50, 50])  # Jogador será um quadrado azul

# Função para mover inimigos
def mover_inimigos(inimigos):
    for inimigo in inimigos:
        inimigo['y'] += inimigo['velocidade']
        if inimigo['y'] > tela_altura:
            inimigo['y'] = -50
            inimigo['x'] = random.randint(0, tela_largura - 50)
        pygame.draw.rect(tela, VERMELHO, [inimigo['x'], inimigo['y'], 50, 50])  # Inimigos serão quadrados vermelhos

# Função para exibir a pontuação
def mostrar_pontuacao(pontuacao):
    texto = fonte.render(f'Pontuação: {pontuacao}', True, PRETO)
    tela.blit(texto, [10, 10])

# Função para verificar colisões
def verificar_colisao(jogador_x, jogador_y, inimigos):
    for inimigo in inimigos:
        if jogador_x < inimigo['x'] + 50 and jogador_x + 50 > inimigo['x'] and jogador_y < inimigo['y'] + 50 and jogador_y + 50 > inimigo['y']:
            return True
    return False

# Função principal do jogo
def iniciar_jogo():
    jogador_x = tela_largura / 2 - 25  # Posição inicial do jogador (centralizada horizontalmente)
    jogador_y = tela_altura - 60       # Posição inicial do jogador (perto do fundo da tela)
    velocidade_jogador = 5             # Velocidade de movimento do jogador
    pontuacao = 0                      # Inicializa a pontuação

    # Criar inimigos em posições aleatórias
    inimigos = [{'x': random.randint(0, tela_largura - 50), 'y': -50, 'velocidade': random.randint(2, 5)} for _ in range(5)]
    
    jogando = True
    while jogando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False

        # Captura as teclas pressionadas
        teclas = pygame.key.get_pressed()

        # Movimentação do jogador
        if teclas[pygame.K_LEFT] and jogador_x > 0:  # Movimento para a esquerda (impede de sair da tela)
            jogador_x -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and jogador_x < tela_largura - 50:  # Movimento para a direita (impede de sair da tela)
            jogador_x += velocidade_jogador

        # Atualiza a tela
        tela.fill(BRANCO)  # Limpa a tela a cada frame
        desenhar_jogador(jogador_x, jogador_y)  # Desenha o jogador na nova posição
        mover_inimigos(inimigos)  # Movimenta e desenha os inimigos

        # Aumenta a pontuação com o tempo
        pontuacao += 1
        mostrar_pontuacao(pontuacao)  # Exibe a pontuação

        # Verifica colisão
        if verificar_colisao(jogador_x, jogador_y, inimigos):
            jogando = False

        pygame.display.update()  # Atualiza a tela

        # Controla a taxa de frames por segundo (FPS)
        clock.tick(60)

    mostrar_game_over(pontuacao)

# Função para mostrar a tela de "Game Over" e opção de reiniciar
def mostrar_game_over(pontuacao):
    tela.fill(BRANCO)
    mensagem = fonte.render(f'Game Over! Pontuação: {pontuacao}', True, PRETO)
    reiniciar_texto = fonte.render('Pressione R para Reiniciar', True, PRETO)
    tela.blit(mensagem, [tela_largura / 2 - 250, tela_altura / 2 - 50])
    tela.blit(reiniciar_texto, [tela_largura / 2 - 250, tela_altura / 2])
    pygame.display.update()

    reiniciar = False
    while not reiniciar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                reiniciar = True
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    iniciar_jogo()

# Função para exibir o menu inicial
def mostrar_menu_inicial():
    tela.fill(BRANCO)
    titulo = fonte.render('Desafio Infinito', True, PRETO)
    iniciar_jogo_texto = fonte.render('Pressione ENTER para Iniciar', True, PRETO)
    sair_texto = fonte.render('Pressione ESC para Sair', True, PRETO)
    
    tela.blit(titulo, [tela_largura / 2 - 150, tela_altura / 2 - 100])
    tela.blit(iniciar_jogo_texto, [tela_largura / 2 - 250, tela_altura / 2])
    tela.blit(sair_texto, [tela_largura / 2 - 200, tela_altura / 2 + 100])
    
    pygame.display.update()

    menu = True
    while menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Tecla Enter para iniciar
                    menu = False
                    iniciar_jogo()
                if evento.key == pygame.K_ESCAPE:  # Tecla Esc para sair
                    pygame.quit()
                    exit()

# Iniciar no menu inicial
mostrar_menu_inicial()
