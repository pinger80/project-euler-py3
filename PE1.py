x = 0

for num in range(1000):
    if num%3==0:
        x += num
        print(num)
    elif num%5==0:
        x += num
        print(num)

print(x)
