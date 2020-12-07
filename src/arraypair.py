def getPairsCount(arr, n, sum): 
      
    count = 0 # Initialize result 
  
    # Consider all possible pairs 
    # and check their sums 
    for i in range(0, n): 
        for j in range(i + 1, n): 
            if arr[i] + arr[j] == sum: 
                count += 1

    return count            

def getPairCount_Test(arr,n,sum):
    print("Test")
    if n < 2:
     return
    found = set()
    output = set()

    for num in arr:
        k = sum - num
        if k not in found:
            found.add(num)
        else:
            output.add(((min(k,num)),(max(k,sum))))
    
    print(output)

    



if __name__ == "__main__":    
    arr = [1, 5, 4,2,7, 5,0,6] 
    n = len(arr) 
    sum = 6
    print(n)
    getPairCount_Test(arr,n,sum)
    print("Count of pairs is",getPairsCount(arr, n, sum)) 