num=int(input("Enter a number:"))

temp=num
sum=0

while num!=0:
    sum=sum+(num%10)
    num=num//10

if temp%sum==0:
    print(f"{temp} is a harshad number")
else:
    print(f"{temp} is not a harshad number")