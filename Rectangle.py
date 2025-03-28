class Rectangle:
    
    def __init__(self, l, w):
        self.length = l
        self.width = w
        
    def rectangleArea(self):
        return self.length * self.width
    
newRectangle = Rectangle(12, 10)

area1 = newRectangle.rectangleArea()

print(f"For length {newRectangle.length} and for width {newRectangle.width} the area is {area1}")