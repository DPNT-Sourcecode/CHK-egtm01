from solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_specialOffers(self):
        assert CheckoutSolution().checkout("AAA") == 130
        assert CheckoutSolution().checkout("AAAA") == 180
        assert CheckoutSolution().checkout("BB") == 45
        assert CheckoutSolution().checkout("BBB") == 75

    def test_regular(self):
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("B") == 30
        assert CheckoutSolution().checkout("C") == 20
        assert CheckoutSolution().checkout("D") == 15
    
    def test_invalid(self):
        assert CheckoutSolution().checkout("F") == -1
        assert CheckoutSolution().checkout(123) == -1
    
    def test_specialOffers_E(self):
        assert CheckoutSolution().checkout("EEB") == 80
        assert CheckoutSolution().checkout("EEBB") == 110
        assert CheckoutSolution().checkout("EEBBB") == 140
