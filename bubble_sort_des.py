def bubble(arr):
    n = len(arr)
    for i in range(n):
      for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j+1],arr[j]=arr[j],arr[j+1]
        
arr=[1,9,5,4,88,55,21,14,16,33,29,11,9]
bubble(arr)
for x in arr:
    print(x,end=" ")

    #O(n)-best case O(n^2)-worst case  O(1)-time complexity
