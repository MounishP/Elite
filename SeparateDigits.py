# 123 === 3/2/1

n = int(input("Enter the number: "))

while n != 0:            #123!=0(T), 12!=0(T), 1!=0(T), 0!=0(F)
    digit = n % 10       # 123%10 = 3, 12%10 = 2, 1%10 = 1
    n = n//10            # 123//10 = 12, 12//10 = 1, 1//10 = 0
    print(digit)         # 3, 2, 1



