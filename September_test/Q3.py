n=int(input("Enter a number: "))

temp=n
length=0
sum=0
largest_digit=0
smalest_digit=9
reverse=0

while n!=0:
    r=n%10
    sum=sum+r
    reverse=reverse*10+r
    if largest_digit<r:
        largest_digit=r
    if smalest_digit>r:
        smalest_digit=r
    length+=1
    n=n//10

print(f"\nSum of digits: {sum}")
print(f"Number of digits: {length}")
print(f"Largest digit: {largest_digit}")
print(f"Smallest digit: {smalest_digit}")
if temp==reverse:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")