amount=int(input('enter the amount of meal :'))
tax = amount*18/100

tip = amount*18/100

gt=amount +tax+ tip
print(f"Your Bill:\nBase Amount: {round(amount, 2)}\ntax: {round(tax,2)}\ntip: {round(tip,2)}\nGrand Total: {round(gt,2)}\nThank you for visiting")
# print("tax :", tax)
# print("tip :" , tax )
# print(f" grand total amount is: {gt}")