# 1238765 = 1+2+3+8+7+6+5 = x

n = int(input("Enter the number: "))
sum = 0
while n!=0:
    digit = n % 10
    sum += digit
    n = n // 10

print(sum)