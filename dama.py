from dama_settings import *
from group import *


class Dama(Group):
    def __init__(self):
        super(Dama, self).__init__()
        self.active_coordinate = None
        self.eaten_value = None
        self.temporay_coordinate = None
        self.active_palyer = None
        self.given_coordinate = None
        self.two_step_list = []
        self.neighboor = None
        self.eaten_list = []

    def neighboor_check(self, active, passive,group):
        active_x,active_y = active
        passive_x,passive_y = passive
        if group == self.group_one():
            if [active_x - passive_x ,active_y - passive_y] == [-1,-1] or [active_x - passive_x ,active_y - passive_y]==[-1,1]:
                return True
        if group == self.group_two():
            if [active_x - passive_x, active_y - passive_y] == [-1, -1] or [active_x - passive_x,
                                                                           active_y - passive_y] == [1, -1]:
                return True

    def two_step_check(self, active, passive):
        pass

    def display_error(self, code):
        if code == 'one':
            print("choose active coordinate first")
        if code == 'invalid':
            print('invalid choice')

    def clear_list(self):
        pass

    def main_game(self, active_player):
        if self.active_palyer == active_player:
            if self.active_coordinate is None:
                if self.given_coordinate in self.active_palyer:
                    self.active_coordinate = self.given_coordinate
                    self.clear_list()
                    self.temporay_coordinate = self.active_coordinate
                if self.given_coordinate in self.space_group():
                    self.display_error('one')
                else:
                    self.display_error("invalid")
        if self.active_coordinate is not None:
            if self.given_coordinate in self.active_palyer:
                self.active_coordinate = self.given_coordinate
                self.clear_list()
                self.temporay_coordinate = self.active_coordinate
            if self.given_coordinate in self.space_group():
                if self.temporay_coordinate == self.active_coordinate:
                    if self.neighboor_check(self.temporay_coordinate, self.given_coordinate):
                        self.neighboor = self.given_coordinate
                        self.clear_list()
                    if self.two_step_check(self.temporay_coordinate,self.given_coordinate):
                        self.clear_list()
                        self.two_step_list.append(self.given_coordinate)
                        self.eaten_list.append(self.eaten_value)
                        self.temporay_coordinate = self.given_coordinate
                else:
                    if self.two_step_check(self.temporay_coordinate,self.given_coordinate):
                        self.two_step_list.append(self.given_coordinate)
                        self.eaten_list.append(self.eaten_value)
                        self.temporay_coordinate =self.given_coordinate




if __name__ == "__main__":
    print(dir(Dama()))
