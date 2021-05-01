def average(array):
    distinct_array = list(set(array))
    return sum(distinct_array)/len(distinct_array)