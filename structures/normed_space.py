from .vector_space import VectorSpace

# Example of a normed space class:
class NormedSpace(VectorSpace):
    def __init__(self, elements, addition, product, norm):
        super().__init__(elements, addition, product)
        self.norm = norm

    def norm(self, a):
        return self.norm(a)