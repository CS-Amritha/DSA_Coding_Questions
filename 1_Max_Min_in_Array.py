def findMaxMin(arr):    
    max_val = -float('inf')
    min_val = float('inf')
    
    for i in arr:
        if i > max_val:
            max_val = i
            
        if i < min_val:
            min_val = i
            
    print("max:",max_val)
    print("min:",min_val)    
    
arr1 = [3,5,4,1,9]
arr_input = int(input("Enter the values separated by spaces:"))
arr = list(map(int,arr_input.split()))
#arr_input.split()   Results in: ['3', '5', '4', '1', '9']
#map(int, ['3', '5', '4', '1', '9']) Results in: [3, 5, 4, 1, 9]
#The map() function returns an iterable (in this case, a map object), so you need to convert it into a list.
findMaxMin(arr)
 
