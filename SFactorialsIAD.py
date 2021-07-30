# 123 = 1!+2!+3! = 9
# 3! = 3*2*1 = 6  = 1*2*3
n = int(input("enter the value"))
sum = 0
# while n != 0:
#     digit = n % 10
#     digifact = 1
#     subdig = 1
#     while digit != 0:
#         digifact *= digit
#         digit -= 1
#         sum += digifact
#     n = n // 10
# print(digifact)

sum = 0


def fact(digit):                   #2
    res = 1                        #1
    for i in range(1, digit+1):    #1,2
        res = res * i              #1,2
    # print(res)
    return res                     #2


while n != 0:                    #123,12,1,0
    digit = n % 10               #3,2,1
    sum = sum + fact(digit)      # 0+6 = 6,6+2 = 8,8+1 = 9
    n = n // 10                  #12,1, 0

print(sum)                       # 9
