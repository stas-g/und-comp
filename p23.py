class Number:
    def __init__(self, x):
        self.value = x
    def __repr__(self):
        return "#< class Number value = %s >" % self.value
        

class Add:
    def __init__(self, l, r):
        self.left = l
        self.right = r
    def __repr__(self):
        return "#< class Add left = %s, right = %s >" % (self.left, self.right)


class Multiply:
    def __init__(self, l, r):
        self.left = l
        self.right = r
    def __repr__(self):
        return "#< class Multiply left = %s, right = %s >" % (self.left, self.right)
        

#Add(Multiply(Number(1), Number(2)), Multiply(Number(3), Number(4)))