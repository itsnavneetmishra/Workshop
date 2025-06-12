class Number:
    evens = []    # Class variable for even numbers
    odds = []     # Class variable for odd numbers
    
    def __init__(self, num):
        self.num = num
        if num % 2 == 0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)  # Changed from 'adds' to 'odds'

N1 = Number(21)
N2 = Number(32)
N3 = Number(43)
N4 = Number(54)
N5 = Number(65)
print("Even Numbers are:", Number.evens)
print("Odd Numbers are:", Number.odds)