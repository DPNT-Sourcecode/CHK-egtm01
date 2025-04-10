
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        
        #initalise the counts of each item
        items = {'A':0,'B':0,'C':0,'D':0}
        #go through each item iteratively and increment
        for item in skus:
            if item not in items:
                return -1
            items[item]+=1

        totalCost = 0

        #calculate cost of SKU A items, 50 each and 3 for 130
        a = items['A']
        total += (a//3)*130 + (a%3)*50

        b
