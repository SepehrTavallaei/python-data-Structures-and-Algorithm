from math import sqrt,ceil
# Diffrent types of sorting:
 #Based on space used Sorting categorise into two subcategory: 1) in pl ace 2) out of place
 #Based on Stability : it is categorized into two subcategory: 1) stable 2) unstable


# inplace sorting algoritm: it's a such sorting algoritm which doesnot reqire any extra space for sorting. example : Buble sort 

# outplace algoritms are such sorting algoritm which extra space is required in the memory.  example: merge sort
 
#stable sorting: If a sorting algorithm after sorting the contents does not change the sequence of similar content in which they appear, 
#                then this sorting is called stable sorting.for example we have two element in an array of numbers with the same value, 
#                in order for us to keep the sorted Array stable we have to sort them as the sequence of Arriving the first element that has the same value as other one
#                insertin sort is an example of a stable sorting algoritm.

# on the other hand if the sequence of repetitive elements change, it's unstable sorting algoritm. Example: Qick sort


# sorting terminology:

# increasing order: 
#  If successive element is greater than the previous one
# - Example: 1, 3, 5, 7, 9,11

#decreaing order:
# - If successive element is less than the previous one
# - Example: 11, 9, 7, 5, 3, 1

#Non increasing order:
# - If successive element is less than or equal to its previous element in the sequence.
# - Example: 11, 9, 7, 5, 5, 3, 1

# Non Decreasing Order
# - If successive element is greater than or equal to its previous element in the sequence
# - Example: 1, 3, 5, 7, 7, 9,

#sorting Algoritms:

    # Bubble sort
    # Selection sort
    # Insertion sort
    # Bucket sort
    # Merge sort
    # Quick sort
    # Heap sort

#Why do we need so many diffrent Sorting algoritms?
#   each of these Algoritms have their own pros and cons.
#   to select an algoritm wwe might consoder these tips as well:
#   - Stability
#    - Space efficient
#   - Time efficient


#Bubble sort:Bubble sort is also referred as Sinking sort 
# We repeatedly compare each pair of adjacent items and swap them if they are in the wrong order

def Buble_sort(custom_list): # O(n^2 time complexity) space complexity is O(1)
    for i in range(len(custom_list)-1 ):
        for j in range(len(custom_list)-i-1):
            if custom_list[j] > custom_list[j+1]:
                custom_list[j], custom_list[j+1] = custom_list[j+1],custom_list[j]
custom_list = [54,73,21,1,2,-30]
# print('befor: ',custom_list) 
# Buble_sort(custom_list)
# print(custom_list)

# selection Sort:
# In case of selection sort we repeatedly find the minimum element and move it to the sorted part of array to make unsorted part sorted. 
# we divide the array into two pice and we call them sorted Array and unsorted Array and then for the first time our sorted Array is empty because we havent done any sorting yet.
# we search for the minimum element in an array, once we find it we insert it to the sorted part of the Array, we repeat this proccess until all elements get into the sorted Array.
# selection sort performs well on small Arrays,no additional storage is needed beyond the Array it self. the main disadvatage of selection sort is that its very time consuming when we are dealing with huge Arrays.

def selectionSort(customList): # O(n^2) timecomplexity & spacexomplexity is o(1) because no additional space is required
    for i in range(len(customList)):
        minimumIndex = i
        for j in range(i+1,len(customList)):
            if customList[j] < customList[minimumIndex]:
                minimumIndex = j 
        customList[i],customList[minimumIndex] = customList[minimumIndex],customList[i]
    print(customList)

cList = [2,1, 7,6,5,3,4,9,81]
# selectionSort(cList)

# when we have insufficient memory & we want something easy to emplement we use selection sort, but we need to avoid this kind of sorting if time is a concern for us.


#insertion sort: 
# - Divide the given array into two part
# - Take first element from unsorted array and find its correct position in sorted array
# - Repeat until unsorted array is empty
# the main advatage of insrtion sort is space effiecieny.

def  insertionSort(customList): # O(n^2) time complexity and O(1) space complexity
    for i in range(1,len(customList)):
        key = customList[i]
        j = i-1
        while j >=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j-=1
        customList[j+1] = key
    return customList


#Bucket Sort:
    # - Create buckets and distribute elements of array into buckets
    # - Sort buckets individually
    # - Merge buckets after sorting
# now you may be curious how  many buckets should we creat? the answer is by using this formula we know how many buckets we need:
    # - Number of buckets = round(Sqrt(number of elements))
# imagine we have this list and we ant to sort it:  [2,1, 7,6,5,3,4,9,81]
    # the number of elements is 9 so according to this formula we need 3 buckets.

# an other question is that which element should get in which bucket? also we have a formula for that one! 
    # Appropriate bucket = ceil(Value * number of buckets / maxValue) (ceil function returns the ceil of the number if the number is not an integer number)
    # in the given list assume we want to insert element with the value of 5 in one of the buckets, according to the formula : ceil(5*3/9) = ceil(1.6) = 2
    # so the element goes to the secind bucket; we implement this process for any element in the Array and then we sort all of them using any aorting algoritm we desire, then merg them all together.

def bucketSort(customList):
    numberOfBuckets = round(sqrt(len(customList)))
    maxValue = max(customList)
    arr = [] 
    for i in range(numberOfBuckets):
        arr.append([])
    for j in customList:
        index_b = ceil(j*numberOfBuckets/maxValue)
        arr[index_b-1].append(j)
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k+=1
    return customList
cList = [2,1,7,6,5,3,4,9,8]
# print(bucketSort(cList))

#now we have used bucket sort to sort the elements in the buckets which take O(n^2) time complexity, but we can also implement it with quick sort which takes O(nlogn) time complexity ans its better than O(n^2)

# when to use bucket sort?
# we use nucket sort when input is uniformly distributed over range, it means that each element doesn't have a lot of diffrences like this list for instance: 1,2,4,91,93,95
# when to avoid Bucket Sort?
# when space is a concern


# Merg Sort:

# - Merge sort is a divide and conquer algorithm
# - Divide the input array in two halves and we keep halving recursively until they become too small that cannot be broken further
# - Merge halves by sorting them

def merg(customList,l,m,r):
    n1 = m - l+1
    n2 = r-m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0,n1):
        L[i] = customList[l+i] # why l+i why not only i from 0 to n1?!

    for j in range(0,n2):
        R[j] = customList[m+1+j]
    
    i = 0
    j = 0
    k = l
    while i < n1 and j<n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i+=1
        else:
            customList[k] = R[j]
            j+=1
        k+=1
    while i < n1:
        customList[k] = L[i]
        i +=1
        k +=1
    while j <n2:
        customList[k] = R[j]
        j+=1
        k+=1

def mergSort(customList,l,r): # space complexity O(n) & O(nlogn) time complexity
    if l <r:
        m = (l+r-1)//2
        mergSort(customList,l,m) # T(n/2) time complexity
        mergSort(customList,m+1,r)# T(n/2) time complexity
        merg(customList,l,m,r) # O(n) time complexity
    return customList

cList = [2,1,7,6,5,3,4,9,8]
# print(mergSort(cList,0,8))

# merge sort is better that other sorting algorithms because it performs faster than them, but it requires more space.

# When to use Merge Sort?
# - When you need stable sort
# - When average expected time is O(NIogN)
# When to avoid Merge Sort?
# - When space is a concern

# quick sort:
def swap(my_list,index1 , index2):
    my_list[index1],my_list[index2] = my_list[index2],my_list[index1]

def pivot(my_list,pivot_index,end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1,end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index +=1
            swap(my_list,swap_index,i)
    swap(my_list,pivot_index,swap_index)
    return swap_index

cList = [3,5,0,6,2,1,4]

def QuickSort(my_list,left,right): # O(nlogn) time complexity
    if left<right:
        pivet_index = pivot(my_list,left,right)
        QuickSort(my_list,left,pivet_index-1)
        QuickSort(my_list,pivet_index+1,right)
    return my_list

print(QuickSort(cList,0,6))
# Heap Sort:
# - Step 1 : Insert data to Binary Heap Tree
# - Step 2 : Extract data from Binary Heap
# - It is best suited with array, it does not work with Linked List

def heapify(customList,n,i):
    smallest = i
    l = 2*i+1
    r = 2*i+2
    if l<n and customList[l] < customList[smallest]:
        smallest = l
    if r<n and customList[r] < customList[smallest]:
        smallest = r
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest],customList[i]
        heapify(customList,n,smallest)

def heapSort(cusomList): # Time Complexity : O(NlogN) Space Complexity: O(1)
    n = len(cusomList)
    for i in range(int(n/2)-1,-1,-1):
        heapify(cusomList,n,i)

    for i in range(n-1,0,-1):
        cusomList[i],cusomList[0]=cusomList[0],cusomList[i]
        heapify(cusomList,i,0)
    

cList = [2,1,7,6,5,3,4,9,8]
heapSort(cList)
print(cList)