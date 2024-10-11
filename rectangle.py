class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield f"{{'length': {self.length}}}"
        yield f"{{'width': {self.width}}}"

length = int(input("Enter Length: "))
width = int(input("Enter Width: "))
rectangle = Rectangle(length, width)
for dimension in rectangle:
    print(dimension)