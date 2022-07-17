from lib.solutions.CHK.checkout_solution import checkout

class TestCheckout():
    def test_checkout(self):

        assert checkout("ABCDEFABCDEF") == 300
        assert checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965