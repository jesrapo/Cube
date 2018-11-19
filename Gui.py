from tkinter import *
from constants import *
from sys import exit
from functools import partial

class Gui:
    def __init__(self, cube):
        root = Tk()

        #make these member variables
        self.root = root
        self.cube = cube

        self.set_up_window()
        self.load_in_cube()
        self.print_cube()
        root.mainloop()

    def set_up_window(self):
        root = self.root
        root.title("RUBIK'S CUBE")

    def quit_program(self):
        sys.exit(0)

    def make_cube_template(self):
        root = self.root
        cube = self.cube

        self.side_widgets = []

        for i in range(6):
            self.side_widgets.append([])
            for j in range(3):
                self.side_widgets[i].append([])
                for k in range(3):
                    rotate_current_side_and_update = partial(self.rotate_current_side_and_update, i)
                    new_widget = Button(root, bg = "black", command = rotate_current_side_and_update)
                    new_widget.config(width = WIDTH, height = HEIGHT, relief = "groove")
                    self.side_widgets[i][j].append(new_widget)
        #print(self.side_widgets)

    def rotate_current_side_and_update(self, side_number):
        self.cube.rotate_whole_side(side_number)
        self.update_cube()

    def load_in_cube(self):
        #make an empty cube template with no data
        self.make_cube_template() 

        #update the contents of that cube template with the current state of the cube
        self.update_cube()

    def update_cube(self):
        def update_side(side_number):
            def update_sticker(color_char, side_number, x, y):

                #get the widget that's at the given coordinate
                current_widget = self.side_widgets[side_number][x][y]

                #update the widget at that spot's color
                self.update_widget_color(current_widget, color_char)

            #for all 9 of the stickers on the given side
            for i in range(3):
                for j in range(3):

                    #get the character of the current spot
                    current_color_char = sides[side_number].get_sticker(i, j)

                    #update the sticker at the appropriate spot with the current color
                    update_sticker(current_color_char, side_number, i, j)

                    #print(current_color_char)

        root = self.root
        cube = self.cube
        sides = cube.sides

        #update all 6 sides
        for i in range(6):
            update_side(i)

        #print("Some square: %s" % sides[2].get_sticker(2, 1))
        #print("Cube now: %s" % self.side_widgets)

    def update_widget_color(self, current_widget, color_char):
            current_widget.config(bg = COLOR[color_char])

    def print_side(self, side_number, gui_location):
        for i in range(3):
            for j in range(3):
                x = self.get_x_coordinate(side_number, i)
                y = self.get_y_coordinate(side_number, j)
                current_widget = self.side_widgets[side_number][i][j]

                #the following is backwards because something somewhere else is backwards (x and y are switched)
                #FIXME
                current_widget.grid(row = x, column = y)

    def get_x_coordinate(self, side_number, column_number):
        #given the side number and the column number, return the x coordinate of the stickers in that position

        side_top_left_corner_x = SIDE_START[side_number][0]
        x_coordinate = side_top_left_corner_x + column_number
        return x_coordinate


    def get_y_coordinate(self, side_number, row_number):
        #given the side number and the row number, return the y coordinate of the stickers in that position
        side_top_left_corner_x = SIDE_START[side_number][1]
        y_coordinate = side_top_left_corner_x + row_number
        return y_coordinate

    def print_cube(self):
        root = self.root
        for i in range(6):
            self.print_side(i, i)

        #print the quit button
        button = Button(root, text = "Quit", command=self.quit_program)
        button.grid(row = 50, column = 50)
