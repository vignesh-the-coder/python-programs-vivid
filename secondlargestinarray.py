n=int(input())
arr=[int(x) for x in input().split()]

def print2largest(arr,arr_size): 
    first = second = -2147483648
    for i in range(arr_size): 
                # first and second  
        if (arr[i] > first): 
          
            second = first 
            first = arr[i]  
        elif (arr[i] > second and arr[i] != first): 
            second = arr[i] 
    print(second)

  
print2largest(arr, n) 