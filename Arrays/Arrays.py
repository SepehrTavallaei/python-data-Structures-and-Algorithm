#Arrays are not built in to the python so instead we use lists which they are more flexibl.
#we can use Arrays in python using Array module or NumPy Array module how ever there are some things that you need to consider before using this data type
# - Each element in Arrays has a unique index
# - Arrays can store data of specified type for example if an Array stores integers it can not stor strings or booleans
# -  Elements of an array are located in a contiguous (they located next to each other and there is no gap between them)

#why do we need arrays?
# lets assume that we want to store tree integers we can assign three variable to each one but what if we want to assign 500 numbers? well we use Arrays so essentially arrays are used to store a collection of data with the same type (usually with the same type).


#types of Array:
# there are two types of array depending on the number of dimenstion : 1) one dimesion 2) multi dymension
# we use indexes to access elements in one dimensional Arrays
# in two dimensional Array we use double indexes to access elements(basically two dimensional Array is a typical matrix)
#in three dimensional Array we can imagine a qube with numbers on it and it consists of multiple two dimensional arrays and ti access each element we use three indexes
#in real world we mostly use one and two dimensional Array

#two dimensional Arrays doesnt locate in memory like we imagine (a symple matrix) but they locate like a one dimensional Array.
#for example if our Array looks like this: 1  2  3 -
#                                          4  5  6 - => it will be like this in memory: 1  2  3  4  5  6  7  8  9
#                                          7  8  9 -                                   firstrow/secondrow/thirdrow
# and as the pattern goes on we show three dimensional Array like that

#creating Array using Array module in python: 
#first we import the built in module in python called Array and the way we specify the type of data that this Array is going to import is like this:
import array;
my_array = array.array('i') # this means that our array is going to store only intergers
array1 = array.array('i',[1,2,3,4]) # now in the second parameter of the array module we put the array, in this example I creat one dimensional array that store 4 contiguose block in the memory.
array1.insert(0,6)
#one of the benefits that array gives us is that it is more memory efficient than lists because it is limited to storing a sepecific data type but in the lists we store data types how ever we want and array is in the python standard library; no additional library that is outside of python is required to be download. the only limitation that it has is that it only basic data types this means that we can not creat our on custom data type and use it with array module

# the other code types that we can specify what type of data we wana use in array are:
# b - B - H - h - i l L q Q  => int / f , d => float

#the next module that we are ggoing to talk about is numpy.
#numpy is not a built in module in python so in orther to use it we have to pip3 install numpy it :
import numpy 
new_array = numpy.array([1,2,3,4])


#now lets talk about the time complexity of arrays: in both ways using array or numpy initialising and assigning a variuable is O(N) time complexity because its based on how many data we wana put in an array but importing both is O(1) time complexity.

#insertion to Array:
#to insert in an array there are three cases: 1) we wana insert an element at the begining of the array or in the middle or art the end the first two are time consuming. anyway now we wana show you how to do that:
np_array1 = numpy.array([1,2,3,4])
#np_array1.insert(0,6) 
# the first parameter is representing the index which we want to locate the element and the second is the value of an element which we wana put in the array

#Array tranversal:
#traversing an array means that visiting all the elemnt of an array for this use: we may want to print all the Array element or edit or add a feature to an array
# in this example you will see how to traverse an array:

def arr_traverser(array):
    for i in array: # o(n) time complexity
        print(i) # ----> o(1) time complexity and o(1) space complexity
arr_traverser(array1)

#traversing in two dimesional arrays:  
new_array2 = numpy.array([[1,2,3],[4,5,6]])
print(new_array2)

for i in range(len(new_array2)): #------> O(mn) time complexity and space c omplexity is O(1)
    for e in range(len(new_array2[0])): #------> O(n) time compelxity
        print(new_array2[i][e]) # ------> O(1) time and space complexity

#searching through the two dimensional array:

def search_array(array,value):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if value == array[i][j]:
                print(f'element found at the index of: [{i}] ,[{j}]')
            else:
                print(f'elemnt not found at the {i} row')
search_array(new_array2,6)


#Deletion arrays:

td_array = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(td_array)
newtd_array = numpy.delete(td_array,1,axis=0) # the second parameter is for culomns and the third parameter is for rows
print(newtd_array)