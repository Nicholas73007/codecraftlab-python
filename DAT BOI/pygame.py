
import pygame
from pygame.locals import  *
import random


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self,).__init__()
##        self.surf = pygame.Surface((75, 75))
##        self.surf.fill((255, 255, 255))
##        self.rect = self.surf.get_rect()
        self.image = pygame.image.load('bottle.png').convert()
        self.image.set_colorkey((255, 255, 255),RLEACCEL)
        self.rect = self.image.get_rect()



    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >600:
            self.rect.bottom = 600


class Opponent(pygame.sprite.Sprite):
    def __init__(self):
        super(Opponent, self).__init__()
        self.image = pygame.image.load('Screaming kid.jpg').convert()
        self.image.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.image.get_rect(
            center = (random.randint(820,900), random.randint(0,600))
        )
        self.speed = random.randint(0,1)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


           
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        # super(Enemy, self).__init__()
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 255, 255))
        # self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))
        # self.speed = random.randint(0, 1)
        
        super(Bird, self).__init__()
        self.image = pygame.image.load('condorFlapPrev.gif').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(850, 900), random.randint(0, 600))
        )
        self.speed = random.randint(0,1)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

#create weather class - Cloud
            
    def update(self):
        self.rect.move_ip(0, 1)
        if self.rect.bottom > 900:
            self.kill()

#create level function
def set_level(level):
    caption = 'Airplane - ' + ' Level ' + str(level)
    pygame.display.set_caption(caption)

#initialize game    
pygame.init()

#create initial screen
screen = pygame.display.set_mode((display_width,display_height))

#set initial level
level = 0
set_level(level)

#create and initialize game events and event timers
ADDBIRD = pygame.USEREVENT + 1
bird_time = 250
pygame.time.set_timer(ADDBIRD,bird_time)

ADDCLOUD = ''
ADDGREYCLOUD = ''
ADDRAIN = ''
ADDLIGHTNING = ''
GAMEOVER = ''

#define weather conditions
rainy_conditions = ["Drizzle", "Rain", "Rain Mist", "Rain Showers", "Thunderstorm", "Thunderstorms and Rain"]
cloudy_conditions = ["Partly Cloudy", "Scattered Clouds", "Mostly Cloudy", "Overcast"]

#create screen background
background = pygame.Surface(screen.get_size())
background.fill((135, 206, 250))
#create weather class - Rain            
class Rain(pygame.sprite.Sprite):
    def __init__(self):
        super(Rain, self).__init__()
        self.image = pygame.image.load('raindrop.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(0, 800), random.randint(-20, 0))
        )        

#get weather condition from WeatherSTEM API
wc = getWeatherCondition(station_data)

#omit weather modifier for now
if 'Light' in wc or 'Heavy' in wc:
    wc = wc[6:]

#if weather condition is cloudy, add cloud to game    
if wc in cloudy_conditions:
    ADDCLOUD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCLOUD, 1000)
    
    #darken background if Mostly Cloudy or Overcast
    if wc == cloudy_conditions[2] or wc == cloudy_conditions[3]:
        pygame.time.set_timer(ADDCLOUD, 500)
        background.fill((211, 211, 211))

#if weather condition has rain, add rain and grey clouds to game           
elif wc in rainy_conditions:    
    ADDRAIN = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDRAIN, 100)
    background.fill((211, 211, 211))
    
    ADDGREYCLOUD = pygame.USEREVENT + 5
    pygame.time.set_timer(ADDGREYCLOUD, 1000)
    
    #if weather condition has thunderstorms, add lightning to game
    if wc == rainy_conditions[4] or wc == rainy_conditions[5]:
        ADDLIGHTNING = pygame.USEREVENT + 6
        pygame.time.set_timer(ADDLIGHTNING, 1250)

#get current background        
curr_bg = tuple(background.get_at((0,0)))

#create an instance of a Player
player = Player()

#add game objects
birds = pygame.sprite.Group()
if wc in cloudy_conditions:
    clouds = pygame.sprite.Group()
elif wc in rainy_conditions:
    raindrops = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#initialize variable to True to run game
running = True

#create game clock, create variable for frames per second (FPS), and get starting time
clock = pygame.time.Clock()
fps = 1000
start_time = time.time()

#main game loop
while running:
    #set game FPS
    clock.tick(fps)
    
    #polling for game events
    for event in pygame.event.get():
        #check for pressing of ESC key and quit if pressed
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        #check if game was quitted
        elif event.type == QUIT:
            running = False
        
        #if Bird event occurs, add bird
        elif(event.type == ADDBIRD):
            new_bird = Bird()
            birds.add(new_bird)
            all_sprites.add(new_bird)
        
        #if cloud event occurs, add cloud
        elif event.type == ADDCLOUD:
            new_cloud = Cloud('white')
            all_sprites.add(new_cloud)
            clouds.add(new_cloud)
        
        #if grey cloud event occurs, add grey cloud
        elif event.type == ADDGREYCLOUD:
            new_cloud = Cloud('grey')
            all_sprites.add(new_cloud)
            clouds.add(new_cloud)
        
        #if rain event occurs, add rain
        elif event.type == ADDRAIN:
            new_rain = Rain()
            all_sprites.add(new_rain)
            raindrops.add(new_rain)
        
        #if lightning event occurs, flash screen
        elif event.type == ADDLIGHTNING:
            flash = random.randint(0,1)
            if flash:
                background.fill((255, 255, 255))
            else:
                background.fill(curr_bg)
        
        #if game over event occurs, pause screen and wait for player to quit        
        elif event.type == GAMEOVER:
            pause = True
            while pause:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pause = False
                            running = False                            
                    elif event.type == QUIT:
                        pause = False
                        running = False 
    
    #get elapsed time
    elapsed_time = time.time() - start_time 
    
    #based on elapsed time, speed up game by adding more birds
    if elapsed_time >= 10.0:
        bird_time -=20
        if bird_time > 0:
            level+=1
            set_level(level)
            pygame.time.set_timer(ADDBIRD,bird_time)
        else:
            pygame.time.set_timer(ADDBIRD,1)
        start_time = time.time()
 
    #draw background to screen
    screen.blit(background, (0,0))
    
    #get pressed keys
    pressed_keys = pygame.key.get_pressed()    
    
    #update player's position on screen
    player.update(pressed_keys)
    
    #update bird's position on screen
    birds.update()
    
    #update cloud positions
    if wc in cloudy_conditions:
        clouds.update()
        
    #update rain position
    elif wc in rainy_conditions:
        raindrops.update()
        clouds.update()
    
    #draw game objects to screen
    for entity in all_sprites:
        screen.blit(entity.image,entity.rect)
    
    
    #if player crashes into bird, game over
    if pygame.sprite.spritecollideany(player, birds):
        player.kill()
        font = pygame.font.Font(None, 36)
        text = font.render("GAME OVER", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)
        GAMEOVER = pygame.USEREVENT + 4
        pygame.time.set_timer(GAMEOVER, 1000)
    



pygame.init()
#create screen
screen = pygame.display.set_mode((800, 600))
player = Player()



background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

#create main loop

running = True
players = pygame.sprite.Group()
opponents = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
ADDOPPONENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADDOPPONENT, 250)
while running:
    for event in pygame.event.get():
        #if key is pressed
        if event.type == KEYDOWN:
            #and that key happens to be the escape key
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            

        elif (event.type == ADDOPPONENT):
            new_opponent = Opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)
                       
    screen.blit(background, (0,0))

    pressed_keys =pygame.key.get_pressed()

    player.update(pressed_keys)
    opponents.update()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, opponents):
        player.kill()

    pygame.display.flip()

pygame.init()

pygame.quit()

