import pygame
import pygame.time
from dama_settings import *
from pygame.locals import *
from group import Group

pygame.init()
clock = pygame.time.Clock()
# print(dir(clock))
all_group = Group()
g1 = all_group.group_one()
# print("g1", g1)
g2 = all_group.group_two()
# print("g2", g2)
space = all_group.space_group()
# print("space", space)
invalid_ = all_group.invalid_group()
# print("invalide", invalid_)


class Gui(object):
    def __init__(self):
        self.run = True
        self.sc = pygame.display.set_mode((WIDTH, HEIGHT))

    def color_choose(self, group):
        if group == 1:
            color = (255, 0, 0)
        if group == 2:
            color = (0, 255, 0)
        if group == 3:
            color = (0, 0, 255)
        if group == 4:
            color = (255, 255, 255)
        return color

    def draw_rect(self, lists, light):
        for i in range(len(lists)):
            color = self.color_choose(light)
            rectangle = pygame.draw.rect(self.sc, color,
                                         ((lists[i][1]) * ratio_x, (lists[i][0]) * ratio_y, ratio_x, ratio_y))
        return True

    def get_coordinate(self, pos):
        x = pos[0]
        y = pos[1]
        return [y // ratio_y, x // ratio_x]

    def close_apps(self):
        for event in pygame.event.get():
            if event.types == QUIT:
                self.run = False
                exit()
            if event.types == MOUSEBUTTONDOWN:
                possition = event.pos
                coordinate = g.get_coordinate(possition)
                print(coordinate)



if __name__ == "__main__":
    g = Gui()
    while g.run:
        g.close_apps()
        g.sc.fill((255, 255, 255))
        g.draw_rect(g1, 1)
        g.draw_rect(g2, 2)
        g.draw_rect(space, 3)
        g.draw_rect(invalid_, 4)
        pygame.display.update()
        clock.tick(60)
