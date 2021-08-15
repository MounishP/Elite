l = [1, 2, 4, 5, 6, 7, 8, 6, 4, 6]
n = int(input("Enter the number: "))


# find n in l --> true, false --->findElement(n,l)

def findElement(n, l):
    for i in l:
        if n == i:
            return True
    return False


print(findElement(n, l))
