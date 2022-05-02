from turtle import title
import pygame, sys, os
from pygame.locals import *
os.chdir("C:\\Final_")
pygame.init()

clock = pygame.time.Clock()
fps = 60


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
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
             img_right = pygame.image.load(f"guy{num}.png")
             img_right = pygame.transform.scale(img_right, (40, 80))
             img_left = pygame.transform.flip(img_right, True, False)
             self.images_right.append(img_right)
             self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5

        #get key presses
        key = pygame.key.get_pressed() 
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index % len(self.images_right)]
            if self.direction == -1:
                self.image = self.images_left[self.index % len(self.images_right)]


        #handle animation
        if self.counter >= walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index % len(self.images_right)]
            if self.direction == -1:
                self.image = self.images_left[self.index % len(self.images_right)]


        #add gravity
        self.vel_y += 1
        if self.vel_y> 10:
            self.vel_y = 10
        dy += self.vel_y
        
        # check for collision
        for tile in world.tile_list:
                #check for collision in the x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                    dx = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                    #check if below the ground
                    if self.vel_y < 0:
                       dy = tile[1].bottom - self.rect.top
                       self.vel_y = 0
                    #check if above the ground
                    elif self.vel_y >= 0:
                       dy = tile[1].top - self.rect.bottom
                       self.vel_y = 0
             
               


         #update player coords
        self.rect.x += dx
        self.rect.y += dy   

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.vel_y = 0
            self.jumped = False 

        #draw player on screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 1)



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
            pygame.draw.rect(screen, (255,255,255), tile[1], 1)


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

    clock.tick(fps)

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