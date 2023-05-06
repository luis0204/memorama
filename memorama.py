import pygame
import random

# Configuraciones del juego
WIDTH = 800
HEIGHT = 600
FPS = 30
CARD_WIDTH = 100
CARD_HEIGHT = 100
CARD_PADDING = 10
CARD_BACK_COLOR = (60, 60, 60)
CARD_FRONT_COLOR = (255, 255, 255)
FONT_NAME = 'arial'

# Crear una lista de pares de conjunciones correlativas
correlatives = ['either...or', 'neither...nor', 'not only...but also', 'both...and', 'whether...or']
card_pairs = correlatives + correlatives

# Inicializar Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de memoria de conjunciones correlativas en inglés")
clock = pygame.time.Clock()

# Cargar las fuentes
font = pygame.font.SysFont(FONT_NAME, 24)
big_font = pygame.font.SysFont(FONT_NAME, 48)

# Cargar los sonidos
pygame.mixer.music.load('background_music.mp3')
flip_sound = pygame.mixer.Sound('flip_sound.wav')
match_sound = pygame.mixer.Sound('match_sound.wav')
win_sound = pygame.mixer.Sound('win_sound.wav')

# Función para crear la superficie de una carta
def create_card_surface(text):
    card_surface = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
    card_surface.fill(CARD_FRONT_COLOR)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(CARD_WIDTH/2, CARD_HEIGHT/2))
    card_surface.blit(text_surface, text_rect)
    return card_surface

# Función para crear el tablero de juego
def create_board(card_pairs):
    board = []
    for i, card_text in enumerate(card_pairs):
        card_surface = create_card_surface(card_text)
        x = CARD_PADDING + (CARD_PADDING + CARD_WIDTH) * (i % 5)
        y = CARD_PADDING + (CARD_PADDING + CARD_HEIGHT) * (i // 5 + 1)
        board.append([card_text, card_surface, (x, y)])
    return board

# Función para mostrar el tablero
def show_board(board):
    for card_text, card_surface, (x, y) in board:
        if card_surface != None:
            screen.blit(card_surface, (x, y))

# Función para voltear una carta
def flip_card(board, card_index):
    card_text, card_surface, card_pos = board[card_index]
    if card_surface == None:
        return False
    flip_sound.play()
    card_back_surface = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
    card_back_surface.fill(CARD_BACK_COLOR)
    screen.blit(card_back_surface, card_pos)
    pygame.display.flip()
    pygame.time.wait(500)
    screen.blit(card_surface, card_pos)
    pygame.display.flip()
    board[card_index] = (card_text, None, card_pos)
    return True

# Función para jugar el juego
def play_game():
    # Crear el tablero de juego
    board = create_board(card_pairs)

    # Mostrar el mensaje de bienvenida
    title_text = big_font.render("Juego de memoria de conjunciones correlativas en inglés", True, (255, 255, 255))
    
