import pygame
from random import randint
 
class BoltKong:
    def __init__(self):
      pygame.init()
      self.window = pygame.display.set_mode((640, 480))
      pygame.display.set_caption("Bolt Kong")
      self.clock = pygame.time.Clock()
      self.load_assets()
      self.setup_game_state()
      self.main_loop()
 
    def load_assets(self):
      self.images = {name: pygame.image.load(f"{name}.png") for name in ["robot", "coin", "door", "monster"]}
      self.coin = self.images["coin"]
      self.font = pygame.font.SysFont("Gill Sans", 18)
      self.monster = pygame.transform.scale(
          self.images["monster"],
          (self.images["door"].get_width() - 10, self.images["door"].get_height() - 20)
      )
 
    def setup_game_state(self):
      self.robot_x = 640 - self.images["robot"].get_width() + 4
      self.robot_y = 434 - self.images["robot"].get_height()
      self.left = False
      self.right = False
      self.moving_up = False
      self.no_brick = True
      self.velocity_x = 20
      self.m_velocity = 0.2
      self.health = 50
      self.coins_txt = 0
      self.coins = []
      self.monster_x = 320 - self.monster.get_width() // 2 - 20
      self.monster_y = 240 - self.monster.get_height() // 2
      self.monsters = []
 
    def main_loop(self):
      while True:
          self.handle_events()
          self.update()
          self.draw()
          self.clock.tick(60)
 
    def handle_events(self):
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              exit()
          elif event.type == pygame.KEYDOWN:
              self.handle_keydown(event.key)
          elif event.type == pygame.KEYUP:
              self.handle_keyup(event.key)
 
    def handle_keydown(self, key):
      if key == pygame.K_LEFT:
          self.left = True
      elif key == pygame.K_RIGHT:
          self.right = True
      elif key == pygame.K_UP:
          self.robot_y -= 100
          self.moving_up = True
      elif key == pygame.K_F2:
          self.setup_game_state()
      elif key == pygame.K_ESCAPE:
          exit()
 
    def handle_keyup(self, key):
      if key == pygame.K_LEFT:
          self.left = False
      elif key == pygame.K_RIGHT:
          self.right = False
      elif key == pygame.K_UP:
          self.robot_y += 100
          self.moving_up = False
 
    def update(self):
        self.update_robot()
        self.update_coins()
        self.update_monsters()
 
    def update_robot(self):
      if self.moving_up:
        return
      #snap to ramp
      if self.robot_x <= 640 and self.robot_x >= -10:
        if self.robot_y == 228:
          self.robot_y = 217 
        if self.robot_y == 93:
          self.robot_y = 82
#would have liked the robot to go back down the ramp the way it comes up but couldn't find a way to do it
# also the robots don't come as fast or slow when I want, because I had only one random spawn, maybe if I had two?
# I would have liked the robot to jump up then back down automatically
#bottom
        if self.robot_y >= 232 and self.left:   
          self.robot_moving(-self.velocity_x)      
#middle
        if 93 < self.robot_y < 232 and self.right:   
          self.robot_moving(self.velocity_x)
#top
        if self.robot_y <= 93 and self.left:
          self.robot_moving(-self.velocity_x)
#game over
        if self.robot_y <= -42:
          self.game_over() if self.health < 50 else self.you_win()
          
 
    def robot_moving(self, move_x):
      if self.no_brick:
        self.robot_x += move_x
        self.no_brick = False
      else:
        self.robot_y += -4
        self.no_brick = True    
 
    def update_coins(self):
      if randint(1, 30) == 1:
          self.spawn_coin()
      for coin in self.coins[:]:
          self.move_coin(coin)
          if self.coin_collides_with_robot(coin):
            self.coins.remove(coin)
            self.coins_txt += 1
 
            if self.coins_txt % 2 == 0 and self.health < 50:   
              self.health += 1
              
    def you_win(self):
      self.window.fill((240, 240, 240))
      text = self.font.render("You Win", True, (50, 130, 80))
      self.window.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
      pygame.display.flip()
      pygame.time.delay(2000)
      self.setup_game_state()
 
    def spawn_coin(self):
      coin_x = -randint(20, 60)
      coin_y = 2
      self.coins.append([coin_x, coin_y])
 
    def move_coin(self, coin):
      x, y = coin
      if y < 120:
          coin[0] += 1.2
          coin[1] += 0.2
      elif 120 <= y < 260:
          coin[0] -= 1.4
          coin[1] += 0.3
      elif 260 <= y < 434:
          coin[0] += 1.5
          coin[1] += 0.3
 
    def coin_collides_with_robot(self, coin):
      coin_rect = pygame.Rect(coin[0], coin[1], self.coin.get_width(), self.coin.get_height())
      robot_rect = pygame.Rect(
          self.robot_x,
          self.robot_y,
          self.images["robot"].get_width(),
          self.images["robot"].get_height()
      )
      return coin_rect.colliderect(robot_rect)
    
    def update_monsters(self):     
      if randint(1, 60) == 1:        
        self.spawn_monsters()
 
      for monster in self.monsters[:]:
        x, y = monster
        self.move_monster(monster)
 
        if self.monster_collides_with_robot(monster):
          self.monsters.remove(monster)
          self.health -= 1
          if self.health <= 0:
            self.game_over()
 
    def spawn_monsters(self):
      monster_x = randint(self.monster_x - 5, self.monster_x + 5)
      self.monsters.append([monster_x, self.monster_y])
 
    def move_monster(self, monster):
      x, y = monster
      if x <= 640 and y < 120:
        monster[0] += 1.2 
        monster[1] += 0.25
      elif x >=320 and y < 255:
        monster[0] += -1.4
        monster[1] += 0.4
      elif x < 320 and y < 255:
        monster[0] += -1.2 
        monster[1] += 0.15
      elif y >= 255:
        monster[0] += 1.4
        monster[1] += 0.3  
        self.new_monster_top()    
 
    def new_monster_top(self):
      self.monster_x = -10
      self.monster_y = -10
 
    def monster_collides_with_robot(self, monster):
      monster_rect = pygame.Rect(monster[0]+5, monster[1], self.monster.get_width()-10, self.monster.get_height())
      half_height = self.images["robot"].get_height() / 2
      robot_rect = pygame.Rect(
          self.robot_x,
          self.robot_y + half_height,
          self.images["robot"].get_width(),
          self.images["robot"].get_height()/2
      )
      return monster_rect.colliderect(robot_rect)
    
    def game_over(self):
      self.window.fill((240, 240, 240))
      text = self.font.render("Game Over", True, (50, 130, 80))
      self.window.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
      pygame.display.flip()
      pygame.time.delay(2000)
      self.setup_game_state()
        
    def draw(self):
      self.window.fill((240, 240, 240))
      self.draw_bricks()            
      self.draw_hud()
      self.draw_characters()
      self.draw_coins()
      self.draw_monsters()
      pygame.display.flip()
 
    def draw_bricks(self):
      def draw_belt(start, end, step=20, adjust_y=None):
        surface = pygame.Surface((640, 480), pygame.SRCALPHA)
        for i in range(start, end, step):
            if start == 0:
                pygame.draw.rect(surface, (178, 34, 34), (i, i / 5, 20, 10))
            else:
                pygame.draw.rect(surface, (178, 34, 34), (i, adjust_y - i / 5, 20, 10))
        return surface
 
      self.window.blit(draw_belt(0, 641), (0, 40))
      self.window.blit(draw_belt(641, 0, -20, 260), (0, 40))
      self.window.blit(draw_belt(0, 641), (0, 310))
 
    def draw_coins(self):
      for c in self.coins:
        self.window.blit(self.coin, (c[0], c[1]))    
    
    def draw_hud(self):
      green = (50, 130, 80)
      pygame.draw.line(self.window, green, (0, 445), (640, 445), 4)
      self.draw_text("coins", self.coins_txt, 100)
      self.draw_text("health", self.health, 180)
      self.draw_text("F2 = new game", -1, 280)
      self.draw_text("Esc = exit game", -1, 415)
 
    def draw_text(self, name, attr, x):
      text = self.font.render(f"{name}: {attr}" if attr >=0 else name, True, (50, 130, 80))
      self.window.blit(text, (x, 452))
 
    def draw_characters(self):      
      self.window.blit(self.images["door"], (320 - self.images["door"].get_width() / 2, 240 - self.images["door"].get_height() / 2))
      self.window.blit(self.images["door"], (-10, -20))
      self.window.blit(self.images["robot"], (self.robot_x, self.robot_y))
 
    def draw_coins(self):
      for c in self.coins:
        self.window.blit(self.coin, (c[0], c[1])) 
    
    def draw_monsters(self):
      for m in self.monsters:
        self.window.blit(self.monster, (m[0], m[1]))      
 
if __name__ == "__main__":
    BoltKong()
 