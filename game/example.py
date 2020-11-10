# In this example.py you will learn how to make a very simple game using the pygame library.
# One of the best ways of learning to program is by writing games.
# Pygame is a collection of modules in one package.
# You will need to install pygame.
# To do so:
# 1) open the command line interface on your computer,
# 2) cd to the directory that this task is located in,
# 3) follow the instructions here: https://www.pygame.org/wiki/GettingStarted
# 4) if you need help using pip, see here: https://projects.raspberrypi.org/en/projects/using-pip-on-windows

import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 2000
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("player.jpg")
enemy = pygame.image.load("enemy.png")
monster = pygame.image.load("monster.jpg")
image = pygame.image.load("image.png")
prize = pygame.image.load("prize.jpg")
# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

player_height = player.get_height()
player_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
monster_height = monster.get_height()
monster_width = monster.get_width()
image_height = image.get_height()
image_width = image.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)#enemy1

monsterXPosition = screen_width + 500
monsterYPosition = random.randint(0,screen_height - monster_height)#enemy2

imageXPosition = screen_width + 1000
imageYPosition = random.randint(0,screen_height - image_height)#enemy3

prizeXPosition = screen_width + 1550
prizeYPosition = random.randint(0,screen_height - image_height)

# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(monster, (monsterXPosition, monsterYPosition))
    screen.blit(image,(imageXPosition, imageYPosition))
    screen.blit(prize,(prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -=1

    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition +=1
            
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = int(enemyXPosition)

    monsterBox = pygame.Rect(monster.get_rect())
    monsterBox.top = monsterYPosition
    monsterBox.left = int(monsterXPosition)

    imageBox = pygame.Rect(image.get_rect())
    imageBox.top = imageYPosition
    imageBox.left = int(imageXPosition)

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = int(imageXPosition) 
    
    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox):# Display losing status to the user
        print("You lose!")
        pygame.quit()# Quite game and exit window:
        exit(0)

    elif playerBox.colliderect(monsterBox):# Display losing status to the user
        print("You lose!")
        pygame.quit()# Quite game and exit window:
        exit(0)
        
     
    elif playerBox.colliderect(imageBox):# Display losing status to the user
        print("You lose!")
        pygame.quit()# Quite game and exit window:
        exit(0)

    if playerBox.colliderect(prizeBox):# Display win Status to the user
        print("You win !")
        pygame.quit()
        exit(0)
        
    
# If the enemy is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width:
        enemyXPosition = screen_height
        enemyYPosition = random.randint(0, screen_height - enemy_height)

    if monsterXPosition < 0 - monster_width:
        monsterXPosition = screen_height
        monsterYPOstion = random.randint(0, screen_height - monster_height)

    if imageXPosition < 0 - screen_width:
        imageXPosition = screen_height
        imageYPosition = random.randint(0,screen_height - image_height)

    if prizeXPosition < - prize_width:
        prizeXPosition = screen_height
        prizeYPosition = random.randint(0, screen_height - image_height)
    
    # Make enemy approach the player.
    
    enemyXPosition -= 1
    monsterXPosition -= 1
    imageXPosition -= 1
    prizeXPosition -= 1
    
    # ================The game loop logic ends here. =============
  
