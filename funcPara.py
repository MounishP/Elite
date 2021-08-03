x = int(input("Enter the number: "))
y = int(input("Enter the number: "))
z = int(input("Enter the number: "))


def largest(x, y, z):
    max = x
    if max < y:
        max = y

    if max < z:
        max = z

    return max


print(largest(x, y, z))
