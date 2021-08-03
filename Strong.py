# 145 = 1!+4!+5! == 145

n = int(input("Enter the number: "))


def fact(digit):
    res = 1
    for i in range(1, digit + 1):
        res = res * i
    # print(res)
    return res


def isStrong(n):
    temp = n
    sum = 0
    while n != 0:
        digit = n % 10
        sum = sum + fact(digit)
        n = n // 10

    # print(n)
    return sum == temp


print(isStrong(n))
