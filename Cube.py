from constants import *
from functions import *
from Side import *
from Gui import *

class Cube:
    def __init__(self):
        #initializer that makes six 9-sticker sides, each one with a single letter on all stickers

        #list of sides
        self.sides = []

        #make 6 single-color 9-sticker sides, with colors being represented by numbers 0-5
        for i in range(6):
            new_side = Side(i) #make a side of the current color (represented by i)
            self.sides.append(new_side)

    def open_window(self):
        #open the GUI window!
        gui = Gui(self)

    def rotate_stickers(self, sticker_coordinates_list):
        #rotates 4 stickers around on the cube right-ward

        #make an array of the 4 stickers' colors
        corner_colors = []
        for i in range(4):
            x = sticker_coordinates_list[i][0]
            y = sticker_coordinates_list[i][1]
            z = sticker_coordinates_list[i][2]
            sticker_color = self.sides[x].get_sticker(y, z)
            corner_colors.append(sticker_color)

        #rotate the colors
        rotate(corner_colors)

        #put the 4 colors back, rotated
        for i in range(4):
            x = sticker_coordinates_list[i][0]
            y = sticker_coordinates_list[i][1]
            z = sticker_coordinates_list[i][2]
            new_color = corner_colors[i]
            self.sides[x].change_sticker(y, z, new_color)
            
    def reverse_rotate_stickers(self, sticker_coordinates_list):
        #rotates 4 stickers around on the cube left-ward

        #make an array of the 4 stickers' colors
        corner_colors = []
        for i in range(4):
            x = sticker_coordinates_list[i][0]
            y = sticker_coordinates_list[i][1]
            z = sticker_coordinates_list[i][2]
            corner_colors.append(self.sides[x].get_sticker(y, z))

        #rotate the colors
        reverse_rotate(corner_colors)

        #put the 4 colors back, rotated
        for i in range(4):
            x = sticker_coordinates_list[i][0]
            y = sticker_coordinates_list[i][1]
            z = sticker_coordinates_list[i][2]
            new_color = corner_colors[i]
            self.sides[x].change_sticker(y, z, new_color)

    def rotate_whole_side(self, side_number):
        #rotates a side's face and all the adjacent sides as well

        self.rotate_face(side_number)
        self.rotate_adjacent_sides(side_number)

    def rotate_face(self, side_number):
        #rotates just the face of a side, leaving the other affected sides to another function

        s = side_number 
        corners = [[s, 0, 0], [s, 0, 2], [s, 2, 2], [s, 2, 0]]
        edges = [[s, 0, 1], [s, 1, 2], [s, 2, 1], [s, 1, 0]]

        self.rotate_stickers(corners)
        self.rotate_stickers(edges)

    def rotate_adjacent_sides(self, side_number):
        #rotate the sides adjacent to the current side

        up_side = self.get_up_side_row(side_number)
        down_side = self.get_down_side_row(side_number)
        right_side = self.get_right_side_row(side_number)
        left_side = self.get_left_side_row(side_number)
    
        #rotate the 3-sticker rows of the 4 adjacent sides
        for i in range(3):
            #rotate those 4 sides
            self.rotate_stickers([up_side[i], right_side[i], down_side[i], left_side[i]])

    def get_column(self, side_number, column_number, is_it_increasing):
        s = side_number
        c = column_number

        if (is_it_increasing):
            return [[s, 0, c], [s, 1, c], [s, 2, c]]
        else:
            return [[s, 2, c], [s, 1, c], [s, 0, c]]

    def get_row(self, side_number, row_number, is_it_increasing):
        s = side_number
        r = row_number

        if (is_it_increasing):
            return [[s, r, 0], [s, r, 1], [s, r, 2]]
        else:
            return [[s, r, 2], [s, r, 1], [s, r, 0]]

    #def get_adjacent_sides_rows_and_columns(self, side_number):
    def get_up_side_row(self, side_number):

        #dictionary of the different rows/column coordinates that are above each side
        rows_columns = {
            0: self.get_row(5, 2, True),
            1: self.get_column(0, 0, True),
            2: self.get_row(0, 2, True),
            3: self.get_column(0, 2, False),
            4: self.get_row(2, 2, True),
            5: self.get_row(4, 2, True)
        }

        return rows_columns.get(side_number)

    def get_down_side_row(self, side_number):

        #dictionary of the different rows/column coordinates that are below each side
        rows_columns = {
            0: self.get_row(2, 0, True),
            1: self.get_column(4, 0, False),
            2: self.get_row(4, 0, False),
            3: self.get_column(4, 2, True),
            4: self.get_row(5, 0, True),
            5: self.get_row(0, 0, True)
        }

        return rows_columns.get(side_number)
            
    def get_right_side_row(self, side_number):

        #dictionary of the different rows/column coordinates that are to the left of each side
        rows_columns = {
            0: self.get_row(3, 0, False),
            1: self.get_column(2, 0, True),
            2: self.get_column(3, 0, True),
            3: self.get_column(5, 2, False),
            4: self.get_row(3, 2, True),
            5: self.get_column(3, 2, False)
        }

        return rows_columns.get(side_number)

    def get_left_side_row(self, side_number):

        #dictionary of the different rows/column coordinates that are to the right of each side
        rows_columns = {
            0: self.get_row(1, 0, True),
            1: self.get_column(5, 0, False),
            2: self.get_column(1, 2, False),
            3: self.get_column(2, 2, True),
            4: self.get_row(1, 2, False),
            5: self.get_column(1, 0, False)
        }

        return rows_columns.get(side_number)
