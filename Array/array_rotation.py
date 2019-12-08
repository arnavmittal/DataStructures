# Time complexity - O(N)
# Space complexity - O(1)

"""
    Rotate array of size n by d elements
    [1,2,3,4,5] rotate left by 2 => [3,4,5,1,2]

    1.  Break array into 2 parts A and B based on d elements, remaining n-d elements
        array = AB
    2.  Reverse entire array
        array = r(AB) = BrAr
    3.  Reverse B and A individually
        array = r(Br) r(Ar) = BA
"""

def rotateLeft(array, d):
    n = len(array)
    d = d%n

    for i in range(n/2):
        array[i], array[n-1-i] = array[n-1-i], array[i]
    
    for i in range((n-d)/2):
        array[i], array[n-1-d-i] = array[n-1-d-i], array[i]

    for i in range(d/2):
        array[n-d+i], array[n-1-i] = array[n-1-i], array[n-d+i]
    
    return array


def rotateRight(array, d):
    return rotateLeft(array, len(array)-d)    

if __name__ == "__main__":
    for i in range(7):
        print("Rotated left  by {} is {}".format(i, rotateLeft([1, 2, 3, 4, 5], i)))
        print("Rotated right by {} is {}\n".format(i, rotateRight([1, 2, 3, 4, 5], i)))