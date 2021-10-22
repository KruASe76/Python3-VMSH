def main(arg1, arg2):
    ans = []
    for i in range(len(arg1)):
        ans.append(arg1[i])
        ans.append(arg2[i])
    
    return ans


list1 = input().split()
list2 = input().split()

print(main(list1, list2))