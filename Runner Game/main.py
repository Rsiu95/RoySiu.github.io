import pygame
import sys
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('Runner Game/graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('Runner Game/graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('Runner Game/graphics/Player/jump.png').convert_alpha()
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0
        
        self.jump_sound = pygame.mixer.Sound('Runner Game/audio/jump.mp3')
        self.jump_sound.set_volume(0.3)
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity = -20
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
            
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'fly':
            fly_1 = pygame.image.load('Runner Game/graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('Runner Game/graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('Runner Game/graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('Runner Game/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
            
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
        
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()
        
    def destroy(self):
        if self.rect.x < -100:
            self.kill()

# Displays the score
def display_score():
    current_time = (pygame.time.get_ticks() - start_time) // 1000 - start_time
    score_surface = game_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = ((screen_width // 2), (screen_height // 5)))
    #pygame.draw.rect(screen, '#c0e8ec', score_rect)
    #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surface,score_rect)
    return current_time

# # Handles the obstacles (fly + snail)
# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -= 5
#             if obstacle_rect.bottom == 300:
#                 screen.blit(snail_surface, obstacle_rect)
#             else:
#                 screen.blit(fly_surface, obstacle_rect)
                
#         obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
#         return obstacle_list
#     else:
#         return []

# Handles Collision
def check_collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player_rect.colliderect(obstacle_rect):
                return False
    return True

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True
    

# Handle player animations
def player_animation():
    # Walk if player on floor, Jump animation if player > floor height
    global player_surface, player_index    
    if player_rect.bottom < 300: 
        player_surface = player_jump
    else:
        # Alternate between walk1 and walk2 image 
        player_index += 0.1 # Increment by 0.1 to allow for smoother walk
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]

# Initialise game
pygame.init()
game_active = True
start_time = 0

# Set main display variables
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


# Set game name
pygame.display.set_caption('Pixel Runner')

# Set game Font
font_type = "Runner Game/font/Pixeltype.ttf"
font_size = 50
game_font = pygame.font.Font(font_type, font_size)

game_name = game_font.render('Pixel Runner', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400, 40))

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
game_over_rect = game_over_text.get_rect(center = ((screen_width // 2), (80)))

# # Snail 
# snail_frame_1 = pygame.image.load('Runner Game/graphics/snail/snail1.png').convert_alpha()
# snail_frame_2 = pygame.image.load('Runner Game/graphics/snail/snail2.png').convert_alpha()
# snail_frames = [snail_frame_1, snail_frame_2]
# snail_frame_index = 0
# snail_surface = snail_frames[snail_frame_index]

# # Fly
# fly_frame_1 = pygame.image.load('Runner Game/graphics/Fly/Fly1.png').convert_alpha()
# fly_frame_2 = pygame.image.load('Runner Game/graphics/Fly/Fly2.png').convert_alpha()
# fly_frames = [fly_frame_1, fly_frame_2]
# fly_frame_index = 0
# fly_surface = fly_frames[fly_frame_index]

# obstacle_rect_list = []

# Player
player_walk1 = pygame.image.load('Runner Game/graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('Runner Game/graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('Runner Game/graphics/Player/jump.png').convert_alpha()

player_surface = player_walk[player_index]
player_x_pos, player_y_pos = 80,300
player_rect = player_surface.get_rect(midbottom = (player_x_pos, player_y_pos))

player_stand = pygame.image.load('Runner Game/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# Gravity
gravity = 1
jump_height = 0

# Check size of sky background by converting from surface object to numpy array object
#image_array = pygame.surfarray.array3d(player_surface)
#print(image_array.shape)

# Initialise clock
clock = pygame.time.Clock()

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 300)

BG_music = pygame.mixer.Sound('Runner Game/audio/music.wav')
BG_music.set_volume(0.06)
BG_music.play(loops = -1)

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
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: #and player_rect.bottom >= 300:
                    print("jump")
                    gravity = -20

            # Get mouse position with "event"
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
            #         gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks() // 1000
        
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly','snail', 'snail', 'snail'])))
            #     if randint(0, 2):
            #         obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))
            #     else:
            #         obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900,1100),210)))
            
            # if event.type == snail_animation_timer:
            #     if snail_frame_index == 0:
            #         snail_frame_index = 1
            #     else:
            #         snail_frame_index = 0
            #     snail_surface = snail_frames[snail_frame_index]

            # if event.type == fly_animation_timer:
            #     if fly_frame_index == 0:
            #         fly_frame_index = 1
            #     else:
            #         fly_frame_index = 0
            #     fly_surface = fly_frames[fly_frame_index]
            
        
    if game_active:
        # This will draw the image in order of top > bottom execution
        screen.blit(sky_background,(0,0)) # blit = block image transfer
        screen.blit(ground_background,(0,300))
        score = display_score()

        # Handle snail movement
        # snail_exit_pos = randint(-10000, -72)
        # #snail_speed = randint(3,6) 
        
        # if snail_rect.right <= snail_exit_pos:
        #     snail_rect.left = 800
        # else:
        #     snail_rect.x -= 4

        # screen.blit(snail_surface,snail_rect)
        
        # # Handle fly movement
        # #fly_speed = randint(4,7)
        # fly_exit_pos = randint(-10000, -84)
        # if fly_rect.right <= fly_exit_pos:
        #     fly_rect.left = 800
        #     fly_rect.top = randint(0, 176)
        # else:
        #     fly_rect.x -= 5
        
        # screen.blit(fly_surface, fly_rect)

        # Handle player movement
        
        # gravity += 1
        # player_rect.y += gravity
        
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        # elif player_rect.top <= 0:
        #     player_rect.top = 0
        
        # player_animation()
        # screen.blit(player_surface, player_rect)
        player.draw(screen)
        player.update()
        
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        # Obstacle movement
        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        #game_active = check_collision(player_rect, obstacle_rect_list)
        game_active = collision_sprite()
        
        # if player_rect.colliderect(snail_rect) or player_rect.colliderect(fly_rect):
        #     #screen.blit(game_over_text,game_over_rect)
        #     game_active = False
            
        #     Handle Score
        #    pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #    pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
        #    screen.blit(score_surface, score_rect)
    
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        #obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0
        
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