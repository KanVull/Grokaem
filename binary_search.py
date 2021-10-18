def binary_search(array, elem):
    '''
    array - iterable element
    elem - element searched in array 
    returns index of elem in array
    '''
    try:
        left_edge = 0
        right_edge = len(array) - 1
    except Exception as e:
        print(e)   
        return None 

    while left_edge <= right_edge:
        middle = (left_edge + right_edge) // 2
        if array[middle] == elem:
            return middle
        elif array[middle] > elem:
            right_edge = middle - 1
        else:
            left_edge = middle + 1

    return None

if __name__ == '__main__':
    array = list(range(100))
    print(binary_search(array, 401))

    array = ['Иванов', 'Смирнов', 'Кузнецов', 'Васильев', 'Петров', 'Соколов', 'Михайлов']
    array.sort()
    print(array)
    print(binary_search(array, 'Петров'))
                        