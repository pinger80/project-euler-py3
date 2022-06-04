output = 0

s,b = 1,1
num = 1

while (s+b < 4000000):
    if(s+b>4000000):
        break
    if((s+b)%2==0):
        output += s+b
        print(s+b)
    temp=b
    b=s+b
    s=temp
    print(b)
    

print(output)
    
