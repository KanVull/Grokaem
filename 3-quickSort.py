def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pillar = arr.pop(len(arr) // 2)
        leftArr = []
        rightArr = []
        for elem in arr:
            if elem >= pillar:
                rightArr.append(elem)
            else:
                leftArr.append(elem)
        return quick_sort(leftArr) + [pillar] + quick_sort(rightArr)


if __name__ == '__main__':
    arr = [1,6,3,0,2,5,6,6,6,0,-4,1,10,8]
    print(quick_sort(arr))