# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
        
#     def area(self):
#         return self.width * self.height
    
#     def perimeter(self):
#         return 2 * (self.width + self.height)
    
# rect = Rectangle(3,8)
# rect1 = Rectangle(7,9)
# rect2 = Rectangle(5,2)

# for rect3 in [rect, rect1, rect2]:
#     print(f"Прямоугольник: ширина = {rect3.width}, высота = {rect3.height}")
#     print(f"Площадь: {rect3.area()}")
#     print(f"Периметр: {rect3.perimeter()}")
#     print()



class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width * self.height)
    
rect1 = Rectangle(5, 6)
rect2 = Rectangle(2, 4)
rect3 = Rectangle(9, 5)


for rect in [rect1,rect2,rect3]:
    print(f"Прямоугольник: ширина = {rect.width}, высота = {rect.height}")
    print(f"Площадь: {rect.area()}")
    print(f"Периметр: {rect.perimeter()}")
    print()
