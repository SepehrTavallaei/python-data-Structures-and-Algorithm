# Dictionaries are unordered collection of data which is indexed and changable;
# so how can we creat one? one way of creating one is lile this: 
my_dict = dict()
print(my_dict) # => the result is : {}
# the other way of creating dictionaries is this:
my_dict2 = {}
print(my_dict2) #=> the time and space complexity of both creating an empty dictionary by dict constructor or {} is O(1)
en_spa = dict(one="ono",two="das", three="tres") # the first param should not be in string but the second that is the value of the first param (key = "value") should be in '' or "";
print(en_spa)
# the equivalence of the above example using the other way if vreating dictioanries is this:
en_spa2 = {"one":"uno","two":'das',"three":'tres'}
print(en_spa2)
# note that if we are putting a vaue as a string we should put them in '' but if it is a number we must only put the number itself not in the quotation/double quotation sign;

# there is also an other way to creat a dictionary! using dict cunstructor associated with lists and tupple! this is an example of it:
en_spa3 = [('one','uno'),('two','das'),('three','tres')]
print(dict(en_spa3)) # {'one': 'uno', 'two': 'das', 'three': 'tres'} 
#note that the time and space complexity of creating dictionaries with n elements (n keys and n values) using these strategy is O(n);


# dictionaries in memory:
#python uses hash function to store and find your dictionary :
# A hash table is a way of doing key-value lookups. You store the values in an array, and then use a hash function to find the index of the array cell that corresponds to your key-value
# for example we give hash function the param 'one' and it calculates and gives us the index that the values and the key is located in the memory this way we can access our key and values in the memory that our dictionary is located in an array;
# but we may accure a problem in the ongoing proccess : look if we give the hash function and it calculate a code and based on that code we get an index that it was already occupied by an other element in the past? the best hash function is the one that avoid this thing but if some how it happends the system creats a linked list and put the new value at the end of the same index in memory!


# how we can update(re new an existing pair in the dictionary) , add a new element to a dictionary?

my_dict_human = {'name': 'sepehr','age':17}
my_dict_human['age'] = 18
print(my_dict_human) # this is how we update an element in dictionaries;
my_dict_human['address'] = "malayer" # this is how we add a new element that has not exist in the past;
print(my_dict_human)

#deleting an element from dictionary: 
#the first way is using del statement using the dictonary and the key:
del my_dict_human['name']
print(my_dict_human)

# the next way is using the pop method:

removed_value = my_dict_human.pop('age')
print(removed_value)
print(my_dict_human)

# the next way is popitem method and clear the clear method will delete all the keys&values from the dictionary and leave it empty;


mine = {'name' : 'sepehr', 'age': 18,'city':"tehran"} # time complexity is O(1) and space complexity is O(n)

def travers(dict):
    for key in dict: # time complexity is O(n) and space complexity is O(1)
        print(key ,dict[key]) # time complexity is O(1)

travers(mine)

# dictionary methodes:

# 1) clear methode : it removes all the keys and values from our dictionary; doesn't return any value and doesn't take any parameter;
# 2) copoy methode : it returns a shallow copy of the dictionaty which is called with and it doesn't get any parameter also, so the syntax of it looks like this:
mine2 = mine.copy()
print(mine2)
# 3) from keys method : it returns a copy of keys from a list and it also gets the values from user and the syntax of it looks like this: syntax: dictionary.fromkeys(sequence|],value)
new_dict = {}.fromkeys([1,2,3], 0)
print(new_dict)
# 4) get methode : it returns the asked value from the key that is provided in the parameter section and if the key was not there we can also add a new parameter as the default value the syntax looks like this: syntax: dictionary.get(key,value)
print(mine.get('age',25))
# 5) items: it will return a view of all the keys and values in a tupple : 
print(mine.items())
# 6) keys: it will return all keys in the given dictionary :
print(mine.keys())
# 7) setdefault methode: returns the value of key if key is in the dictionary if not it puts the default value which we give it ti the methode and the syntax is like this : syntax: dictionary.setdefault(key,default_value)
new_dict2 = {'name' : 'artin'}
print(new_dict2.setdefault('name1','abbas'))
print(new_dict2)
# 8) values methode : it returns a list of all values of th egiven dictionary :
print(mine.values())
# 9) update methode : it will update the key value with the new value that we provide it with. it will get a tupple or an array as param and travers through it and if there is a match of keys it only update the value else it will add the key and the value at the end of our dictionary;
new_dict3 = {'a':1,"b":2,'c':3,'age':19}
mine.update(new_dict3)
print(mine)


# list vs dictionary :
# dictionary        list
# unorderd          orderd
#access via keys    access via index
# collection of key value pairs  /   collection of elements
#no duplicate members   duplicate members are allowed


# dictionary comprehension :
# the structure of it looks like this : {new_key : new_value for item in list} here instead of lists we can write any iterables that we want
import random
my_names = ['abbas','sina', 'sepehr', 'artin','arta']
mine3 = {name : random.randint(1,10) for name in my_names}
print(mine3 )

# and we can move it one more step further and make a new dictionary based on an other dictionary : 
# new_dict = {new_key:new_value for (key,value) in dict.items()}

city = ['paris', 'london', 'new york', 'amsterdam', 'tokyo']
cities = {city: random.randint(20,30) for city in city}
print(cities)

above28 = {city:temp for (city,temp) in cities.items() if temp > 28}
print(above28)