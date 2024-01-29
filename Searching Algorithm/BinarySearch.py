def BinarySeach(customList,value):
    l=0
    r=len(customList)-1
    while l<=r:
        m = (l+r)//2
        if value == customList[m]:
            return m
        elif value > customList[m]:
            l = m+1
        else:
            r=m-1
    return -1

cList = [1,2,3,4,5,6,7,8,9]
print(BinarySeach(cList,1))
# Binary Seach Time complexity:

# worst case : O(logn) best case: O(1)