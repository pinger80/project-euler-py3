from math import factorial

def factorize(x) -> list:
    factors = []
    while x!=1:
        for fac in range(2,x+1):
            if x%fac==0:
                print(fac)
                factors.append(fac)
                x /= fac
                x = int(x)
                break
            
    return factors

smallest_num = factorial(20)

[factorized.append(factorize(x)) for x in range(2,21)]
concat_factorized = [j for i in factorized for j in i].sort()


print(concat_factorized)
