list_1=[3,55,44,22,"mudit",44,453]
print(type(list_1))
print(list_1)
l_1=[2,54,34,23,65,45,55,77]
#you cannot change the string
#string are immutable and  non- modify_able
#but you manipulate the list
#list is mutable
list_1.remove(22)
print(list_1)
print(list_1.count(44))
l_1.sort() # for sorting the  list
l_1.pop() #for pop the last element the list
l_1.append(20) # for adding the new number on last position
# l_1.clear() # to remove the all element in the from list
l_1.extend([45,33,2,121])
print(l_1) 

p =l_1.index(45)# to show the index number
print(p)
print(l_1[2:4]) # slicing of the list
# and more many methods in list 