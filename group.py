from element import Element

# Example of a group class:
class Group:
    def __init__(self, elements, operation):
        self.elements = elements
        self.operation = operation

    def apply(self, a, b):
        return self.operation(a, b)

    def identity(self):
        return None

    def inverse(self):
        return None

# Example of a group operation:
def addition_mod_n(n):
    def inner(a, b):
        return (a + b) % n
    return inner

# Example usage:
elements = [Element(i) for i in range(5)]
group = Group(elements, addition_mod_n(2))

print(group.apply(2, 3))
