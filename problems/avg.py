num = input("Please Enter the numbers seperating with commas: ")
lst=num.split(",")
l=0
add=0
for i in lst:
    add+=float(i)
    l+=1

print(add/l)