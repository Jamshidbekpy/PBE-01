from datetime import datetime 

# x = datetime.now()
# # print(x)

# # print(x.year)
# # print(x.month)
# # print(x.day)
# # print(x.hour)
# # print(x.minute)
# # print(x.second)
# # print(x.microsecond)

# a = datetime(2020, 5, 17, 15, 30, 45)
# print(a)
# print(type(a))

# print(a.strftime("%Y-%m-%d %H:%M:%S"))
# print(type(a.strftime("%Y-%m-%d %H:%M:%S")))

# print(x.strftime("%w"))


# from math import fabs, pi, e, fabs, ceil, floor, sqrt



# print(pi)
# print(e)

# print(fabs(-5))
# print(ceil(3.2))
# print(floor(3.7))
# print(sqrt(16))

n = int(input("n: "))
if n % 2 == 1:
    n -= 1 
for i in range(n):
   if i >= n//2:
        if n % 4 == 0 and (i-n//2)+(i-n//2+1)>=(n-2)//2-1:
            print((n-1-i)*" ", end="")   
            print((i-n//2)*"*", end='')
            print((i-n//2+1)*"*", end="")
            
            print(((n-1-i)*2+1)*" ", end="")   
            print((i-n//2)*"*", end='')
            print((i-n//2+1)*"*", end="")
            print()
        elif n % 2 == 0 and (i-n//2)+(i-n//2+1)>=(n-2)//2:
            print((n-1-i)*" ", end="")   
            print((i-n//2)*"*", end='')
            print((i-n//2+1)*"*", end="")
            
            print(((n-1-i)*2+1)*" ", end="")   
            print((i-n//2)*"*", end='')
            print((i-n//2+1)*"*", end="")
            print()
          
for i in range(n, 0, -1):
    print((n - i) * " ", end="")
    for j in range(i):
        print("*", end="") 
    print((i - 1) * "*", end="")
    print()