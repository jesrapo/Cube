from constants import *
from functions import *
from Side import *

class Cube:
    def __init__(self):
        #initializer that makes six 9-sticker sides, each one with a single letter on all stickers

        #list of sides
        self.sides = []

        #make 6 single-color 9-sticker sides, with colors being represented by letters a-f
        for i in range(6):
            c = chr(i + 97) #letters a-f
            new_side = Side(c)
            self.sides.append(new_side)

    def print_cube(self):

        def print_sides(start, end):
            #prints multiple sides in a single line
            for j in range(3):
                for k in range(start, end):
                    for i in range(3):
                        print(self.sides[k].get_sticker(j, i), end = " ")
                    print("  ", end = " ")
                print()
            print()

        def print_side_with_space(side_number):
            #prints a single side in a line, with space before it
            for j in range(3):
                print(8*" ", end = " ")
                for i in range(3):
                    print(self.sides[side_number].get_sticker(j, i), end = " ")
                print()
            print()

        #print side 0 on one line, then sides 1-3 on the next, then side 4 and 5
        print()
        print_side_with_space(0)
        print_sides(1, 4)
        print_side_with_space(4)
        print_side_with_space(5)
        print()

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

    def front_test(self):

        #numbers for the current side's up, left, self, right, down sides
        u, l, s, r, d = 0, 1, 2, 3, 4

        #rotate the stickers on the current side
        self.rotate_stickers([[s, 0, 0], [s, 0, 2], [s, 2, 2], [s, 2, 0]])
        self.rotate_stickers([[s, 0, 1], [s, 1, 2], [s, 2, 1], [s, 1, 0]])

        #rotate the stickers on the non-current side
        for i in range(3):
            j = 2 - i
            self.rotate_stickers([[u, 2, i], [r, i, 0], [d, 0, j], [l, j, 2]])

    def right_test(self):

        #numbers for the current side's up, left, self, right, down sides
        u, l, s, r, d = 2, 4, 3, 0, 5

        #rotate the stickers on the current side
        self.rotate_stickers([[s, 0, 0], [s, 0, 2], [s, 2, 2], [s, 2, 0]])
        self.rotate_stickers([[s, 0, 1], [s, 1, 2], [s, 2, 1], [s, 1, 0]])

        #rotate the stickers on the non-current side
        for i in range(3):
            j = 2 - i
            self.rotate_stickers([[u, 2, i], [r, i, 0], [d, 0, j], [l, j, 2]])

    #DEFINE RELATIONSHIPS BETWEEN ALL THE SIDES: WHO IS WHOSE UP, WHO IS WHOSE DOWN, LEFT, RIGHT, ETC


    '''
    def right_inverted(self):
    def left(self):
    def left_inverted(self):
    def up(self):
    def up_inverted(self):
    def down(self):
    def down_inverted(self):
    def front(self):
    def front_inverted(self):
    def back(self):
    def back_inverted(self):
    '''

    '''
    side 2:
        above:
            side 2 top->
            side 0 bottom
        below:
            side 2 bottom->
            side 4 top
        left:
            side 2 left->
            side 1 right
        right:
            side 2 right->
            side 3 left
    '''
    '''
        initialize_side_relationships():
            #initialize sides with who is on whose side

            #side 2 has 0 above, 
            assign_adjacent_sides(2, 0, 4, 1, 3, 5)
    '''
    
    def front(self):
        self.rotate_whole_side(2)

    def right(self):
        self.rotate_whole_side(3)

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
