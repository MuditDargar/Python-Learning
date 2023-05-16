s= "Mudit is the awesome  and the fabulous guy"

#WRITING TO A  FILE

#open the file with open and then write  "w"
# this is the first method
# with open("test.txt","w") as f :
#     f.write(s)

fp= open("test.txt","w")
fp.write(s)
fp.close()


#append mode
with open("test.txt","a") as f:
    f.write(". mudit need the G wagon 63 amg")

#READING A FILE
with open("test.txt","r") as f:
    s=f.read()
    print(s)