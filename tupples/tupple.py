#A tuple is an immutable (we can not change them) sequence of Python objects , Tuples are also comparable and hashable 

#hashable means that a value and its key stays the same during its life time
# atuple looks like this: 
new_tuple = 'a','b','c','d'
print(new_tuple)
# it is advisable to always indicate paranteces at the beggining and at the end of our values so it is easier to identify it's a tupple 
#if out tupple has only one value we must write it in this structure: 
new_tuple1 = ('a',) # if we don't indicate that "," at the end pythone thinks that we are creating a variable with "a" character inside of it;
print(new_tuple1) 
#an other way to creat tupple is like this:
a = tuple("absd")
print(a) # the result is : ('a', 'b', 's', 'd') so we now know that tuple function iterate through the string that we give it and put each character inside a distinguished place.
# Time complexity : 0(1)
# Space complexity : 0(n)

#tuples in memory:
#tuples are immutable it means that once we declare them we can not chnage them in any way;
#tuples uses the same way of saving data of arrays and lists and they store contigeously (no empty space between the values)
#to access tuple element we use braket operator and we use the indexing system for addressing the elements:
print(new_tuple[1], "second element of new tuple") # we can also put minus values as an index so it starts from backwards and find elements :
print(new_tuple[-1], "the second elements from last element")
# there is an other way to access elements in the tuples : and that is slice operator (:) : syntax: tuple [leftIndex: rightIndex] note that it doesnt give us the right index
print(new_tuple[:2], "prints from a to b and not c")    


#traversing through a tuple:
#the most trend way to loop through a tuple is via for loop:
for i in new_tuple:
    print(i)

# Time complexity : 0(n)
# Space complexity : 0(1)

#serach through tuple : 
# in operator: 
print('a' in new_tuple) # returms bool data type O(N) time complexity & O(1) space complexity
#index methode:
print(new_tuple.index('c')) # returns the index that the element is located in a tuple and if the element does not exist in the tuple it will raise an error;


def search_tuple(p_tuple, element):
    for i in range(0,len(p_tuple)):# -----> O(n) time complexity
        if p_tuple[i] == element:
            return f"the {element} is found at {i} index"
    return 'the element is not found'

print(search_tuple(new_tuple,'d'))

# Tuple operations & methode:
myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)
print(myTuple+myTuple1) # (1, 4, 3, 2, 5, 1, 2, 6, 9, 8, 7) using plus operator we can concatenate two diffrent tuples

#star operator:
print(myTuple* 4) # it will creat an other tuple and repeat each element 4 times: (1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5)

#count function: counts the number of times that al element is repeated: 
print((myTuple*4).count(1)) # returns 4 because element 1 is repeated 4 times 
# max methode returns the maximum value in a tuple :
print(max(myTuple))
#tuple methode convert lists to tuples:
print(tuple([1,23,45,6,2,8])) # (1, 23, 45, 6, 2, 8)

#tuple vs lists:
# the major diffrence between tuples and lists is that tuples are immutable but we can change the lists;
# we can delete elements in lists but not in the tuplse

# Methods that can be used for both lists and tuples:
# - count
# - index

# methods that only applies to lists : 1) append 2) insert 3) remove 4) pop 5) clear 6) sort 7) reverse

# - Tuples can be stored in Lists
# - Lists can be stored in Tuples

my_list = [1,2,3,(1,2,3,4)]
# del my_list[3][0] # TypeError: 'tuple' object doesn't support item deletion
print(my_list)

# - We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# - Iterating through a tuple is faster than with list
# - Tuples that contain immutable elements can be used as a key for a dictionary.
# - If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.


# Time and Space Complexity in Python Tuples
# Operation                 Time complexity         Space complexity           
#Creating a Tuple               o(1)                      O(n)
#Traversing a given Tuple       o(n)                      o(1)
#Accessing a given element      0(n)                      0(1) 
#Searching a given element      0(n)                      O(1)

