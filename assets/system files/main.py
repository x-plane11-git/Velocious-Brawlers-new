import pygame
from fighter import Fighter
pygame.init()

#game window
width,height = 1280,720
screen = pygame.display.set_mode((width,height),pygame.FULLSCREEN)
pygame.display.set_caption('Velocious Brawlers')
#FPS
clock = pygame.time.Clock()
FPS = 60
#colours
YELLOW = (255,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (124,252,0)

#define fighter variables
wind_fighter_width = 288
wind_fighter_height = 128
wind_fighter_data = [wind_fighter_width,wind_fighter_height]
fire_fighter_width = 288
fire_fighter_height = 128
fire_fighter_data = [fire_fighter_width,fire_fighter_height]
#Main loop
run = True

#load background images
mapone_1 = pygame.transform.scale((pygame.image.load('../graphics/map_1/1.png').convert_alpha()), (width,height))
mapone_2 = pygame.transform.scale((pygame.image.load('../graphics/map_1/2.png').convert_alpha()), (width,height))
mapone_3 = pygame.transform.scale((pygame.image.load('../graphics/map_1/3.png').convert_alpha()), (width,height))
mapone_4 = pygame.transform.scale((pygame.image.load('../graphics/map_1/4.png').convert_alpha()), (width,height))
mapone_5 = pygame.transform.scale((pygame.image.load('../graphics/map_1/5.png').convert_alpha()), (width,height))
mapone_6 = pygame.transform.scale((pygame.image.load('../graphics/map_1/6.png').convert_alpha()), (width,height))
mapone_7 = pygame.transform.scale((pygame.image.load('../graphics/map_1/7.png').convert_alpha()), (width,height))
mapone_8 = pygame.transform.scale((pygame.image.load('../graphics/map_1/8.png').convert_alpha()), (width,height))
mapone_9 = pygame.transform.scale((pygame.image.load('../graphics/map_1/9.png').convert_alpha()), (width,height))
mapone_10 = pygame.transform.scale((pygame.image.load('../graphics/map_1/10.png').convert_alpha()), (width,height))
mapone_11 = pygame.transform.scale((pygame.image.load('../graphics/map_1/11.png').convert_alpha()), (width,height))
mapone_12 = pygame.transform.scale((pygame.image.load('../graphics/map_1/12.png').convert_alpha()), (width,height))
map_1 = [mapone_1,mapone_2,mapone_3,mapone_4,mapone_5,mapone_6,mapone_7,mapone_8,mapone_9,
                mapone_10, mapone_11, mapone_12]
#load sprite sheets
wind_fighter = pygame.image.load('../graphics/player_1/windsprite.png').convert_alpha()
fire_fighter = pygame.image.load('../graphics/player_2/firesprite.png').convert_alpha()
#steps in animation
wind_fighter_steps = [8,8,3,3,7,6,8,18,26,31,8,6,19]
fire_fighter_steps = [8,8,3,3,20,8,8,19,28,18,10,6,13]
#fn
def draw_bg():
    for img in map_1:
        screen.blit(img, (0,0))
#health bars
def drawhb(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x-2,y-2,404,34),0,20)
    pygame.draw.rect(screen, RED, (x,y,400,30),0,20)
    pygame.draw.rect(screen, GREEN, (x,y, 400 * ratio, 30),0,20)
#create 2 fighter instances
fighter_1 = Fighter(200, 310, wind_fighter_data, wind_fighter, wind_fighter_steps)
fighter_2 = Fighter(700, 500, fire_fighter_data, fire_fighter,fire_fighter_steps)
while run:
    clock.tick(FPS)
    draw_bg()
    #health bars
    drawhb(fighter_1.health,20,20)
    drawhb(fighter_2.health,860,20)
    #move
    fighter_1.move(width,height,screen,fighter_2)
    #fighter_2.move()
    #draw fighter
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #update
    pygame.display.update()
pygame.quit()