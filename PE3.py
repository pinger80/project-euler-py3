num = 600851475143
factor = 1
largest_factor = 0

while(largest_factor < num):
    if(num%(factor+1)==0):
        num = num/(factor+1)
        print(factor+1)
        if(factor+1 > largest_factor):
            largest_factor = factor+1
        factor = 1
    else:
        factor += 1
    

print(largest_factor)
