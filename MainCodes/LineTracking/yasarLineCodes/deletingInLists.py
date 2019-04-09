list1 = [11, 5, 17, 18, 23, 50]

# given index of elements
# removes 11, 18, 23
unwanted = [0, 3, 4]

for ele in sorted(unwanted, reverse=True):
    del list1[ele]

# printing modified list
print(list1)