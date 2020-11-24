import pygame
import random

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 1
        
        if self.rect.y > 401:
            self.reset_pos()
    def reset_pos(self):
        self.rect.x = random.randrange(700)
        self.rect.y = -20
    

hit_group = pygame.sprite.Group()
all_group = pygame.sprite.Group()

for i in range(10):
    block = Block(BLACK,20 ,15)
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    all_group.add(block)
    hit_group.add(block)

player = Block(RED,20 ,15)
all_group.add(player)

score = 0

font = pygame.font.Font(None, 50)

done = False

clock = pygame.time.Clock()
start_time =pygame.time.get_ticks()
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        
    screen.fill(WHITE)
    seconds = int((pygame.time.get_ticks()-start_time)/1000)
    pos = pygame.mouse.get_pos()
    all_group.update()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    score_group = pygame.sprite.spritecollide(player, hit_group, True)
    
    scoreShow = font.render(str(seconds), 20, BLACK)
    screen.blit(scoreShow, (-50, -50))
    random_x = random.get_randbits(player_x)
    random_y = random.get_randbits(player_y)
    if space.key_down():
        player = (WHITE,random_x,random_y）＃按鍵按下改變顏色與位置
    for block in score_group:
        score+=1
        block.reset_pos()
    all_group.draw(screen)        
      
    message = str(score)+' point'
    text = font.render(message, 10, BLACK)
    screen.blit(text, (10,10))
    if seconds >10:
        done = True
        GameOver = font.render("Time's up, game over!", 70, BLACK)
        screen.blit(GameOver, (350,200))
    
    all_group.draw(screen)
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()
