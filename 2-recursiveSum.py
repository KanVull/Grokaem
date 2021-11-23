def recursive_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursive_sum(arr[1:])    


def recursive_count_elem(arr):
    if arr:
        return 1 + recursive_count_elem(arr[1:])
    else:
        return 0    

def binary_search(arr, elem):
    def _binary_search(arr, left, right, elem):
        middle = (left + right) // 2
        if elem > arr[middle]:
            return _binary_search(arr, middle + 1, right, elem)
        elif elem < arr[middle]:
            return _binary_search(arr, left, middle - 1, elem)
        else:
            return middle

    return _binary_search(arr, 0, len(arr)-1, elem)                


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    print(recursive_sum(arr))
    print(recursive_count_elem(arr)) 
    print(binary_search(arr, 5))        