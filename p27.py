class Number:
    def __init__(self, x):
        self.value = x
    def __repr__(self):
        return "%s" % self.value
    def reducible(self):
        return False
        
class Complex:
    def __init__(self, l, r):
        self.left = l
        self.right = r
    def __repr__(self):
        return  "%s * %s" % (self.left, self.right)
    def reducible(self):
        return False
        
class Add:
    def __init__(self, l, r):
        self.left = l
        self.right = r
    def __repr__(self):
        return "%s + %s" % (self.left, self.right)
    def reducible(self):
        return True
    def reduce(self):
        if self.left.reducible():
            return Add(self.left.reduce(), self.right)
        elif self.right.reducible():
            return Add(self.left, self.right.reduce())
        else:
            return Number(self.left.value + self.right.value)

class Multiply:
    def __init__(self, l, r):
        self.left = l
        self.right = r
    def __repr__(self):
        return  "%s * %s" % (self.left, self.right)
    def reducible(self):
        return True
    def reduce(self):
        if self.left.reducible():
            return Add(self.left.reduce(), self.right)
        elif self.right.reducible():
            return Add(self.left, self.right.reduce())
        else:
            return Number(self.left.value * self.right.value)


#expression = Add(Multiply(Number(1), Number(2)), Multiply(Number(3), Number(4)))
#expression.reducible()
#expression.reduce()
#expression.reduce().reduce()
#expression.reduce().reduce().reduce()