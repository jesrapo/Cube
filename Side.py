class Side:
    def __init__(self, c):
        #initialize the 3x3 list of stickers
        self.stickers = [[c, c, c], [c, c, c], [c, c, c]]

        #find the coordinates of the adjacent rows/columns, and store them as piece's up, down, left, right members
        self.left = self.find_left()
        self.right = self.find_right()
        self.up = self.find_up()
        self.down = self.find_down()

    def find_left(self):
        return 2

    def find_right(self):
        return 2

    def find_up(self):
        return 2

    def find_down(self):
        return 2
    
    def get_sticker(self, x, y):
        #returns the color at the given coordinates
        return self.stickers[x][y]

    def get_row(self, y):
        #returns a list of the colors at the given row
        row = self.stickers[y]
        return row

    def get_column(self, x):
        #returns a list of the colors at the given column
        column = []
        for i in range(3):
            column.append(self.stickers[i][x])
        return column

    def change_sticker(self, x, y, new_color):
        self.stickers[x][y] = new_color
