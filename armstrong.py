# 153 = 1^3+5^3+3^3
# 1634 = 1^4+6^4+3^4+4^4
# 3 = 3^1
# if the sum of digit of the number is raised to the length of the number and
#     equal to the number then it is an armstrong number
"""
1. length of the number
2. Separate the digit
3. cal power of digit raised by length
4. sum
5. compare
"""

n = int(input("Enter the number: "))


def length(n):
    count = 0
    while n != 0:
        count += 1
        n = n // 10

    return count


def isArmstrong(n):
    temp = n
    sum = 0
    l = length(n)
    while n != 0:
        digit = n % 10
        sum = sum + pow(digit, l)
        n = n // 10

    return sum == temp


print(isArmstrong(n))
