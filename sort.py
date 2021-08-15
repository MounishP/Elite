l = [1, 26, 4, 59, 0, 3, 68, 7, 8]
# str = "mounish"
# sort the list

#bubble sort algorithm

for i in range(0, len(l)):  # 0,1
    # n = l[i]  # 1
    for j in range(0, len(l)):  # 0,1,2
        if l[j] > l[i]:  # 1>1,1>0
            l[i], l[j] = l[j], l[i]

print(l)
