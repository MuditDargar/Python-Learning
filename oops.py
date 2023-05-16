#basic example

# class Employee:
#     salary=90000 
#     name="sachin"
#     def getsalary(self):
#         return self.salary
    
# rohan =Employee()
# print(rohan.salary)
# print(rohan.name)

class student:
    def __init__ (self,name,roll_no):
        self.name= name
        self.roll_no =roll_no

    def getRoll_no(self):
        return self.roll_no
    
mudit=student("sachin","29")
# print(mudit.name)
# print(mudit.roll_no)
    
mudit=student("mudit","19")
# print(mudit.name)
# print(mudit.roll_no)
print(mudit.getRoll_no())