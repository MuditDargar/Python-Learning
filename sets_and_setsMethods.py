# set written in  curly bras_ics
set_1={3,5,100,3,5,5,5}
set_2={3,100,12}

# set_1.clear()   #clear all the element from set_1
print(set_1) 
#print(set_1.pop()) #remove the random element from set
#set_1.add(250) #add the number in a set_1 at a random place
print(set_1.union(set_2)) #new set return karega naa ki set_1 ko modify karega

print(set_1.intersection(set_2)) # intersection apply and new set return 

print(set_1) 
print(set_2) 
#All rule are follow of set theory
print(type(set_1))