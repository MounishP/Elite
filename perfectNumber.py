# 6 --> 1,2,3 --> 1+2+3 = 6

"""
1. input
2. factor
3. sum of factors
4. compare
"""

n = int(input("Enter the number: "))


def isPerfect(n):                  #6
    sum = 0                        #0,1,3,6
    for i in range(1, n):          #1,2,3,4,5
        if n % i == 0:             #T,T,T,F,F
            sum = sum + i          #0+1 = 1,1+2=3,3+3=6
    return sum == n                #6==6 (True)


print(isPerfect(n))
