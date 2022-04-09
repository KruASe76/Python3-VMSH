def bin_search(l,x):
    left = 0
    right = len(l) - 1
    pos = -1
    while pos == -1 and (left<=right):
        mid = (right + left)//2
        if l[mid] == x:
            pos = mid
        elif l[mid]>x:
            right = mid -1
        else:
            left = mid + 1
    return pos

def lin_search(l,x):
    pos = -1
    for i in range(len(l)):
        if l[i] == x:
            pos = i
            break
    return pos

def merge(l,r):
    res = []
    i=0
    j=0

    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1

    res+=l[i:]
    res+=r[j:]

    return res

def merge_sort(arr):
    if len(arr)==1:
        return arr
    elif len(arr)>1:
        mid = len(arr)//2
        Left = arr[:mid]
        Right = arr[mid:]
        Left = merge_sort(Left)
        Right = merge_sort(Right)
        
        return merge(Left,Right)

