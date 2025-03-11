import pygame
import random

pygame.init()


COLUMNS, ROWS = 10, 20
BLOCK_SIZE = 30
WIDTH, HEIGHT = COLUMNS * BLOCK_SIZE, ROWS * BLOCK_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE_SKY = (135, 206, 250)
CLOUD = (240, 240, 240)
COLORS = [
    (0, 255, 255), (255, 255, 0), (128, 0, 128),
    (255, 165, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0)
]

# Score system
score = 0
font = pygame.font.SysFont('Arial', 30)

# Game state
game_over = False

# Track key presses for smooth movement
keys = {
    "left": False,
    "right": False,
    "down": False
}

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]]
]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def draw(self):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect(
                        (self.x + col_idx) * BLOCK_SIZE, (self.y + row_idx) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE
                    )
                    pygame.draw.rect(screen, self.color, rect)
                    pygame.draw.rect(screen, GRAY, rect, 2)

    def rotate(self):
        rotated_shape = list(zip(*self.shape[::-1]))
        if not check_collision(self, new_shape=rotated_shape):
            self.shape = rotated_shape

class Cloud:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 100)
        self.y = random.randint(0, HEIGHT // 4)
        self.speed = random.uniform(0.05, 0.1)  # Slower speed

    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = -100

    def draw(self):
        pygame.draw.ellipse(screen, CLOUD, (self.x, self.y, 80, 40))
        pygame.draw.ellipse(screen, CLOUD, (self.x + 30, self.y - 10, 60, 30))
        pygame.draw.ellipse(screen, CLOUD, (self.x - 30, self.y - 10, 60, 30))

clouds = [Cloud() for _ in range(3)]
board = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
current_tetromino = Tetromino()
fall_speed = 500
last_fall_time = pygame.time.get_ticks()
move_speed = 100  # Speed of horizontal movement (ms)
last_move_time = pygame.time.get_ticks()

def check_collision(tetromino, dx=0, dy=0, new_shape=None):
    shape = new_shape if new_shape else tetromino.shape
    for row_idx, row in enumerate(shape):
        for col_idx, cell in enumerate(row):
            if cell:
                new_x = tetromino.x + col_idx + dx
                new_y = tetromino.y + row_idx + dy
                if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or (new_y >= 0 and board[new_y][new_x] != BLACK):
                    return True
    return False

def lock_tetromino(tetromino):
    for row_idx, row in enumerate(tetromino.shape):
        for col_idx, cell in enumerate(row):
            if cell:
                board[tetromino.y + row_idx][tetromino.x + col_idx] = tetromino.color

def clear_rows():
    global board, score
    rows_to_clear = [i for i, row in enumerate(board) if all(cell != BLACK for cell in row)]
    for i in rows_to_clear:
        for _ in range(3):
            board[i] = [WHITE] * COLUMNS
            pygame.display.flip()
            pygame.time.delay(100)
            board[i] = [BLACK] * COLUMNS
            pygame.display.flip()
            pygame.time.delay(100)
        del board[i]
        board.insert(0, [BLACK for _ in range(COLUMNS)])
        score += 100

def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def draw_game_over():
    game_over_text = font.render(f"Game Over! Score: {score}", True, WHITE)
    play_again_text = font.render("Press Enter to Play Again", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 40))
    screen.blit(play_again_text, (WIDTH // 2 - play_again_text.get_width() // 2, HEIGHT // 2 + 10))

def reset_game():
    global board, current_tetromino, score, game_over, last_fall_time
    board = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
    current_tetromino = Tetromino()
    score = 0
    game_over = False
    last_fall_time = pygame.time.get_ticks()

running = True
while running:
    screen.fill(BLUE_SKY)
    for cloud in clouds:
        cloud.move()
        cloud.draw()

    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_RETURN:
                    reset_game()
            else:
                if event.key == pygame.K_LEFT:
                    keys["left"] = True
                if event.key == pygame.K_RIGHT:
                    keys["right"] = True
                if event.key == pygame.K_DOWN:
                    keys["down"] = True
                if event.key == pygame.K_UP:
                    current_tetromino.rotate()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys["left"] = False
            if event.key == pygame.K_RIGHT:
                keys["right"] = False
            if event.key == pygame.K_DOWN:
                keys["down"] = False

    if not game_over:
        if current_time - last_fall_time > fall_speed:
            if not check_collision(current_tetromino, dy=1):
                current_tetromino.y += 1
            else:
                lock_tetromino(current_tetromino)
                clear_rows()
                current_tetromino = Tetromino()
                if check_collision(current_tetromino):
                    game_over = True
            last_fall_time = current_time

        if current_time - last_move_time > move_speed:
            if keys["left"] and not check_collision(current_tetromino, dx=-1):
                current_tetromino.x -= 1
            if keys["right"] and not check_collision(current_tetromino, dx=1):
                current_tetromino.x += 1
            if keys["down"] and not check_collision(current_tetromino, dy=1):
                current_tetromino.y += 1
            last_move_time = current_time

        current_tetromino.draw()
        for y, row in enumerate(board):
            for x, color in enumerate(row):
                if color != BLACK:
                    rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(screen, color, rect)
                    pygame.draw.rect(screen, GRAY, rect, 2)

    draw_score()
    if game_over:
        draw_game_over()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()