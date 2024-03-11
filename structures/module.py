from .ring import Ring

# Example of a module class:
class Module(Ring):
    def __init__(self, elements, addition, multiplication, product):
        super().__init__(elements, addition, multiplication)
        self.product = product

    def product(self, r, a):
        return self.product(r, a)