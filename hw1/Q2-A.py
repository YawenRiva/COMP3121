# use forloop to make sure that every element in the array S
# is tested till the last one or the Diff has been found
# array S got n elements and X is the given integer
for (i=0; i<n; i++) in array S
    Difference = (X - array[i])
    # low is the first index, and high is the index of last element
    FindDifference(array, low, high, Difference)
        if high >= 1
            mid = (high + low)/2
            if array[mid] == Difference
                return True
            elif array[mid] > Difference
                return FindDifference(array,low,mid-1,Difference) 
            elif array[mid] < Difference
                return FindDifference(array,mid+1,high,Difference)
        else
            return False


            
