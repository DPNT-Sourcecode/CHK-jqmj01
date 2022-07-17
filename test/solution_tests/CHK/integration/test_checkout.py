from lib.solutions.CHK.checkout_solution import checkout

class TestCheckout():
    def test_checkout(self):

        assert checkout("ABCDEFABCDEF") == 300
        assert checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 965
        assert checkout("ABCCSdaWD") == -1
        assert checkout("ABB&") == -1
        assert checkout("LGCKAQXFOSKZGIWHNRNDITVBUUEOZXPYAVFDEPTBMQLYJRSMJCWH") == 1880
