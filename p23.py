class Number:
    def __init__(self, x):
        self.value = x
        
class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imag = b

class Add:
    def __init__(self, l, r):
        self.left = l
        self.right = r

class Multiply:
    def __init__(self, l, r):
        self.left = l
        self.right = r


#Add(Multiply(Number(1), Number(2)), Multiply(Number(3), Number(4)))