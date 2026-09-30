unit=int(input("Enter units: "))

if unit<=100:
    bill=unit*5
    print(f"Electricity Bill: {bill}")
elif unit>100 and unit<=200:
    bill=100*5 + (unit-100)*7
    print(f"Electricity Bill: {bill}")
elif unit>200 and unit<=400:
    bill=100*5 + 100*7 + (unit-200)*10
    print(f"Electricity Bill: {bill}")
else :
    bill=100*5 + 100*7 + 200*10 + (unit-400)*12
    print(f"Electricity Bill: {bill}")