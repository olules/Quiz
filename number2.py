arr = [5,2,9,4,7]
    
temp=0

for i in range(0, len(arr)):
    print(arr[i], end=' ')
    
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            
print('Elements of array sorted in ascending order: ')
for i in range(0, len(arr)):
    print(arr[i], end=" ")
    
                