colors_db = {}
class Colors:
    def __init__(self, red, green , blue):
        self.red = red
        self.green = green
        self.blue = blue

    def print_rgb_color(self):
        print(f"R:{self.red} G:{self.green} B:{self.blue}")
        print('-----------------------------------------------------')

c1  = Colors(1,2,3)
c2 = Colors(4,5,6)
c3 = Colors(7,8,9)
# c1.print_rgb_color()

colors_db[c1] = c1
colors_db[c2] = c2
colors_db[c3] = c3
print(colors_db)
for Colors in colors_db.values():
    Colors.print_rgb_color()