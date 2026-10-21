print("The prime Numbers Between 1 to 100 are:")

for n in range(1,101):
    i=2
    while i<=n//2:
        if n%i==0:
            break
        i+=1
    if i>n//2 and n>1:
        print(n,end=" ")

