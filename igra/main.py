import pygame
import sys

# Инициализация Pygame
pygame.init()

# Параметры экрана
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Крестики-нолики")

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)

# Размер клетки
cell_size = width // 3

# Игровое поле
board = [[' ' for _ in range(3)] for _ in range(3)]

# Рисование сетки
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, white, (i * cell_size, 0), (i * cell_size, height), 2)
        pygame.draw.line(screen, white, (0, i * cell_size), (width, i * cell_size), 2)

# Отрисовка крестика или нолика в ячейке
def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 100)
    text = font.render(symbol, True, white)
    text_rect = text.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2))
    screen.blit(text, text_rect)

# Определение победителя
def check_winner():
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

# Основной игровой цикл
def main():
    current_player = 'X'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // cell_size
                clicked_col = mouseX // cell_size

                # Проверка, что ячейка свободна перед ходом
                if board[clicked_row][clicked_col] == ' ':
                    board[clicked_row][clicked_col] = current_player

                    if check_winner():
                        print(f'Игрок {current_player} выиграл!')
                        pygame.quit()
                        sys.exit()

                    current_player = 'O' if current_player == 'X' else 'X'

        screen.fill(black)
        draw_grid()

        for row in range(3):
            for col in range(3):
                if board[row][col] != ' ':
                    draw_symbol(row, col, board[row][col])

        pygame.display.flip()

if __name__ == "__main__":
    main()
