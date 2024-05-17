a=[1,3,5,7,2,4,6,8]
print("Array is",a)
n=len(a)
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("Sorted array is",a)
