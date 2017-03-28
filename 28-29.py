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

class Machine:
    def __init__(self, expression):
        self.expr = expression
    def step():
        self.expr = self.expr.reduce()
    def run(self):
        while self.expr.reducible():
            print(self.expr)
            step()
        

class Test:
    def__init__(self, x):
        self.a = x
    def fun():
        z = x*x
    def __repr__(self):
        


class Machine < Struct.new(:expression)
def step
self.expression = expression.reduce
end
def run
while expression.reducible?
puts expression
step
end