from solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_sum2(self):
        assert SumSolution().compute(0,5) == 5

    def test_sum2(self):
        assert SumSolution().compute(5, 14) == 14