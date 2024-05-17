n=int(input("enter the value: \n"))
for i in range(2,n):
    if(n%i==1):
        print(n,"is a prime number")
        break
    else:
        print(n,"is not a prime number")
        break
