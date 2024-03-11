from .algebra import Algebra

# Example of a Lie algebra class:
class LieAlgebra(Algebra):
    def __init__(self, elements, addition, product, multiplication, lie_bracket):
        super().__init__(elements, addition, product, multiplication)
        self.lie_bracket = lie_bracket

    def lie_bracket(self, a, b):
        return self.lie_bracket(a, b)