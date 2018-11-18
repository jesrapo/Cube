import sys

def rotate(original_list):
    #rotate the list given right-ward: push each element forward one spot

    #make a new list that is the old one rotated
    rotated_list = []

    #the last element of the old list will be the first element of the rotated one
    last = original_list[-1]
    rotated_list.append(last)

    #rotate the rest of the list
    for i, x in enumerate(original_list[:-1]):
        rotated_list.append(original_list[i])

    #set the list given as the new rotated one
    original_list[:] = rotated_list


def reverse_rotate(some_list):
    #rotate the list given left-ward: push each element backward one spot

    for i, x in enumerate(some_list[:-1]):
        previous = some_list[i+1]
        some_list[i+1] = some_list[i]
        some_list[i] = previous


def twice_rotate(some_list):
    rotate(some_list)
    rotate(some_list)

def ask_user_which_side_to_turn():
    #recursively call function until a valid int is given, then return that int

    try: 
        print()
        side_number = int(input("Which side would you like to move? (0-5) "))
    except ValueError:
        print("That wasn't an integer!")
        return ask_user_which_side_to_turn()
    else:
        #if it's in the valid range, return it
        if(side_number >= 0 and side_number <= 5):
            return side_number

        #if the user returned 9, quit the program (temporary)
        elif(side_number == 9):
            sys.exit(0)

        #if it's not in the valid range, give a different error and call the function again
        else:
            print("That integer is not in the appropriate range!")
            return ask_user_which_side_to_turn()
