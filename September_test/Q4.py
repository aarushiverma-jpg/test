num1=int(input("Enter start: "))
num2=int(input("Enter end: "))

count=0
print("Prime numbers:")

for i in range (num1+1,num2):
    n=2
    while n<=i//2:
        if i%n==0:
            break
        n=n+1
    if n>i//2 and i>1:
        print(i,end=" ")
        count+=1
    
print(f"\nTotal prime numbers: {count}")