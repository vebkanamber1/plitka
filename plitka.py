import pygame
import os
import sys

from Tools.demo.sortvisu import WIDTH

current_path = os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('Aria', 40)
FPS = 60
clock = pygame.time.Clock()

on_image = pygame.image.load('data/image/on.png').convert_alpha()
of_image = pygame.image.load('data/image/of.png').convert_alpha()
p_1_image = pygame.image.load('data/image/p_1.png').convert_alpha()
p_2_image = pygame.image.load('data/image/p_2.png').convert_alpha()

plitka_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

list_player = []

NUM_HOD = 0

maps_list = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

def game():
    screen.fill('grey')
    plitka_group.update()
    plitka_group.draw(screen)
    plitka_group.update()
    player_group.draw(screen)
    if len(player_group) == 1:
        text = f'win player: {list_player[0].name}'
    else:
        text = f'ход игрока - {list_player[NUM_HOD].name}'
    text_render = font.render(text, 'black', True)
    screen.blit(text_render,(725,170))
    pygame.display.update()





class Plitka(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = on_image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.on = True
        self.adr = (self.rect.y //100, self.rect.x // 100 )

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            self.on = False
            self.image = of_image
            maps_list[self.adr[0]][self.adr[1]] = 1

        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.on:
                if self.rect.left < self.rect.right and self.rect.top < self.rect.bottom:
                    list_player[NUM_HOD].step = True




def drawmaps():
    for i in range(0,7):
        for j in range(0,7):
            x = 100 * i
            y = 100* j
            pos = (x,y)
            plitka = Plitka(pos)
            plitka_group.add(plitka)

class Player(pygame .sprite.Sprite):
    def __init__(self,image,x,y, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect. x = x
        self.rect. y = y
        self.hod = False
        self.step =False
        self.name = name

    def proverka(self):
        pl = pygame.sprite.spritecollide(self, plitka_group, False)[0]
        x = pl.adr[1]
        y = pl.adr[0]
        list_hod = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                index_y = y + i
                index_x = x + j
                if -1 < index_x < 7 and -1 < index_y < 7:
                    if maps_list[index_y][index_x] == 0:
                        list_hod.append(True)
        return True in list_hod
    def update(self):
        global NUM_HOD
        if self.hod:
            if not self.proverka():
                NUM_HOD += 1
                if NUM_HOD > len(list_player) - 1:
                    NUM_HOD = 0
                    list_player[NUM_HOD].hod = True
                list.remove(self)
                self.kill()
            if pygame.mouse.get_pressed()[0]:
                if self.stop:
                    click_pos = pygame.mouse.get_pos()
                    if ((click_pos[0] - self.rect.center[0]) ** 2 + (
                            click_pos[1] - self.rect.center[1]) ** 2) ** 0.5 <= 150:
                        self.rect.x = 10 + click_pos[0] // 100 * 100
                        self.rect.y = 10 + click_pos[1] // 100 * 100
                        self.step = False
                        NUM_HOD += 1
                        if NUM_HOD > len(list_player) - 1:
                            NUM_HOD = 0
                        list_player[NUM_HOD].hod = True

player_1 = Player(p_1_image, 10,10, 'Egor')
player_group.add(player_1)
list_player.append(player_1)
player_2 = Player(p_2_image, 610,610,'Sasha')
player_group.add(player_2)
list_player.append(player_2)
list_player[0].hod = True






















drawmaps()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game()


    clock.tick(FPS)


