import pygame
from random import randint

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Racket(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
           self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 800:
           self.rect.x = 800



class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(-8, 8),randint(4, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[1] = -self.velocity[1]
        self.velocity[0] = randint(-8,8)


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

player = Racket(WHITE, 100, 10)
player.rect.x = 20
player.rect.y = 470


ball = Ball(WHITE,10,10)
ball.rect.x = 250
ball.rect.y = 10


all_sprites_list = pygame.sprite.Group()


all_sprites_list.add(player)
all_sprites_list.add(ball)


running = True
gameRunning = False


clock = pygame.time.Clock()


score = 0
scoreMax = 0
font = pygame.font.Font(None, 74)
fontSmall = pygame.font.Font(None, 40)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if gameRunning:
        if keys[pygame.K_LEFT]:
            player.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            player.moveRight(5)

        
        all_sprites_list.update()
        if ball.rect.x>=690:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>490:
            ball.velocity[1] = -ball.velocity[1]
            gameRunning = False
            scoreMax = max(score,scoreMax)
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]

        if pygame.sprite.collide_mask(ball, player):
          ball.bounce()
          score+=1

        screen.fill(BLACK)
        all_sprites_list.draw(screen)

        
        text = font.render(str(score), 1, WHITE)
        screen.blit(text, (320,10))
    else:
        screen.fill(BLACK)
        if keys[pygame.K_SPACE]:
            score = 0
            player.rect.x = 300
            player.rect.y = 480
            ball.rect.x = 250
            ball.rect.y = 10
            ball.velocity = [randint(-8, 8),randint(4, 8)]
            screen.fill(BLACK)
            gameRunning=True

        t1 = font.render(f'Current Score: {str(score)}', 1, WHITE)
        t2 = font.render(f'Max Score: {str(scoreMax)}', 1, WHITE)
        t3 = fontSmall.render(f'Press Space to start game', 1, WHITE)
        screen.blit(t1, (20,10))
        screen.blit(t2, (20,60))
        screen.blit(t3, (20,460))


    pygame.display.flip()

    clock.tick(60)

pygame.quit()