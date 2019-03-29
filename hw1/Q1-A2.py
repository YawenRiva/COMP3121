# Find the INDEX of LAST element that is euqlas or smaller than Rk
# the array is SORTED
# now, low is the index of the first element in the array, and high is the index of the last
FindRight (array, low, high, Rk) 
    // if the first element is greater than Rk, then no solution
    if array[low] > Rk
        then no such a exist in the range [Lk,Rk]
    # set mid for binary search
    mid = (low + high)/2
    if (array[mid] < Rk) 
        if (array[mid+1] > Rk)
            return mid
        else
            FindRight(array, mid, high, Rk)
    elif (array[mid] > Rk)
        if (array[mid-1] <= Rk)
            return mid-1
        else
            FindRight(array, low, mid, Rk)
    elif (array[mid] == Rk)
        if (array[mid-1] != Rk)
            return mid
        else
            FindRight(array, low, mid, Rk)


CountElements (LeftIndex, RightIndex)
    # because Lk<=Rk
    # if they are the same then theres only one element is in the range [Lk,Rk]
    if (LeftIndex == RightIndex)
        Count = 1
    else
        Count = RightIndex - LeftIndex + 1
    return Count

