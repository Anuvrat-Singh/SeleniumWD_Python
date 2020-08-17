class fruit():
    def __init__(self):
        print("fruit created")

    def nutrition(self):
        print("This is a nutritiuos fruit")

    def fruit_shape(self):
        print("The fruit is cylindrical")

class kiwi(fruit):
    def __init__(self):
        super(kiwi, self).__init__()
        print("Kiwi is created")

    def nutrition(self):
        print("Kiwi has vitamin c")

    def color(self):
        print("Kiwi skin color is brown")
#
# f = fruit()
# f.nutrition()
# f.fruit_shape()

k = kiwi()
k.nutrition()
k.fruit_shape()
k.color()