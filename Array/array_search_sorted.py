"""
    Search for element d in sorted array of size n
    Return index of elemnt or -1 if not found
    [2,12,70,71,99] d=1 => -1 | d=2 => 0 | d=70 => 2 | d=75 => -1 | d=99 => 4 | d=101 => -1

    Binary Search
    
    Time complexity - O(log(N))
    Space complexity - O(1)
"""

def sortedSearch(array, d):
    left = 0
    right = len(array)

    while right > left:
        mid = int(left + (right-left)/2)

        if array[mid] == d:
            return mid
        elif d > array[mid]:
            left = mid+1
        else:
            right = mid
    
    return -1


if __name__ == "__main__":
    for i in [1, 2, 12, 70, 71, 75, 99, 101]:
        print("Index of {} is {}".format(i, sortedSearch([2,12,70,71,99], i)))