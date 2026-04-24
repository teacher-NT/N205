import os
os.system("cls")

set1 = {'olma', 'anor', 'gilos', 'banan', 'uzum'}
set2 = {'qovun', 'tarvuz', 'uzum', 'banan', 'olma'}

# set3 = set1.intersection(set2)
# print(set3)

# set1.intersection_update(set2)
# print(set1)

# set3 = set1.difference(set2)
# set3 = set2.difference(set1)
# print(set3)

# set1.difference_update(set2)
# print(set1)

# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1.symmetric_difference_update(set2)
# print(set1)


set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {4,5,6}

print(set2.issubset(set1))
print(set1.issuperset(set2))
