age=int(input("enter of the human age"))
dog_age=0
if age>=2:
    dog_age=2*10.5 + (age-2) * 4
else:
    dog_age=age*10.5

print(dog_age)