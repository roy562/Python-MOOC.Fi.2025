# Complete your game here

#My game idea is similar to half part of brick breaker game 
    #A ball (here coin) bounces around the screen.
    #A robot/door at the bottom of the screen can be moved by user by pressing left and right arrow
    #If the robot collides with bouncing ball, the ball remains in play and bounces back upwards. 
        #Good to have - the speed of the ball increases after 5 collisions to make the game tougher by time
    #If the ball touches the floor without colliding with robot, user looses 1 life and ball resets. 
    #After the lives are 0, the game ends and user has to close the window or press F2 to restart the game again. 
    #Bugs:
        #At some particular angles ball causes multiple collisions with the door even during single collision
        #Could not flip the door image to make it horizontal for better game experience
        #Could not make the ball go into different directions upon reset. 
            #Taking random numbers for ball velocity didn't work as it also took value 0 sometimes 

import pygame
import random

#Door Class
class Door:
    def __init__(self, window_width:int, window_height:int):
        
        self.door=pygame.transform.flip(pygame.image.load("door.png"), False, True) #Flip image is not working
        self.width=self.door.get_width()
        self.height=self.door.get_height()

        self.x=random.randint(250,400)
        self.y=window_height-self.height
        self.velocity=5

    def get_coll_dims(self):
        return self.door.get_rect(topleft=(self.x,self.y))
        
    def display(self, main_window):
        main_window.blit(self.door, (self.x, self.y))
   
    def reset(self, window_width:int, window_height:int):
        self.door_x=random.randint(250,400)
        self.door_y=window_height-self.height    

    def move(self, to_left:bool,to_right:bool, window_width:int = 0):
        if to_right and (self.x+self.width <= window_width):
            self.x += self.velocity
        if to_left and (self.x >=0):
            self.x -= self.velocity

class Coin:
    def __init__(self, window_width:int, window_height:int):
        
        self.coin=pygame.image.load("coin.png")
        self.width=self.coin.get_width()
        self.height=self.coin.get_height()

        self.x=random.randint(0,window_width-self.width)
        self.y=random.randint(0,window_height//2)
        self.velocity_x=3   #Good to have: ball goes in different directions after each life is lost
        self.velocity_y=3

    def get_coll_dims(self):
        return self.coin.get_rect(topleft=(self.x,self.y)) 
        
    def display(self, main_window):
        main_window.blit(self.coin, (self.x, self.y))
   
    def reset(self, window_width:int, window_height:int):
        self.x=random.randint(0,window_width-self.width)
        self.y=random.randint(0,window_height//2)
        self.velocity_x=2
        self.velocity_y=2   
    
    def move(self, window_width:int, window_height:int):
        if self.x <= 0 or self.x+self.width >= window_width:
            self.velocity_x = -self.velocity_x
        if self.y <= 0 or self.y+self.height >= window_height:
            self.velocity_y = -self.velocity_y

        self.x+=self.velocity_x
        self.y+=self.velocity_y

class Lives:
    
    def __init__(self, lives_left:int):
        self.x=550
        self.y=10
        self.lives_left = lives_left
        
    def display(self, main_window):
        game_font=pygame.font.SysFont("Arial", 28)
        text=game_font.render(f"Lives: {self.lives_left}", True, (255,0,0))
        main_window.blit(text, (self.x, self.y))
        
    def reduce_life_by_one(self):
        self.lives_left-=1

    def get_lives(self):
        return self.lives_left     

class BrickBreaker:
    def __init__(self):
        pygame.init()

        #Initialize the window and display game name
        self.window_width,self.window_height  = 640,480
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("BrickBreaker")

        self.door = Door(self.window_width,self.window_height)
        self.ball = Coin(self.window_width,self.window_height)
        self.lives = Lives(3)
        
        self.main_loop()
    
    def main_loop(self):
        to_left = False
        to_right = False

        game_finished = False

        clock = pygame.time.Clock()
        collisions = 0

        while True:
            self.window.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        to_left = True
                    if event.key == pygame.K_RIGHT:
                        to_right = True
                    if event.key == pygame.K_F2:
                        self.__init__()
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        to_left = False
                    if event.key == pygame.K_RIGHT:
                        to_right = False
                      
            if self.lives.get_lives() > 0:
                self.lives.display(self.window)
                self.ball.display(self.window)
                self.door.display(self.window)

                self.door.move(to_left, to_right, self.window_width)
                self.ball.move(self.window_width, self.window_height)

                door_dims = self.door.get_coll_dims()
                ball_dims = self.ball.get_coll_dims()

                if pygame.Rect.colliderect(door_dims, ball_dims):
                    self.ball.velocity_y = -self.ball.velocity_y
                    collisions+=1
                
                if collisions == 5:
                    self.ball.velocity_y=round(self.ball.velocity_y*1.5)
                    collisions=0
                
                if self.ball.y+self.ball.height >= self.window_height:
                    self.ball.reset(self.window_width, self.window_height)
                    self.door.reset(self.window_width, self.window_height)
                    self.lives.reduce_life_by_one()
            else:
                game_font=pygame.font.SysFont("Arial", 28)
                text=game_font.render(f"Game Over. Press F2 to restart the game.", True, (255,0,0))
                self.window.blit(text, (100,240))

            pygame.display.flip()
            clock.tick(60)
            
    
if __name__ == "__main__":
    BrickBreaker()