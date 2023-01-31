import pygame
from sys import exit

pygame.init()
WindowWidth = 800
WindowHeight = 400
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

text_surface = test_font.render("Score: ", False, (64, 64, 64)).convert()
text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (800, 300))

# player
player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

start_time = 0

# intro screen
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f"{current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 54))
    screen.blit(score_surf, score_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.MOUSEMOTION:
                if player_rectangle.collidepoint((event.pos)):
                    print("collision")
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.right = 400
                start_time = int(pygame.time.get_ticks()/1000)
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, "#c0e8ec", text_rect, 0, 6)
        display_score()

        if snail_rectangle.right < 0: snail_rectangle.left = 800
        snail_rectangle.x -= 5
        screen.blit(snail_surface, snail_rectangle)


        # player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300:
            player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)

        # collision
        if snail_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)


    pygame.display.update()
    clock.tick(60)