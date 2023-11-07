#list is an orderd data type that holds an orderd collection of data types
#for accessing the elemnts in the lists we use indexes,  

#in operator: 
list1 = ['milk', 'butter', 'yogurt']
print('yogurt' in list1) # if it returns true it mean that the string milk is one of the elements of list1

#updating a list in python:
list1[2] = "bread" # now instead of yogurt we have bread;
print(list1)
print('yogurt' in list1) # and this should be false now
# space complexity and time complexity for updating a list is O(1)

#insertion to the lists:
# we have four ways to insert a list:
#1) insert an element to the first place of a list
#2) insert an element in any given index
#3) inserting an element to the end of the list
#4) insert a list to an other list
#List methods
#- insert() => insert to any given index
#- append() => insert to the end of an array
#- extend() => by usiinf extend method we can add another list to the other one!

#insert():
my_list = [1,2,3,4,5,6,7]
print(my_list)
my_list.insert(0,0) # => the first parameter always stands for index that we wana put the element to and the second parameter stands for the value of an element that we wana place;
# it also has O(n) time complexity and O(1) space complexity 
print(f'my list: {my_list}')

#append method:
my_list.append(8) # time and space complexity is O(1)
print(my_list) 

#exted method:
new_list = [9,10,11,12,13]
my_list.extend(new_list) # adds up new list to the end of my_list.
#o(n) time and space complexity

# slicing trough the list:

 # lets imaging that we have a list like this: 
my_list2 = ['a', 'b', 'c', 'd', 'e', 'f']
#if we want to select the first two element we do this:
print(my_list2[:2 ]) # basically the format that we slice a list is like: 
#start index:end index: step over
 # if we ommit the second part of the slicing it will start from the starting index(the one that you include) untill the end of your list 
 # if we want to delete and put an other element instead of deleted elements using list slicing we do this:
my_list2[0:2] = ['x','y'] 
print(my_list2)
#List methods for deletion
#- pop()
# we give this method an index of the element that we want to delete:
my_list2.pop(0) # note that if we didnt put any index the methode will delete the last element of the list
print(my_list2)
#- delete()
# we give it an index and it will take care of deleting that element it self:
del my_list[1] # => this will delete the second element of our list 
#- remove() # => it is very usefull when you want to remove an element it selfe and not knowing the index;
# 
# Linear search:
#  this kind of search is basically like this:
def linear_search(p_list, p_target):
    for i,value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(linear_search([1,2,3,4],4)) # which gives us 3 as the index of value 4
 # the space complexity of this operation is o(1) and the time complexity is O(n)


#list operations:
 # + operator : it concatenate the lists:
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) # it returns [1,2,3,4,5,6]
# * operator : repeats n times of each element that is in the list:
print(a*4) # like this : [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# len()
# this function returns the length of the list that we gave
#max() this function returns the biggest number in the list
# min this function is the oposite of max it returns the minimum or the lowest number of the list
# sum this function return the sumation of all the elements in the given list 

test_list = []
while(True):
    number = input('please enter a number: ')
    if number == "done":
        print(sum(test_list)/len(test_list))
        break
    else:
        test_list.append(int(number))
# list function : 
a = 'hello'
b = list(a) # this will iterate through all the characters of a variuable and as each character we have an element in the list


#split function :
# it is like list but it will only save the new element in the list if it sees a space in the string:
c = "hello hello hello"
d = c.split()
print(d)