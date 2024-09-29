'''def reverse(arr):
    return arr[::-1]
arr = [1,2,3,4,5]
print(reverse(arr))'''

def reverse(arr):
    
    n = len(arr)
    temp = [0]* n
    
    #copy to temp in reverse order
    for i in range(n):
        temp[i] = arr[n - i - 1]
        
    #overwrite temp to arr
    for i in range(n):
        arr[i] = temp[i]
        
    return arr
        
arrinput = input("Enter array values separted with space:")

arr = list(map(int,arrinput.split()))

print(reverse(arr))

