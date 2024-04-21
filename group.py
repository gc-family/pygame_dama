class Group(object):
    def __init__(self):
        # x -axis is column , y-axis is row
        self.G1 = []
        self.G2 = []
        self.space = []
        self.invalid =[]
        self.row = 3
        self.total_row = 8
        self.column = 8

    def group_one(self):
        for i in range(self.row):
            for j in range(self.column):
                if (i + j) % 2 == 0:
                    self.G1.append([i, j])
        return self.G1

    def group_two(self):
        for i in range(self.column - self.row, self.column):
            for j in range(self.column):
                if (i + j) % 2 == 0:
                    self.G2.append([i, j])
        return self.G2

    def space_group(self):
        for i in range(self.row, self.column - self.row):
            for j in range(self.column):
                if (i + j) % 2 == 0:
                    self.space.append([i, j])
        return self.space
    def invalid_group(self):
        for i in range(self.total_row):
            for j in range(self.column):
                if (i+j)%2==1:
                    self.invalid.append([i,j])
        return self.invalid

if __name__ == "__main__":
    g = Group()
    print(g.group_one())
    print(g.group_two())
    print(g.space_group())
    print(g.invalid_group())
