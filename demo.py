# # 6 = 1 + 2 + 3 == 6
#
# sum = 0                                #0,1,3,6
# n = int(input("Enter the number: "))   #6
# for i in range(1, n):                  # 1,2,3,4,5
#     if n % i == 0:                     # 6%1==0, 6%2==0, 6%3==0
#         sum = sum + i                  #0+1=1, 1+2=3,3+3=6
#
#
# if n == sum:
#     print("It is a perfect number")
# else:
#     print("It is not a perfect number")
# swap --> a = 3, b = 4 ----> a = 4, b = 3

a = 3
b = 4
print("before swap a: ", a)
print("before swap b: ", b)

temp = b
b = a
a = temp

print("after swap a: ", a)
print("after swap b: ", b)
