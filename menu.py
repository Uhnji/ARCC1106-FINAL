import pygame
from button import Button

def draw_text(text, font, text_color, x, y):  
    """Draws Text To Screen"""
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def event_handler():
    """Checks if the x on the screen is hit or if the space bar is hit to pause the game"""
    global running, game_paused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = True

def on_screen_buttons():
    """Function that put the buttons on the screen and then checks to see if a button was click.
       Also, when starting the game it shows the start button but after the fist time (for pauses)
       it shows a resume button. Also, when the start or resume button is hit it brings you to another 
       screen that says what is in the bottom else statement."""
    global running, game_paused, menu_state, game_start
    if game_paused:
        if game_start:
            if start_button.draw(screen):
                game_paused = False
                game_start = False
        elif not game_start:
            if resume_button.draw(screen):
                game_paused = False
        if quit_button.draw(screen):
            running = False
        
    else:
       while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                player.left = True
            else:
                player.left = False

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
               player.right = True
            else:
                player.right = False

            if keys[pygame.K_w] or keys[pygame.K_UP]:
                player.up = True
            else:
                player.up = False

            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                player.down = True
            else:
                player.down = False

            if keys[pygame.K_SPACE] or keys[pygame.K_RCTRL]:
                player.dash_active = True
            else:
                player.dash_active = False

        tiles, floor_tiles = dungeon.read(win)

        enemy.update(player.x, player.y)
        player.update()
        player.check_collisions(tiles)
        enemy.check_collisions(tiles)



        timer_frame = None 

        if 450 < player.cooldown <= 600: # Mainline check to append the Player Cooldown icon to the screen following the Dash (Accessibility Function)
            timer_frame = (player.timer_sprites[1],player.x,player.y-45)

        elif 300 < player.cooldown <= 450:
            timer_frame = (player.timer_sprites[2],player.x,player.y-45)

        elif 150 < player.cooldown <= 300:
            timer_frame = (player.timer_sprites[3],player.x,player.y-45)

        elif 50 < player.cooldown <= 150:
            timer_frame = (player.timer_sprites[4],player.x,player.y-45)

        elif 0 < player.cooldown <= 50: 
            timer_frame = (player.timer_sprites[5],player.x,player.y-45)


        if timer_frame != None:
            render_layer2.append(timer_frame)



        #Camera movement section start.
        camera_x = (player.x - winWidth/2 + 16)/20
        camera_y = (player.y - winHeight/2 + 16)/20

        dungeon.x0 -= camera_x
        dungeon.y0 -= camera_y

        player.x -= camera_x
        player.y -= camera_y

        enemy.x -= camera_x
        enemy.y -= camera_y
        #Camera movement section end.

        #Add to render layer 1.
        render_layer1.append(player.draw(win))
            

        render_layer0 += floor_tiles
        render_layer1 += tiles
        tiles.clear()
        floor_tiles.clear()
        #End to render layer 1.

        y_sort(render_layer1)

        #Render loop.
        win.fill((12,24,36))

        #Render render layer 1.

        for i in range(len(render_layer0)): 
            win.blit(render_layer0[i][0], (render_layer0[i][1], render_layer0[i][2]))

        for i in range(len(render_layer1)): # Walls, Players, Enemies
            win.blit(render_layer1[i][0], (render_layer1[i][1], render_layer1[i][2]))

        for i in range(len(render_layer2)): # Rendered HUD icons, Projectiles, Items
            win.blit(render_layer2[i][0], (render_layer2[i][1], render_layer2[i][2]))

        enemy.render(win)

        pygame.display.flip()

        render_layer0.clear()
        render_layer1.clear()
        render_layer2.clear()

        clock.tick(120)

pygame.init()

# Create Game Window
SCREEN_HEIGHT = 1000  # Screen Height Up/Down
SCREEN_WIDTH = 800    # Screen Width Left/Right

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pygame.RESIZABLE) # Makes a window called screen with said variables
pygame.display.set_caption('MENU')  # Window caption name

# Game Variables
running = True      # Checks if game loop is running
game_start = True
game_paused = True # Checks if game is paused

# Define Fonts
font1 = pygame.font.SysFont('arialblack', 40) # font

# Define Colors
TEXT_COLOR = (255,255,255) # text color
FILL_COlOR = (52,78,91)    # background color

# Button Images
quit_img = pygame.image.load('C:\John\'s Stuff\VS Code\CSCI 1106 - 80\Game\GameImages\QuitButtonImage.png').convert_alpha()
resume_img = pygame.image.load('C:\John\'s Stuff\VS Code\CSCI 1106 - 80\Game\GameImages\ResumeButtonImage.png').convert_alpha()
start_img = pygame.image.load('C:\John\'s Stuff\VS Code\CSCI 1106 - 80\Game\GameImages\LockStartButtonImage.png').convert_alpha()

# Button Instances 
quit_button = Button(336, 300, quit_img, 1)
resume_button = Button(300, 125, resume_img, 1)
start_button = Button(300, 125, start_img, 0.4)


# Game Loop     
while running:
    screen.fill(FILL_COlOR)  # fills the screen
    event_handler()          # runs event handler function
    on_screen_buttons()      # puts and checks buttons on screen
    pygame.display.update()  # Updates display
pygame.quit()                # quits pygame when loop done
