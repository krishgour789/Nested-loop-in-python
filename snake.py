# import pygame
# import random
# import sys

# # Initialize pygame
# pygame.init()

# # Screen settings
# WIDTH, HEIGHT = 600, 400
# CELL_SIZE = 20
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Snake Game")

# # Colors
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# WHITE = (255, 255, 255)

# # Snake & Food
# snake = [(100, 100)]
# direction = (CELL_SIZE, 0)  # moving right
# food = (200, 200)
# score = 0

# # Font
# font = pygame.font.SysFont(None, 30)

# def draw_snake():
#     for block in snake:
#         pygame.draw.rect(screen, GREEN, (*block, CELL_SIZE, CELL_SIZE))

# def draw_food():
#     pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

# def show_score():
#     text = font.render(f"Score: {score}", True, WHITE)
#     screen.blit(text, (10, 10))

# # Main Game Loop
# clock = pygame.time.Clock()
# while True:
#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
#                 direction = (0, -CELL_SIZE)
#             elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
#                 direction = (0, CELL_SIZE)
#             elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
#                 direction = (-CELL_SIZE, 0)
#             elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
#                 direction = (CELL_SIZE, 0)

#     # Move snake
#     new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
#     snake.insert(0, new_head)

#     # Check food collision
#     if snake[0] == food:
#         score += 1
#         food = (random.randrange(0, WIDTH, CELL_SIZE),
#                 random.randrange(0, HEIGHT, CELL_SIZE))
#     else:
#         snake.pop()  # remove last block if no food eaten

#     # Check collisions (wall or itself)
#     if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
#         snake[0][1] < 0 or snake[0][1] >= HEIGHT or
#         snake[0] in snake[1:]):
#         print("Game Over! Final Score:", score)
#         pygame.quit()
#         sys.exit()

#     # Draw everything
#     screen.fill(BLACK)
#     draw_snake()
#     draw_food()
#     show_score()
#     pygame.display.flip()

#     # Control speed
#     clock.tick(functions.py10)
