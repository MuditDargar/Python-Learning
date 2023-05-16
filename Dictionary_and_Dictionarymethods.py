# a={}  #empty dictionary
# b=set() #empty set
# print(b,type(b))
# print(a,type(a))

dict1={"good" : "something pleasant ","fetch":"to bring",
     "1":"THe number 1"  }
print(dict1["good"])
print(dict1["1"])

#Q. you write the name than automatically print the marks
marks={"mudit":77 ,"rohit":45 ,"mohit":92 ,"yash":62}
# mean key se retrive kar sakhte ho data
# keys are mudit,rohit etc and data is 77,45 ...
print(marks["yash"])
print(marks["rohit"])
# print(marks["yash chopra"])  give this error....
#dictionary are mutable
marks["sachin"]=100 ;
print(marks)

#.get aapko error se baccha deta hai
print(marks.get("yash chopra"))
print(marks.get("yash"))

# to print the keys of the dictionary
print(dict1.keys())
print(marks.keys())

# to print the values in the dictionary
print(dict1.values())
print(marks.values())


# to print the tuples tuples
print(dict1.items())
print(marks.items())