lis=[12, 45, 7, 45, 30, 22, 30]

s=set(lis)

max=0
max2=0

for num in s:
    if num>max:
        max2=max
        max=num
    elif max2<num<max:
        max2=num

print(f"Second maximum element is {max2}")