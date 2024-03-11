from .vector_space import VectorSpace

# Example of an algebra class:
class Algebra(VectorSpace):
    def __init__(self, elements, addition, product, multiplication):
        super().__init__(elements, addition, product)
        self.multiplication = multiplication

    def multiply(self, a, b):
        return self.multiplication(a, b)