#hash functions:

def mod(number,cellNumber):
    return number%cellNumber

#Ascii function:

def modASCII(string, cellNumber):
    total=0
    for i in string:
        total+=ord(i)
        return total%cellNumber

#properties of a good hash function:
    
    #- it destributes hash values uniformly across hash tables
    #- it has to use all the unout data(not just part of it)

# collision resulution techniques:
    # direct chaining: Implements the buckets as linked list. Colliding elements are stored in this lists
    # open Addressing: Colliding elements are stored in other vacant buckets. During storage and lookup these are found through so called probing.
        #linear probing: store's the colided element at the nearest vacant place of Array
        # quadratic probing: Adding arbitrary quadratic polynomial to the index until an empty cell is found
        # double Hashing:Interval between probes is computed by another hash function 

# hash Table is Full
    #to avoid this problem we can use direct chaining and this situation will never arise.
    # for open addressing technoque we create a 2x size hash table and restire all the elements again (it is not really effiecient because we have to call hash function again for all the data that we were storing in the orevious Array)

# pros and cons of collision resulution techniques:
    # Direct chaining:
    #   + hash table never get's full (the biggest advantage of Direct chaining)
    #   - Huge Linked List causes performance leaks (Time complexity for search operation becomes O(n).)
    #Open addressing:
    #   + easy implementation
    #   - When Hash Table is full, creation of new Hash table affects performance (Time complexity for search operation becomes O(n).)

# if the size of inputs is known we shall use Direct chaining
# if we tend to use deletion frequently we shall use Direct chaining


    