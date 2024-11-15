list1 = (1,2,3,4,5,6)
list2 = (5,6,8,9,10,12)
list1 = set(list1)
list2 = set(list2)
abin_list = list1|list2
# print(list)
# list.add(6)
# list.remove(5)
print(abin_list)
intersection_list = list1 & list2
print (intersection_list)
symmetric_list = list1 ^ list2
print(symmetric_list)
print(type(list1))

