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
        assert CheckoutSolution().checkout("Z1") == -1
        assert CheckoutSolution().checkout(123) == -1
    
    def test_specialOffers_E(self):
        assert CheckoutSolution().checkout("EEB") == 80
        assert CheckoutSolution().checkout("EEBB") == 110
        assert CheckoutSolution().checkout("EEBBB") == 125

    def test_specialOffers_F(self):
        assert CheckoutSolution().checkout("FFFFF") == 40
        assert CheckoutSolution().checkout("FFF") == 20
        assert CheckoutSolution().checkout("FFFF") == 30

    def test_specialOffers_R4(self):
        assert CheckoutSolution().checkout("HHHHH") == 45
        assert CheckoutSolution().checkout("HHHHHHHHHH") == 80
        assert CheckoutSolution().checkout("NNNM") == 120
        assert CheckoutSolution().checkout("RRRQ") == 150
        assert CheckoutSolution().checkout("UUUU") == 120
        assert CheckoutSolution().checkout("VV") == 90
        assert CheckoutSolution().checkout("VVV") == 130
        
    def test_groupDiscounts_R5(self):
        assert CheckoutSolution().checkout("STXYZ") == 