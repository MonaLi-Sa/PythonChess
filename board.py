import pygame
import os

# Constants
WIDTH, HEIGHT = 400, 400
SQUARE_SIZE = WIDTH // 8
BORDER = 20

class Board:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        self.selected_piece = None
        self.load_images()

    def load_images(self):
        self.piece_images = {}
        piece_names = {'k': 'king', 'q': 'queen', 'b': 'bishop', 'n': 'knight', 'r': 'rook', 'p': 'pawn'}
        colors = ['white', 'black']
        for color in colors:
            for piece in piece_names.keys():
                path = os.path.join('pieces', f'{piece}_{color}.png')
                if os.path.exists(path):
                    self.piece_images[f'{piece}_{color}'] = pygame.image.load(path)
                else:
                    print(f"Error: Image not found for {piece}_{color}")

    def draw(self, win):
        for row in range(8):
            for col in range(8):
                color = (238, 238, 210) if (row + col) % 2 == 0 else (118, 150, 86)
                pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.board[row][col]
                if piece != ' ':
                    # Draw piece
                    piece_color = 'white' if piece.isupper() else 'black'
                    piece_name = f"{piece.lower()}_{piece_color}"
                    if piece_name in self.piece_images:
                        piece_image = self.piece_images[piece_name]
                        win.blit(piece_image, (col * SQUARE_SIZE, row * SQUARE_SIZE))
                    else:
                        print(f"Error: Image not found for {piece_name}")
