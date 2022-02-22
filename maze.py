from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (700, 500))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
clock = time.Clock()
speed = 3
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += speed

class Enemy(GameSprite):
    direction = "L"
    def update(self):
        if self.rect.x < 150:
            self.direction = "R"
        if self.rect.x >= 500:
            self.direction = "L"
        if self.direction == "R":
            self.rect.x += 5
        else:
            self.rect.x -= 5

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1   
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w1 = Wall(0, 225, 225, 50, 100, 200, 20)
w2 = Wall(0, 225, 225, 200, 100, 200, 20)
w3 = Wall(0, 225, 225, 400, 100, 20, 100)
w4 = Wall(0, 225, 225, 200, 300, 200, 20)
w5 = Wall(0, 225, 225, 100, 300, 200, 20)
w6 = Wall(0, 225, 225, 400, 300, 200, 20)
w7 = Wall(0, 225, 225, 500, 300, 200, 20)
hero = Player("hero.png", 50, 0, 15)
enemy = Enemy("cyborg.png", 200, 250, 10)
treasure = GameSprite("treasure.png", 600, 400, -200)
game = True
finish = False
font.init()
font = font.SysFont("Arial", 70)
win = font.render("YOU WIN!", True, (0, 255, 0))
lose = font.render("YOU LOSE!", True, (255, 0, 0))
while game:
    if finish != True:
        
        window.blit(background, (0, 0))
        hero.update()
        enemy.update()
        hero.reset()
        enemy.reset()
        treasure.reset()
        clock.tick(FPS)
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        if sprite.collide_rect(hero, treasure):
          window.blit(win, (200, 200))
          finish = True
          money.play()
        if sprite.collide_rect(hero, enemy):
          window.blit(lose, (200, 200))
          finish = True
          kick.play()
        if sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5) or sprite.collide_rect(hero, w6) or sprite.collide_rect(hero, w7):
          window.blit(lose, (200, 200))
          finish = True
          kick.play()
        

    for e in event.get():
        if e.type == QUIT:
            game = False


    
    display.update()
    clock.tick(120)


