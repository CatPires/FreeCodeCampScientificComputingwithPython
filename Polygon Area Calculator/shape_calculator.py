class Rectangle:
    def __init__(self, width, height):  #= width
        self.width = width
        self.height = height

    # Replace .description() with __str__()
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
        return('New width set')

    def set_height(self, height):
        self.height = height
        return('New height set')
    
    def get_area(self):
        return (self.width * self.height)
    
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if (self.width > 50) or (self.height > 50):
          return("Too big for picture.")
        else:
          return(("*"*self.width + "\n") * (self.height))

    def get_amount_inside(self, other):
        return (self.width//other.width) * (self.height//other.height)

class Square(Rectangle):    
    def __init__(self, side):
        self.width = side
        self.height = side

    # Replace .description() with __str__()
    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, width):
        self.width = width
        self.height = width
        return('New width set')

    def set_height(self, height):
        self.width = height
        self.height = height
        return('New height set')
        
    def set_side(self, side):
        self.width = side
        self.height = side
        return('New side set')
        
    def get_amount_inside(self, other):
        return (self.width//other.width) * (self.height//other.height)


