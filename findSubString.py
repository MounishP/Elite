s = "bob the builder"
sub = "bob"
print(s.split(" "))   # list

# if string is containing sub-string then print True or else False
#contains
#split it in to the list then compare

if sub in s:
    print(True)
else:
    print(False)