import copy

li = [1, 2]
list1 = [1, 2, li]
list2 = copy.deepcopy(list1)
print(list2)
li.append(4)
print(list1)
print(list2)