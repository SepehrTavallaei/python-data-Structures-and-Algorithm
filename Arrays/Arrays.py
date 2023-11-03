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
print(array1)
#one of the benefits that array gives us is that it is more memory efficient than lists because it is limited to storing a sepecific data type but in the lists we store data types how ever we want and array is in the python standard library; no additional library that is outside of python is required to be download. the only limitation that it has is that it only basic data types this means that we can not creat our on custom data type and use it with array module
#the next module that we are ggoing to talk about is numpy.

#NUMPY => this library is not preinstalled with python standard library so we have to install it using command pip3 install numpy
