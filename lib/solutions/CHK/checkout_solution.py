
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
        
        items = {'A':0,'B':0,'C':0,''}
 
