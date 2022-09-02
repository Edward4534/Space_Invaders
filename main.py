# import requerid library
from tkinter import font
import pygame
import random
import math
from pygame import mixer
# initialize pygame
pygame.init()

# window size
screen_width = 800
screen_height = 600

# Size variable
size = (screen_width, screen_height)

#Display the window
screen = pygame.display.set_mode( size )

#background image
background = pygame.image.load("fondo.jpg")

#background music
mixer.music.load ("ambience-sounds-8-15136.wav")
mixer.music.play(-1)


#title
pygame.display.set_caption("Space Invaders")

#icono 
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

#player
player_img = pygame.image.load("astronave.png")
player_x = 370
player_y = 480
player_change_x = 0


#ENEMY
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []

# number of enemy
number_enemies = 8

 # create multiples enemies
for item in range( number_enemies):
    enemy_img.append(pygame.image.load("enemigo.png"))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append (4)
    enemy_y_change.append (35)

#bullet
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = "ready"

#score variable
score = 0

# front variable
score_font = pygame.font.Font("stocky.ttf", 32)

# text position in the screen
text_x = 10
text_y = 10

#game over font
go_font = pygame.font.Font("stocky.ttf", 64)
go_x = 200
go_y = 250

#game over function
def game_over (x,y):
    go_text = go_font.render("Game Over", True, (255,255,255))
    screen.blit(go_text, (x, y))

#score function
def show_text (x, y):
    score_text = score_font.render("SCORE: " + str(score), True, (255,255,255))
    screen.blit(score_text, (x, y))

#player function
def player(x, y):
    screen.blit(player_img, (x, y))


# ENEMY FUNCTION
def enemy (x ,  y, item):
    screen.blit(enemy_img[item], (x,y))


#bullet function
def fire(x, y):
    global bullet_state
    bullet_state  = "fire"
    screen.blit (bullet_img, (x + 16 , y + 10))


#collision function
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)

    if distance < 27:
        return True
    else:
        return False




# game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystoke is pressioned,
    # check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -0.1


            
            if event.key == pygame.K_RIGHT:
                player_change_x = 0.1

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    #bullet sounds
                    bullet_sounds = mixer.Sound("blaster-2-81267.wav")
                    bullet_sounds.play()
                    bullet_x = player_x
                    fire(bullet_x, bullet_y)

       
       # REVIEW IF KEYSTROKE WAS REALESED

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change_x = 0
        
    
    rgb = (0, 0, 0)
    screen.fill(rgb)

    #show background image
    screen.blit(background, (0, 0))


#INCREASE OR DEACREASE THE VARIABLE PLAYER_X

    player_x += player_change_x


    #BOUNDARIES

    if player_x <= 0:
        player_x = 0

    elif player_x >= 736:
        player_x = 736
    
    #enemy movements
    for item in range (number_enemies):

        #game over zone
        if enemy_y[ item] > 440:
            for j in range (number_enemies):
                enemy_y [ item] = 2000


            # call game over function
            game_over (go_x , go_y) 

            # break the loop
            break   


        enemy_x[item] += enemy_x_change[item]
        

        if enemy_x[item] <=  0:
            enemy_x_change[item] = 0.5
            enemy_y[item] += enemy_y_change[item]


        elif enemy_x[item] >= 736:
            enemy_x_change[item] = -0.5
            enemy_y[item] += enemy_y_change[item]

        enemy(enemy_x[item],enemy_y[item], item)


        # call the collision function
        collision = is_collision( enemy_x[item], enemy_y[item], bullet_x, bullet_y)

        if collision:

            #explosion sound
            explosion_sound = mixer.Sound("pop2-84862.wav")
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            print (score)
            enemy_x[item] = random.randint (0, 736)
            enemy_y[item] = random.randint (50, 150)


    #bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"


    if bullet_state == "fire":
        fire(bullet_x, bullet_y)
        bullet_y -= bullet_y_change



    



    player(player_x, player_y)

    # call the show_text function
    show_text(text_x, text_y)
   
    pygame.display.update()


           




