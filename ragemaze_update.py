import pygame #importing the pygame library
import sys #importing sys module so we can allow the user to exit the program using the system
pygame.font.init()#initializing the font for the completion text
pygame.init()#initializes pygames stuff like audio
pygame.mixer.init()

# setup for the finishing txt
textfont = pygame.font.SysFont("monospace", 50)
goal_text = textfont.render("Took you long enough!", 1, (255, 255, 255))
#the size of the tile in the grid, the screen is 600 x600 so to make it even for a 20x20 grid ya want to make it 30
tile_size = 30
Resets = -1

# Sounds for the rage maze
respawn_sound = pygame.mixer.Sound("restart.wav")#loading respawn sound in the offical pygame tutorial the guy was like "i dont know why they decided to make Sound caplitlaized, littlerally nothing else is."
pygame.mixer.music.load("loud_noises.wav") # loading our games "music" lol
pygame.mixer.music.play(-1) #the mixer basically plays all the audio when you set it to -1 the music will play in a infinite loop.

#Loading all of the images into our game
background = pygame.image.load('Rage Game Background.png')
ketchup = pygame.image.load('Ketchup 50x50.png')
weeny = pygame.image.load('Glizzy 40x40.png')
behind=pygame.image.load('Walls.png')
#adjusting the size of the images first arguement is what you want to resize, the second is the width and height ya want
newweeny = pygame.transform.scale(weeny, (30, 30))
newketchy = pygame.transform.scale(ketchup, (70, 70))
newbacky = pygame.transform.scale(background, (370, 370))
newbehindy = pygame.transform.scale(behind, (600, 600))

class goal:
    def __init__(self, x, y, color):#the init lets the object"goal"have all the paraneters inputed at the start like its x and y and stuff
        self.x = x #x coordinate of goal
        self.y = y #y coordinate of goal
        self.color = color #we kept this just in case 
        self.image = pygame.Surface((30, 30)) # A Surface is just a 2d image that holds data , the coordinates is its width and height.
        self.rect = self.image.get_rect(topleft=(self.x, self.y)) # This gets our rect which is like a little invisible hitbox, it is what lets us move our characture and lets us do collisions. the rects main purpose is to give a image a defined position and size
    # this is for updating the goal and drawing it on the screen
    def update(self):
        self.image.fill(self.color) # if we were to use the original surface we would use this code to fill in the surface with the color the user selected
        self.rect.x = self.x * tile_size #this calculates the  x position of the goal based on the grid position ie. position (1,1) 1*30= the actual position on the display
        self.rect.y = self.y * tile_size #this calculates the  x position of the goal based on the grid position
        screen.blit(newketchy, (self.rect.x - 18, self.rect.y - 18)) #to blit is to draw on the screen basically. we  used the rect that was originally made from the surface and instead blitted the picture of the ketchup bottle.due to the wierd shape of the image we had to do calculations to put the image more centered on the map

class weenie:
    def __init__(self, x, y, color):
        self.original_x = x  # Store original position
        self.original_y = y
        self.x = x 
        self.y = y 
        self.speed = 1 #this controlls how fast the character will move
        self.color = color
        self.image = pygame.Surface((20, 20)) 
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.movement_disabled = False  # Flag to disable movement once the user completes the game

    def update(self):
        if not self.movement_disabled:
            self.rect.x = self.x * tile_size
            self.rect.y = self.y * tile_size
            screen.blit(newweeny, (self.rect.x - 3.5, self.rect.y - 6))
    
    def reset_position(self, x, y):
        self.x = x  # Reset to original position
        self.y = y
bck= pygame.surface.Surface((270,60))
bck.fill((191, 64, 191))
Weenie = weenie(12, 18, (255, 255, 255)) #making our charecter 
ketchy = goal(12, 18, (255, 29, 10))#making our goal if we used the og surface those three numbers is our rgb 

# Clock
fps = 30 #how many frames our game should draw per second
fpsClock = pygame.time.Clock()# controls the timing of the game and prevents the game from refreshing too fast

# making our display
screen = pygame.display.set_mode((600, 600), pygame.DOUBLEBUF)#draws behinds the scenes in the back buffer, then shows it in the front buffer (the user scree)
pygame.display.set_caption("Rage Maze")

# Drawing a grid
def draw_grid(tile_size):#each for loop is drawing a line for x and y spaced by the tile size and moving in incraments of the tile size which is 30
    for x in range(tile_size, 600, tile_size):
        pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, 600))
    for y in range(tile_size, 600, tile_size):
        pygame.draw.line(screen, (255, 255, 255), (0, y), (600, y))



maze_stuff = []#this is the list that we will be appending onto from the text file called mazetiles
with open('mazetiles', 'r') as mazetiles:
    for line in mazetiles: #this is a loop that says for each line in maze tiles that is read, append the text as string onto the list maze_stuff
        maze_stuff.append(line)
     
wall_group = pygame.sprite.Group() #comming up we are going to create walls for the maze, putting the wall into a sprite group makes them easier to manage and draw on screen
#making a class for the wall to be built, if you notice we are using sprite, the reason why is that it makes the walls eaiser to group together
class walls(pygame.sprite.Sprite):#the Sprite class is a built in class within the sprite mod that is for objects that are used in the game , the reason why we are using it here is that its very handy for grouping, but its good for many other things
    def __init__(self, x, y, color):
        super().__init__()#this is used to let the class we make work intandum with the parent class which is Sprite
        self.x = x
        self.y = y
        self.color = (153, 51, 255)
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x * tile_size
        self.rect.y = self.y * tile_size
        self.image.blit(newbacky, (0, 0))
#this line of code right here takes the index and the string for each row then column then makes it nice and sorted, then it looks if any thing within the column is a "1" if so by its index(row, col) create a wall sprite, then add it to the overall group
for row, tiles in enumerate(maze_stuff):
    for col, tile in enumerate(tiles):
        if tile == "1":
            wall = walls(col, row, (90, 90, 90))
            wall_group.add(wall)
 


running = True # The while loop to rune the game is True to run False to stop
goal_text_displayed = False
goal_time = 0  # stores the time when the goal text is shown
# game loop
while running: #this is saying that while True, which is an infinant loop 
    screen.fill((0, 0, 0)) #this clears your screen. you must always clear your screen. also fill your screen before you draw anything else on the screen or else your screen will just be black or a character will not be drawn
    screen.blit(newbehindy, (0, 0))#this draws the backround on the screen starting at the back corner
    pygame.mouse.set_visible(False)#this just hides the mouse 
    pygame.mouse.set_pos(Weenie.x * tile_size + tile_size // 2, Weenie.y * tile_size + tile_size // 2) #as soon as you hit the screen you mouse teleport directly to the weenie
    draw_grid(tile_size)
    fpsClock.tick(fps)# this starts refreshing the game at 30 frames per second
     #this is so that the user can hit the x button on the pygame window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    #puts our wall group on the screen
    wall_group.draw(screen)

    # The movement
    if not Weenie.movement_disabled:
        rel_x, rel_y = pygame.mouse.get_rel()#gets the amount of movement weenie gets
        sensitivity = .09 #variable used to desenitize our movement
        
        # Update character position based on trackpad movement
        Weenie.x += rel_x * Weenie.speed * sensitivity# basically movement measured(by the trackpad) * 1(speed)*.1(desensitizantion)
        Weenie.y += rel_y * Weenie.speed * sensitivity
        #keeps weenie on the screen, yes we actually need it lol
        Weenie.x = max(0, min(Weenie.x, (600 // tile_size) - 1))
        Weenie.y = max(0, min(Weenie.y, (600 // tile_size) - 1))

    # Collision detection makes it to where if weenies rect overlaps any of the walls rects it will reset weenie to 1,1
    for wall in wall_group:
        if Weenie.rect.colliderect(wall.rect):
            Weenie.reset_position(1, 1)
            Resets += 1
            
            # Reset goal to prevent cheatsies
            ketchy.x, ketchy.y = 12, 18 
            ketchy.rect.x = ketchy.x * tile_size
            ketchy.rect.y = ketchy.y * tile_size
        
            break  # Reset position on collision
        #plays respawn sound only at coordinates 1-2,1
        if 1 <= Weenie.x <= 2 and Weenie.y == 1:
            pygame.mixer.Sound.play(respawn_sound)
            pygame.mixer.music.play(-1)
    
      #moves they goal to the end 
    if   17 <= Weenie.y <= 18  :
        ketchy.x, ketchy.y = 13, 2 
        ketchy.rect.x = ketchy.x * tile_size
        ketchy.rect.y = ketchy.y * tile_size
        


    if   1<= Weenie.y <=3 and 10<= Weenie.x <= 12 and ketchy.x==13 and ketchy.y ==  2  :
        ketchy.x, ketchy.y = 1, 12 
        ketchy.rect.x = ketchy.x * tile_size
        ketchy.rect.y = ketchy.y * tile_size
    
    if   11<= Weenie.y <=12 and  2<= Weenie.x <= 3 and ketchy.x==1 and ketchy.y ==  12  :
        ketchy.x, ketchy.y = 4, 1 
        ketchy.rect.x = ketchy.x * tile_size
        ketchy.rect.y = ketchy.y * tile_size



    if Weenie.rect.colliderect(ketchy.rect):
        screen.blit(goal_text, (1, 200))  # Display the goal text

        # Disable movement once Weenie collides with the goal
        Weenie.movement_disabled = True

        # Check if the goal text has been displayed for 30 seconds
        if not goal_text_displayed:
            goal_text_displayed = True
            goal_time = pygame.time.get_ticks()  # Record the time when goal text is shown

    # If 30 seconds have passed, stop the game
    if goal_text_displayed and pygame.time.get_ticks() - goal_time >= 1000:  # 1 seconds = 1000 ms
        running = False
    Weenie.update() #draws weenie onto the screen
    ketchy.update()
    screen.blit(bck,(330,-3))
    Resets_txt= textfont.render(f"Resets:{Resets}", True, (255,255,255))
    screen.blit(Resets_txt, (330,1))
    pygame.display.flip()#copies ecverything on the back buffer and redraws it on the front buffer(what we see)
print("Wow its either you just gave up or it took you 30 years to finish this simple maze....be better")
print("You failed about",Resets,"times...BE BETTER!")
pygame.quit()
sys.exit()




