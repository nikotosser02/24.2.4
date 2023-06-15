import pytest

from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

# -------------------------------------------сложение
    def test_adding_succes(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsucces(self):
        assert self.calc.adding(self, 1, 1) == 3

# -------------------------------------------умножение

    def test_multiply_succes(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_multiply_unsucces(self):
        assert self.calc.multiply(self, 1, 1) == 3

# -------------------------------------------деление

    def test_division_succes(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_division_unsucces(self):
        assert self.calc.division(self, 1, 1) == 3

    # -------------------------------------------деление на 0
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)

# -------------------------------------------вычитание

    def test_subtraction_succes(self):
        assert self.calc.subtraction(self, 6, 2) == 4

    def test_subtraction_unsucces(self):
        assert self.calc.subtraction(self, 1, 1) == 3

# -------------------------------------------teardown

    def teardown(self):
        print("Выполнение метода Teardown")

