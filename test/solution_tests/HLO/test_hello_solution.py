from solutions.HLO.hello_solution import HelloSolution


class TestHello():
    def test_Hello(self):
        assert HelloSolution().hello("World") == "Hello, World!"

    def test_sum2(self):
        assert HelloSolution().hello("Arturo") == "Hello, Arturo!"

    def test_sum2(self):
        assert HelloSolution().hello("John") == "Hello, John!"