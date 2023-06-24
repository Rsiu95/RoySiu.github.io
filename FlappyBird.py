import random
import pygame
from pygame.locals import * 
import sys

pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height), SRCALPHA)
clock = pygame.time.Clock()
FPS = 60

pipe_frequency = 2000  # Time interval between sets of pipes (in milliseconds)
last_pipe_time = pygame.time.get_ticks()  # Time when the last set of pipes was displayed

bird_image = pygame.image.load("C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/FlappyBird/Images/chris.png").convert_alpha()
bird_image = pygame.transform.scale(bird_image, (50, 50))
bird_rect = bird_image.get_rect()
bird_rect.center = (width // 2, height // 2)

background = pygame.image.load("C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/FlappyBird/Images/Background.png")
background = pygame.transform.scale(background,(width, height))

bird_width = bird_rect.width
bird_height = bird_rect.height

pipe_gap = 200
pipe_x = width
pipe_height = random.randint(bird_height, height - pipe_gap - bird_height)

bird_movement = 0  # Vertical movement of the bird
bird_gravity = 0.5  # Gravity affecting the bird's fall
jump_height = 10  # Height of each jump

game_over_font = pygame.font.Font(None, 30)  # Font for "Game Over" text

spray_image = pygame.image.load("C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/FlappyBird/Images/spray.png").convert_alpha()
spray_image = pygame.transform.scale(spray_image, (bird_width, pipe_height))
spray_bottom_rect = spray_image.get_rect()
spray_top_rect = spray_image.get_rect()
spray_bottom_rect.midtop = (pipe_x, pipe_height + pipe_gap)
spray_top_rect.midbottom = (pipe_x, pipe_height)

start_game_flag = False
game_over_flag = False

def check_collision():
    if bird_rect.colliderect(spray_bottom_rect) or bird_rect.colliderect(spray_top_rect):
        return True
    if bird_rect.top <= 0 or bird_rect.bottom >= height:
        return True
    return False

def start_game():
    global start_game_flag, bird_movement, pipe_x
    start_game_flag = True
    bird_movement = 0
    pipe_x = width

def game_over():
    global game_over_flag
    game_over_flag = True

def reset_game():
    global start_game_flag, game_over_flag, bird_movement, pipe_x, pipe_width, spray_image
    bird_rect.center = (width // 2, height // 2)
    pipe_x = width
    bird_movement = 0
    start_game_flag = False
    game_over_flag = False
    pipe_height = random.randint(bird_height + 100, height - pipe_gap - bird_height - 100)
    spray_image = pygame.image.load("C:/Users/RSiu9/OneDrive/Documents/GitHub/RoySiu.github.io/FlappyBird/Images/spray.png").convert_alpha()
    spray_image = pygame.transform.scale(spray_image, (bird_width + 100, pipe_height))
    spray_bottom_rect.midtop = (pipe_x, pipe_height + pipe_gap)
    spray_top_rect.midbottom = (pipe_x, pipe_height)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if not start_game_flag:
            if event.type == KEYDOWN and event.key == K_SPACE:
                start_game()

        elif game_over_flag:
            if event.type == KEYDOWN and event.key == K_SPACE:
                reset_game()

        elif event.type == KEYDOWN and event.key == K_SPACE:
            if not check_collision():
                bird_movement = -jump_height

    screen.blit(background,(0,0))
    current_time = pygame.time.get_ticks()  # Current time
    if current_time - last_pipe_time >= pipe_frequency:
        last_pipe_time = current_time  # Update the last pipe time
        pipe_height = random.randint(bird_height, height - pipe_gap - bird_height)
        pipe_x = width  # Start the pipe at the right edge of the screen

    if start_game_flag:
        # Update bird's vertical position
        bird_movement += bird_gravity
        bird_rect.y += bird_movement

        # Check collision
        if check_collision() or bird_rect.bottom >= height:
            game_over_flag = True

        # Check if the bird reaches the top or bottom of the screen
        if bird_rect.top <= 0:
            bird_rect.top = 0
            game_over_flag = True
        elif bird_rect.bottom >= height:
            bird_rect.bottom = height
            game_over_flag = True

        # Update pipe position
        if not game_over_flag:
            pipe_x -= 2

        # Check if pipe has gone off the screen
        if pipe_x < -bird_width:
            pipe_x = width

        # Update spray image position
        spray_bottom_rect.x -= 2
        spray_top_rect.x -= 2

        # Check if spray image has gone off the screen
        if spray_bottom_rect.right <= 0:
            spray_bottom_rect.left = width
            spray_top_rect.left = width

        # Draw bird
        screen.blit(bird_image, bird_rect)

        # Draw spray images
        screen.blit(pygame.transform.flip(spray_image, False, True), spray_top_rect)
        screen.blit(spray_image, spray_bottom_rect)

        # Draw game over text if game over
        if game_over_flag:
            game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
            screen.blit(game_over_text,
                        (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
            restart_text = game_over_font.render("Press SPACEBAR to restart", True, (255, 0, 0))
            screen.blit(restart_text,
                        (width // 2 - restart_text.get_width() // 2, height // 2 + restart_text.get_height()))

    else:
        # Draw start menu text
        start_text = game_over_font.render("Press SPACEBAR to start", True, (255, 0, 0))
        screen.blit(start_text, (width // 2 - start_text.get_width() // 2, height // 2 - start_text.get_height() // 2))

    pygame.display.update()
    clock.tick(FPS)
