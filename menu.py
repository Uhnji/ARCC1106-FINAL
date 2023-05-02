import pygame

class Button:
    def __init__(self, x, y, image, scale):  
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # Get Mouse Position
        pos = pygame.mouse.get_pos()

        # Check Mouserover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        # Draw Button On Screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

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
        if menu_state =='main':
            if game_start:
                if start_button.draw(screen):
                    game_paused = False
                    game_start = False
            elif not game_start:
                if resume_button.draw(screen):
                    game_paused = False
                    
            if options_button.draw(screen):
                menu_state = 'options'
            if quit_button.draw(screen):
                running = False
        
        if menu_state == 'options':
            if video_settings_button.draw(screen):
                print('Video')
            if audio_settings_button.draw(screen):
                menu_state = 'audio'
                print(menu_state)
            if key_bindings_button.draw(screen):
                print('Keys')
            if back_button.draw(screen):
                menu_state = 'main'

        if menu_state == 'audio':
            if back1_button.draw(screen):
                menu_state = 'options'
    else:
        draw_text('Press ESCAPE to pause', font1, TEXT_COLOR, 160, 250)
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
menu_state = "main" # variable for the menu state

# Define Fonts
font1 = pygame.font.SysFont('arialblack', 40) # font

# Define Colors
TEXT_COLOR = (255,255,255) # text color
FILL_COlOR = (52,78,91)    # background color

# Button Images
audio_settings_img = pygame.image.load('Sprites\MenuAssets\AudioSettingsButtonImage.png').convert_alpha()
back_img = pygame.image.load('Sprites\MenuAssets\BackButtonImage.png').convert_alpha()
back1_img = pygame.image.load('Sprites\MenuAssets\BackButtonImage.png').convert_alpha()
key_bindings_img = pygame.image.load('Sprites\MenuAssets\KeyBindingsButtonImage.png').convert_alpha()
options_img = pygame.image.load('Sprites\MenuAssets\OptionsButtonImage.png').convert_alpha()
quit_img = pygame.image.load('Sprites\MenuAssets\QuitButtonImage.png').convert_alpha()
resume_img = pygame.image.load('Sprites\MenuAssets\ResumeButtonImage.png').convert_alpha()
start_img = pygame.image.load('Sprites\MenuAssets\LockStartButtonImage.png').convert_alpha()
video_settings_img = pygame.image.load('Sprites\MenuAssets\VideoSettingsButtonImage.png').convert_alpha()

# Button Instances 
audio_settings_button = Button(225, 200, audio_settings_img, 1)
back_button = Button(332, 450, back_img, 1)
back1_button = Button(332, 450, back1_img, 1)
key_bindings_button = Button(246, 325, key_bindings_img, 1)
options_button = Button(297, 250, options_img, 1)
quit_button = Button(336, 375, quit_img, 1)
resume_button = Button(300, 125, resume_img, 1)
start_button = Button(300, 125, start_img, 0.4)
video_settings_button = Button(226, 75, video_settings_img, 1)


# Game Loop     
while running:
    screen.fill(FILL_COlOR)  # fills the screen
    event_handler()          # runs event handler function
    on_screen_buttons()      # puts and checks buttons on screen
    pygame.display.update()  # Updates display
pygame.quit()                # quits pygame when loop done
