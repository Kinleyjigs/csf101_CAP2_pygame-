# Import necessary libraries
import pygame
import random
import sys

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 700 # Define the game window dimensions
GRID_SIZE = 30 # Size of each grid cell
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE # Calculate grid dimensions
WHITE = (255, 255, 255) #Define colors
BLACK = (0, 0, 0)

# Tetromino shapes and their rotations
SHAPES = [ # Define various tetromino shapes
    [[1, 1, 1, 1]], # I-shape
    [[1, 1], [1, 1]], # O-shape
    [[1, 1, 1], [0, 1, 0]], # T-shape
    [[1, 1, 1], [1, 0, 0]],  # L-shape
    [[1, 1, 1], [0, 0, 1]], # J-shape
    [[1, 1, 1], [0, 1, 0]], # S-shape
    [[1, 1, 1], [0, 0, 1]] # Z-shape
]

# Define colors for tetromino shapes
SHAPE_COLORS = [
    (0, 255, 255),  # Cyan
    (0, 0, 255),  # Blue
    (128, 0, 128),  # Purple
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),  # Green
    (255, 0, 0)  # Red
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create game window
pygame.display.set_caption("Tetris Clone")# Set the window title

# Initialize game variables
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Set the score to zero when the program starts
score = 0

# Load the saved high score and set it to zero
def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0

high_score = load_high_score()
if score > high_score:
    high_score = score
    with open("high_score.txt", "w") as file:
        try:
            file.write(str(high_score))
        except Exception as e:
            print(f"Error writing high score: {e}")

# Functions
def generate_shape():
    if not shape_list:
        shape_list.extend(list(zip(SHAPES, SHAPE_COLORS)))
    shape, color = random.choice(shape_list)
    shape_list.remove((shape, color))
    return shape, color, (GRID_WIDTH - len(shape[0])) // 2, 0

def draw_scores():
    font = pygame.font.Font(None, 36)
    current_score_text = font.render(f"Score: {score}", True, WHITE)
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(current_score_text, (10, 10))
    screen.blit(high_score_text, (10, 40))

def is_valid_position(shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                if x + col < 0 or x + col >= GRID_WIDTH or y + row >= GRID_HEIGHT or grid[y + row][x + col]:
                    return False
    return True

def place_shape(shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                grid[y + row][x + col] = current_color

def clear_lines():
    global grid, score, high_score
    full_lines = [i for i, row in enumerate(grid) if all(row)]
    for line in full_lines:
        grid.pop(line)
        grid.insert(0, [0] * GRID_WIDTH)
    score += len(full_lines)

    if score > high_score:
        high_score = score
        with open("high_score.txt", "w") as file:
            try:
                file.write(str(high_score))
            except Exception as e:
                print(f"Error writing high score: {e}")

def rotate(shape, direction):
    if direction == "clockwise":
        return [[shape[j][i] for j in range(len(shape))] for i in range(len(shape[0]) - 1, -1, -1)]
    elif direction == "counterclockwise":
        return [[shape[j][i] for j in range(len(shape) - 1, -1, -1)] for i in range(len(shape[0]) - 1, -1, -1)]
    return shape

def display_navigation_instructions():
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("TETRIS GAME", True, WHITE)
    instruction_text = font.render("Use Arrow Keys to Move", True, WHITE)
    rotate_text = font.render("Up Arrow to Rotate", True, WHITE)
    pause_text = font.render("Press 'Space' to Pause", True, WHITE)
    start_text = font.render("Press 'Space' to Start", True, WHITE)
    screen.blit(title_text, (30, 100))
    screen.blit(instruction_text, (50, 200))
    screen.blit(rotate_text, (90, 250))
    screen.blit(pause_text, (80, 300))
    screen.blit(start_text, (80, 400))
    pygame.display.update()
    waiting_for_start = True

    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting_for_start = False
                screen.fill(BLACK)

# Display navigation instructions
display_navigation_instructions()

def display_game_over():
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("GAME OVER", True, (172, 21, 16))
    restart_font = pygame.font.Font(None, 36)
    restart_text = restart_font.render("Press Q to quit ", True, (255, 255, 255))
    play_again_text = restart_font.render("Press Space to play again", True, (255, 255, 255))

    screen.blit(game_over_text, (70, SCREEN_HEIGHT // 2 - 62))
    screen.blit(restart_text, (90, SCREEN_HEIGHT // 2 + 20))
    screen.blit(play_again_text, (90, SCREEN_HEIGHT // 2 + 60))
    pygame.display.update()

# Initialize game variables
reset_game = False
score = 0
high_score = 0
shape_list = list(zip(SHAPES, SHAPE_COLORS))  # Define shape_list here
reset_game = False

# Main game loop
clock = pygame.time.Clock()
game_over = False
is_paused = False
score = 0  # Initialize score

current_shape, current_color, current_shape_x, current_shape_y = generate_shape()


def draw_pause_screen():
    font = pygame.font.Font(None, 72)
    pause_text = font.render("PAUSED", True, WHITE)
    screen.blit(pause_text, (150, SCREEN_HEIGHT // 2 - 36))

score = 0
draw_scores()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if not is_paused:
        if keys[pygame.K_LEFT]:
            if is_valid_position(current_shape, current_shape_x - 1, current_shape_y):
                current_shape_x -= 1
        elif keys[pygame.K_RIGHT]:
            if is_valid_position(current_shape, current_shape_x + 1, current_shape_y):
                current_shape_x += 1
        elif keys[pygame.K_DOWN]:
            if is_valid_position(current_shape, current_shape_x, current_shape_y + 1):
                current_shape_y += 1
        elif keys[pygame.K_UP]:
            rotated_shape = rotate(current_shape, "clockwise")
            if is_valid_position(rotated_shape, current_shape_x, current_shape_y):
                current_shape = rotated_shape

    if keys[pygame.K_SPACE]:
        is_paused = not is_paused

    if not is_paused:
        if is_valid_position(current_shape, current_shape_x, current_shape_y + 1):
            current_shape_y += 1
        else:
            place_shape(current_shape, current_shape_x, current_shape_y)
            clear_lines()
            current_shape, current_color, current_shape_x, current_shape_y = generate_shape()

            if not is_valid_position(current_shape, current_shape_x, current_shape_y):
                display_game_over()
                pygame.display.update()

                waiting_for_decision = True
                while waiting_for_decision:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()
                            if event.key == pygame.K_SPACE:
                                grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
                                game_over = False
                                current_shape, current_color, current_shape_x, current_shape_y = generate_shape()
                                waiting_for_decision = False
                                score = 0  # Reset the score to zero
                                screen.fill(BLACK)
                pygame.display.update()

    screen.fill(BLACK)

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x]:
                pygame.draw.rect(screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 2)

    for row in range(len(current_shape)):
        for col in range(len(current_shape[row])):
            if current_shape[row][col]:
                pygame.draw.rect(screen, current_color, ((current_shape_x + col) * GRID_SIZE, (current_shape_y + row) * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, BLACK, ((current_shape_x + col) * GRID_SIZE, (current_shape_y + row) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 2)

    if is_paused:
        draw_pause_screen()

    draw_scores()
    pygame.display.update()
    clock.tick(6)





