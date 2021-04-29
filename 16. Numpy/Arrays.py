import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.flipud(numpy.array(arr, dtype=float))
    #OR
    #return numpy.array(arr[::-1], dtype=float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)