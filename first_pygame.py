# pylint: skip-file
import pygame


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(
        f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surf = test_font.render('my pygame', False, (64, 64, 64))
# score_rect = score_surf.get_rect(midtop=(400, 25))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(800, 300))

player_surf = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

# intro screen
player_stand = pygame.image.load(
    'graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

title_surf = test_font.render('Name of the game', False, (111, 196, 169))
title_rect = title_surf.get_rect(center=(400, 80))

instruction_surf = test_font.render(
    'Press any button to play', False, (111, 196, 169))
instruction_rect = instruction_surf.get_rect(center=(400, 330))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint((event.pos)):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect.inflate(10, 10), 0, 20)
        # screen.blit(score_surf, score_rect)
        score = display_score()

        snail_rect.x -= 5
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("jump")

        # if player_rect.colliderect(snail_rect):
        #     print("collision")

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint((mouse_pos)):
        #     print("It's beeing hover")
    else:
        # game over screen
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(title_surf, title_rect)
        score_surf = test_font.render(
            f'Score: {score}', False, (111, 196, 169))
        score_rect = score_surf.get_rect(center=(400, 330))

        if score != 0:
            screen.blit(score_surf, score_rect)
        else:
            screen.blit(instruction_surf, instruction_rect)

    pygame.display.update()
    clock.tick(60)
