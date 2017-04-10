#def seconds(change_this):
#    pass
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]


def seconds(the_list):
    every_other_number = the_list[1::2]
    return every_other_number
    
print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
