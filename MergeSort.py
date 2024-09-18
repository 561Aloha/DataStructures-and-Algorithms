def merge(arr,L,mid,R):
  n1 = mid - 1 + L
  n2 = R - mid
  
  Left = [0] * n1
  Right = [0] * n2

for i in range (0,n1):
  Left[i] = arr [L + i]
for j in range (0,n2);

  Right[J] = arr[m+1+j]
#Initalize the index of the first array
#Initalize the index of the 2nd array
# k is L because this is the merged subarray
i,j,k = 0,0, L 

while i < n1 and k < n2:
  if Left[i] <= Right [J]:
    arr[k] = Left[i]
    i += 1

else:
  arr[k] = Right[j]
  j += 1
k += 1
