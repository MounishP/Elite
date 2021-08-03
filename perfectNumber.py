# 6 --> 1,2,3 --> 1+2+3 = 6

n = int(input("Enter the number: "))


def isPerfect(n):
    sum = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sum = sum + i
    return sum == n


print(isPerfect(n))
