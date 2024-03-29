"""
    Search for element d in sorted but rotated array of size n
    Return index of elemnt or -1 if not found
    [70,71,99,2,12] d=1 => -1 | d=2 => 3 | d=12 => 4 | d=70 => 0 | d=75 => -1 | d=99 => 2 | d=101 => -1

    Binary Search
    - Check pivot value against leftmost/righmost indexs' value of subarray => sorted half of the array
    - ensure d >= min and d < max of the sorted half before looking in unsorted half of the array

    Time complexity - O(log(N))
    Space complexity - O(1)
"""
from array_rotation import rotateLeft

def sortedRotatedSearch(array, d):
    left = 0
    right = len(array)

    while right > left:
        mid = int(left + (right-left)/2)

        if array[mid] == d:
            return mid
        elif array[mid] > array[left] and d < array[mid] and d >= array[left]:
            right = mid
        else:
            left = mid+1
    
    return -1


if __name__ == "__main__":
    for i in [1, 2, 12, 70, 71, 75, 99, 101]:
        print("Index of {} is {}".format(i, sortedRotatedSearch(rotateLeft([2,12,70,71,99], 2), i)))