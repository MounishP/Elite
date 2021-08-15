s = "malayalam"

# op: maly , remove the repeated characters, no predefined methods
res = ""
# for i in range(0, len(s)-1):
#     flag = False
#     for j in range(i+1, len(s)):
#         if flag == False and s[i] != s[j]:
#             res += s[j]

for i in range(0, len(s)):
    if s[i] in res:
        continue
    else:
        res += s[i]



print(res)
