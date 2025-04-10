from solutions.HLO.hello_solution import HelloSolution


class TestHello():
    def test_Hello(self):
        assert HelloSolution("World") == "Hello, World!"

    def test_sum2(self):
        assert HelloSolution("Arturo") == "Hello, Arturo!"

    def test_sum2(self):
        assert HelloSolution("John") == "Hello, John!"