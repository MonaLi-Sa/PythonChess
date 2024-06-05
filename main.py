import pygame
from board import Board

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Main function
def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    selected_piece = None
    valid_moves = {}

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
                    # Get mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Convert mouse position to board coordinates
                    col = mouse_x // (WIDTH // 8)
                    row = mouse_y // (HEIGHT // 8)
                    if selected_piece:
                        if (row, col) in valid_moves:
                            board.board[row][col] = selected_piece
                            selected_piece = None
                            valid_moves.clear()
                        else:
                            selected_piece = None
                            valid_moves.clear()
                    else:
                        piece = board.board[row][col]
                        if piece != ' ':
                            selected_piece = board.board[row][col]
                            valid_moves = board.get_valid_moves(row, col)

        # Update display
        WIN.fill(WHITE)
        board.draw(WIN)
        if selected_piece:
            draw_valid_moves(WIN, valid_moves)
        pygame.display.update()

    pygame.quit()

def draw_valid_moves(win, valid_moves):
    for move in valid_moves:
        row, col = move
        pygame.draw.circle(win, GREEN, (col * (WIDTH // 8) + (WIDTH // 16), row * (HEIGHT // 8) + (HEIGHT // 16)), 15)

if __name__ == "__main__":
    main()
