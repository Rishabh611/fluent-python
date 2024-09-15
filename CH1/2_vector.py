import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __mull__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    

vec1 = Vector(3,4)
vec2 = Vector(6,8)
print(vec1, vec2)
print(abs(vec1), abs(vec2))
print(vec1 + vec2)