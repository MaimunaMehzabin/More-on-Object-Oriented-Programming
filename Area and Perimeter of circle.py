class Circle:
    
    def __init__(self, r):
        self.radius = r
        
    def circleArea(self):
        return 3.1416 * self.radius * self.radius
    
radius = float(input("Enter the Radius: "))
newCircle = Circle(radius)

area1 = newCircle.circleArea()

print(f"The Area is = {area1} ")