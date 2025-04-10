
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        
        #initalise the counts of each item
        items = {'A':0,'B':0,'C':0,'D':0,'E':0}
        #go through each item iteratively and increment
        for item in skus:
            if item not in items:
                return -1
            items[item]+=1

        totalCost = 0

        #calculate cost of SKU A items, 5A > 3A > individual
        a = items['A']
        totalCost += (a//5) * 200
        a%=5
        totalCost += (a//3) * 130
        totalCost += (a%3)* 50

        #calculate cost of SKU B items, 30 each and 2 for 45
        b = items['B']
        e = items['E']
        freeB =  e//2
        if (b - freeB) < 0:
            b = 0
        else:
            b -= freeB
        total += (b//2)*45 + (b%2)*30
        
        totalCost += items['C']*20

        totalCost += items['D'] * 15

        totalCost += items['E'] * 40

        return totalCost

