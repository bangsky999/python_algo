arr = [1,0,2,1,4,0,2,4]

counts = [0]*5 #[0000000000]
temp = [0]*len(arr)

for i in range(len(arr)):
    counts[arr[i]] += 1
    
for i in range(1,5):
    counts[i] += counts[i-1]

for i in range(len(arr)-1, -1, -1):
    counts[arr[i]] -= 1
    temp[counts[arr[i]]] = arr[i]
    
print(temp)

