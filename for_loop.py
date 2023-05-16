# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

for i in range(5):
    if(i==3):
        break ;
    print(i+1)


for i in range(5):
    if(i==3):
        continue;
    print(i+1)


#printing the list
print("printing the list")
a=[1,34,33,22,666]
for item in a :
    print(item)

#printing  the set
print("printing the set")
set={1,23,44,3333,222} # the value of set not print in the order
for item in set:
    print(item)