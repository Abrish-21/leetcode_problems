arr = [1, 2, 3, 4, 5]
index = 0
size = len(arr)
k = 2 # Remove every 2nd element

while size > 1:
    # Move to the k-th friend (1 step forward to count the 2nd element)
    index = (index + k-1)%size
    del arr[index]
    size -= 1  # Decrease the size of the array after deletion
    print(arr)
