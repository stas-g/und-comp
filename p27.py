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
    def reduce(self, a, b):
        if a.reducible() == True:
            return Add(self.left.reduce)

class Multiply:
    def __init__(self, l, r):
        self.left = l
        self.right = r
    def __repr__(self):
        return  "%s * %s" % (self.left, self.right)
    def reducible(self):
        return True


#Number(10).reducible()
#Add(20, 10).reducible()
#Multiply(45, 12).reducible()