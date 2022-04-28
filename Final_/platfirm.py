import pygame, sys, os
from pygame.locals import *
os.chdir("C:\\Final_")
pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platfirm")

#define game variables
tile_size = 50

# images
sun = pygame.image.load("sun.png")
sky = pygame.image.load("sky.png")

#code to draw the grid

# def draw_grid():
#     for line in range(0,20):
#         pygame.draw.line(screen, (255,255,255), (0,line*tile_size), (screen_width,line*tile_size))
#         pygame.draw.line(screen, (255,255,255), (line*tile_size,0), (line*tile_size,screen_height))

class Player():
    def __init__(self,x,y):
        img = pygame.image.load("guy1.png")
        self.image = pygame.transform.scale(img, (40, 80)) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):
        dx = 0
        dy = 0

        #get key presses
        key = pygame.key.get_pressed() 
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5

        #add gravity
        self.vel_y += 1
        if self.vel_y> 10:
            self.vel_y = 10
        dy += self.vel_y
        
        # check for collision
             
         #update player coords
        self.rect.x += dx
        self.rect.y += dy   

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.vel_y = 0
            self.jumped = False 

        #draw player on screen
        screen.blit(self.image, self.rect)



class World():
    def __init__(self, data):
       self.tile_list = []
       
       #load images
       dirt = pygame.image.load("dirt.png")
       grass = pygame.image.load("grass.png")
       row_count = 0
       for row in data:
           col_count = 0
           for tile in row:
               if tile ==1:
                    img = pygame.transform.scale(dirt, (tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
               if tile ==2:
                    img = pygame.transform.scale(grass, (tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
               col_count += 1
           row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


world_data = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,2,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,2,0,2,0,2,2,2,2,2,2,1],
[1,0,0,0,0,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

player = Player(100,screen_height-130)
world = World(world_data)

run = True
while run:

    screen.blit(sky, (0,0))
    screen.blit(sun, (100,100))

    world.draw()
    
    player.update()

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    pygame.display.update() 

pygame.quit()