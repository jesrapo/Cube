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
