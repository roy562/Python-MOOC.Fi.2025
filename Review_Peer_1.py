import pygame 
import random
import sys
 
# Initialize Pygame
pygame.init()
 
# Window dimensions and FPS
WIDTH = 640
HEIGHT = 480
FPS = 60
 
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chase the Coin")
clock = pygame.time.Clock()
 
# Sprite size
SPRITE_SIZE = 50
 
# Load images 
try:
    robot_img = pygame.image.load("robot.png").convert_alpha()
    coin_img = pygame.image.load("coin.png").convert_alpha()
    enemy_img = pygame.image.load("monster.png").convert_alpha()
except Exception as e:
    print("Error loading images. Make sure 'robot.png', 'coin.png', and 'monster.png' are in the directory.")
    sys.exit()
 
# Scale images
robot_img = pygame.transform.scale(robot_img, (SPRITE_SIZE, SPRITE_SIZE))
coin_img = pygame.transform.scale(coin_img, (SPRITE_SIZE, SPRITE_SIZE))
enemy_img = pygame.transform.scale(enemy_img, (SPRITE_SIZE, SPRITE_SIZE))
 
# Font for displaying text
font = pygame.font.SysFont("Arial", 28)
 
def draw_text(text, x, y, color=BLACK):
    """Draw text on screen."""
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))
 
def generate_position():
    """Generate a random position within the window."""
    x = random.randint(0, WIDTH - SPRITE_SIZE)
    y = random.randint(0, HEIGHT - SPRITE_SIZE)
    return [x, y]
 
def collision(rect1, rect2):
    """Detect collision between two rectangles."""
    return rect1.colliderect(rect2)
 
# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = robot_img
        self.rect = self.image.get_rect()
        self.rect.topleft = [100, 100]
        self.speed = 5
 
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
 
        # Keep player within screen bounds
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT)
 
# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = generate_position()
        self.speed = 3
        self.dir_x = random.choice([-1, 1])
        self.dir_y = random.choice([-1, 1])
 
    def update(self):
        self.rect.x += self.dir_x * self.speed
        self.rect.y += self.dir_y * self.speed
 
        # Bounce on window edges
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dir_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.dir_y *= -1
 
# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.topleft = generate_position()
 
    def reposition(self):
        self.rect.topleft = generate_position()
 
# Sprite groups
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
 
player = Player()
all_sprites.add(player)
 
coin = Coin()
all_sprites.add(coin)
 
enemy = Enemy()
all_sprites.add(enemy)
enemy_group.add(enemy)
 
# Game variables
score = 0
target_score = 10
 
# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    keys = pygame.key.get_pressed()
    player.update(keys)
    enemy_group.update()
 
    if collision(player.rect, coin.rect):
        score += 1
        coin.reposition()
 
    if pygame.sprite.spritecollide(player, enemy_group, False):
        score = 0
        for en in enemy_group:
            en.rect.topleft = generate_position()
 
    screen.fill(WHITE)
    all_sprites.draw(screen)
    draw_text(f"Score: {score}", 10, 10)
 
    if score >= target_score:
        draw_text("You Win!", WIDTH//2 - 70, HEIGHT//2, RED)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
 
    pygame.display.flip()
 
pygame.quit()