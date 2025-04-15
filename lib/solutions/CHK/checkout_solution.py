
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1
         
        #initalise the counts of each item
        items = {'A':0,'B':0,'C':0,'D':0,'E':0, 'F':0, 'G':0,'H':0,'I':0,'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
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
        totalCost += (b//2)*45 + (b%2)*30
        
        totalCost += items['C']*20

        totalCost += items['D'] * 15

        totalCost += items['E'] * 40

        # 2F Get 1 Free
        f = items['F']
        paidFor =  f - (f//3)
        totalCost += paidFor * 10

        totalCost += items['G']*20

        #10 for 80, 5 for 45
        h = items['H']
        totalCost += (h//10)*80
        h%=10
        totalCost += (h//5)*45
        totalCost += (h%5)*10

        totalCost += items['I']*35

        totalCost += items['J']*60

        #2K for 150
        k = items['K']
        totalCost +=(k//2)*150
        totalCost+= (k%2)*80
        
        totalCost += items['L']*90

        # 3N Get 1M free
        m = items['M']
        n = items['N']
        freeM =  n//3
        if (m - freeM) < 0:
            m = 0
        else:
            m -= freeM
        totalCost += (m%3)*15

        totalCost += items['N'] * 40

        totalCost += items['O']*10

        #5 for 200
        p = items['P']
        totalCost +=(p//5)*200
        totalCost += (p%5)*50

        # 3Q for 80, 3R Get 1Q Free
        q = items['Q']
        r = items['R']
        freeQ =  r//3
        if (q - freeQ) < 0:
            q = 0
        else:
            q -= freeQ
        totalCost += (q//3)*80 + (q%3)*30

        totalCost += items['R'] * 50

        totalCost += items['S'] * 30

        totalCost += items['T'] * 20

        # 3U get 1 Free
        u = items['U']
        paidForU =  u - (u//4)
        totalCost += paidForU * 40
    
        #3V for 130, 2V fr 90
        v = items['V']
        totalCost += (v//3) * 130
        v%=3
        totalCost += (v//2) * 90
        totalCost += (v%2)* 50

        totalCost += items['W'] * 20

        totalCost += items['X'] * 90

        totalCost += items['Y'] * 10

        totalCost += items['Z'] * 50

        return totalCost









