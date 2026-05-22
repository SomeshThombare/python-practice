class Color:
    def __init__(self,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue

    def print_rgb_color(self):
        print(f"R:{self.red} G:{self.green} B:{self.blue}")

color = Color(1,2,3)
color.print_rgb_color()

