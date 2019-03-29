# Find the INDEX of FIRST element that is euqlas or greater than Lk
# the array is SORTED# now, low is the index of the first element in the array, and high is the index of the last
FindLeft(array, Low, High, Lk)
    # If the FIRST element is greater and equals to Lk
    if (array[low] >= Lk) 
        then return 'low'
    # If the LAST element is smaller than Lk then theres no a exist in the range
    elif (array[high] <= Lk)
        then theres no such a exist in the range [Lk,Rk]

# based on binary search, repeatedly dividing the search interval in half
# and ignore half of the element after one comparison
    mid = (low + high)/2
    # start to compare the Lk to array[mid]
    if array[mid] > Lk
        then ignore the right part and keep searching the left side
        FindLeft(array, Low, Mid, Lk)
    elif array[mid] == Lk
        if array[mid-1] < Lk
            return mid
        else
            FindLeft(array, Low, mid, Lk)
    elif array[mid] < Lk
        if array [mid+1] >= Lk
            return mid+1
        else
            FindLeft(array, mid, high, Lk)

        

        
