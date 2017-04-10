#def count_as(change_this):
#    pass
    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

text = open("afile.txt", "r")
t = text.read()
text.close()

def count_as(filename):
    for letter in t:
        number_of_as = 0
        if letter == "a" or letter == "A":
            number_of_as += 1
    return number_of_as
    try:
        filename = open('filename.txt', 'r')
    except:
        print(0)

print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
