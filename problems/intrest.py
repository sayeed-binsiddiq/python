amount = float(input("enter the deposite amount: "))
intrst1 = amount + amount*4/100
intrst2 = intrst1 + intrst1*4/100
intrst3 = intrst2 + intrst2*4/100
print(f"amount after one year: {round(intrst1,2)}\n amount after two year: {round(intrst2,2)} \n amount after three year: {round(intrst3,2)}")