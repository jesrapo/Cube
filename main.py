from constants import *
from Cube import *

print()
print("To quit at any time, press 9.")

my_cube = Cube()

#program will exit as soon as user enters 9 (temporary)
while(True):
    my_cube.print_cube()
    side_to_turn = ask_user_which_side_to_turn()
    my_cube.rotate_whole_side(side_to_turn)
