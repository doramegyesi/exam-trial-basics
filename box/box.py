#class Cuboid(object):
#    pass
    # Create a class that represents a cuboid:
    # It should take its three dimensions as constructor parameters (numbers)
    # It should have a method called `get_surface` that returns the cuboid's surface
    # It should have a method called `get_volume` that returns the cuboid's volume


class Cuboid():
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_surface(self):
        surface =

    def get_volume(self):
        volume = self.length * self.width * self.height
        return volume

box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print("The volume of the box is", box.get_volume()) # should print 6000
