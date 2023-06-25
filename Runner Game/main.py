import pygame
import sys
#import numpy
from random import randint


def display_score():
    current_time = (pygame.time.get_ticks() - start_time) // 1000 - start_time
    score_surface = game_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = ((screen_width // 2), (screen_height // 5)))
    #pygame.draw.rect(screen, '#c0e8ec', score_rect)
    #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface,score_rect)
    return current_time


# Initialise game
pygame.init()
game_active = True
start_time = 0

# Set main display variables
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set game name
pygame.display.set_caption('Pixel Runner')

# Set game Font
font_type = "Runner Game/font/Pixeltype.ttf"
font_size = 50
game_font = pygame.font.Font(font_type, font_size)

game_name = game_font.render('Pixel Runner', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400, 20))

game_message = game_font.render('Press space to run', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400, 320))

# Initialise score
score = 0

# Import images
sky_background = pygame.image.load("Runner Game/graphics/Sky.png").convert()
ground_background = pygame.image.load("Runner Game/graphics/ground.png").convert()

# Score text
#score_surface = game_font.render('Score: ', False, (64,64,64)) # render(text, (anti-aliasing (T/F), colour)
#score_rect = score_surface.get_rect(center = (screen_width // 2, screen_height // 8))
game_over_text = game_font.render("GAME OVER!", False, (64,64,64))
game_over_rect = game_over_text.get_rect(center = ((screen_width // 2), (screen_height // 8)))

# Snail
snail_surface = pygame.image.load('Runner Game/graphics/snail/snail1.png').convert_alpha()
snail_x_pos, snail_y_pos = 870, 300
snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, snail_y_pos))

# Fly
fly_surface = pygame.image.load('Runner Game/graphics/Fly/Fly2.png').convert_alpha()
fly_x_pos, fly_y_pos = 850, 176
fly_rect = fly_surface.get_rect(midbottom = (fly_x_pos, fly_y_pos))

#fly_surface2 = pygame.image.load('Runner Game/graphics/Fly/Fly1.png').convert_alpha()
#fly2_x_pos, fly2_y_pos = fly_x_pos, fly_y_pos
#fly2_rect = fly_surface2.get_rect()

# Player
player_surface = pygame.image.load('Runner Game/graphics/Player/player_walk_1.png').convert_alpha()
player_x_pos, player_y_pos = 300,300
player_rect = player_surface.get_rect(midbottom = (player_x_pos, player_y_pos))

player_stand = pygame.image.load('Runner Game/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# Gravity
gravity = 1
jump_height = 0

# Check size of sky background by converting from surface object to numpy array object
image_array = pygame.surfarray.array3d(player_surface)
print(image_array.shape)

# Initialise clock
clock = pygame.time.Clock()


# Main game loop
while True:
    # Check player input
    for event in pygame.event.get():
        # Check exit input
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    print("jump")
                    gravity = -20
                # if event.key == pygame.K_a:
                #     player_rect.x -= 5
                # if event.key == pygame.K_d:
                #     player_rect.x += 5
            
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_SPACE:
            #         jump_height = max(jump_height,0)
            #         gravity = -jump_height
            
            #Get mouse position with "event"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_init_pos = randint(800, 1000)
                fly_init_pos = randint(800, 1000)
                snail_rect.left = snail_init_pos
                fly_rect.left = fly_init_pos
                start_time = pygame.time.get_ticks() // 1000
                
    if game_active:
        # This will draw the image in order of top > bottom execution
        screen.blit(sky_background,(0,0)) # blit = block image transfer
        screen.blit(ground_background,(0,300))
        score = display_score()
        
        # Handle snail movement
        snail_exit_pos = randint(-10000, -72)
        snail_speed = randint(3,6) 
        if snail_rect.right <= snail_exit_pos:
            snail_rect.left = 800
        else:
            snail_rect.x -= snail_speed

        screen.blit(snail_surface,snail_rect)
        
        # Handle fly movement
        fly_speed = randint(4,7)
        fly_exit_pos = randint(-10000, -84)
        if fly_rect.right <= fly_exit_pos:
            fly_rect.left = 800
            fly_rect.top = randint(0, 176)
        else:
            fly_rect.x -= fly_speed
        
        screen.blit(fly_surface, fly_rect)

        # Handle player movement
        
        gravity += 1
        player_rect.y += gravity
        
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        elif player_rect.top <= 0:
            player_rect.top = 0
        
        screen.blit(player_surface, player_rect)   
    
        if player_rect.colliderect(snail_rect) or player_rect.colliderect(fly_rect):
            #screen.blit(game_over_text,game_over_rect)
            game_active = False
            
        #     Handle Score
        #    pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #    pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
        #    screen.blit(score_surface, score_rect)
    
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_over_text, game_over_rect)
        screen.blit(game_name, game_name_rect)
        score_message = game_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # Handle Collision and Game Over!
    
    # else:
    #     # Handle Score
    #     pygame.draw.rect(screen, '#c0e8ec', score_rect)
    #     pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
    #     screen.blit(score_surface, score_rect)
    
    # Get cursor position
    # cursor_position = pygame.mouse.get_pos()
    # if player_rect.collidepoint(cursor_position):
    #     print("Collision")
    
    # Check keypres
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('Jump')


    # Draw/Update elements in the game
    pygame.display.update()
    clock.tick(60) # Limiting the while loop to not run more than 60 ticks per second.