# big o is a language we use to measure the efficency of an algoritm:
# big o will determine the efficency of code by timecomplexity(number of operations), space complexity
#we show the worst case senario (the one that is most time consuming) with big O and in the academics we cal big teta the middle one and the best with omega sign
# RUN TIME COMPLEXITIES:
#o(1): constant time  complexity this means that with any given input in the execution the value will never change.
# for example in this function no matter what do we give n as input the number
#of the operation will always be : 1: 
def multiply_numbers(n):
    return n*n
print (multiply_numbers(100)) # which gives us 10000 and no matter if we change the n only
# one operation is going to be executed;

# O(n):  it is called linear time complexity this means as the number of our inputs grow the number of the operations
#will also grow here is a good example:
def num_printer(n):
    for i in range(n):
        print(n)
num_printer(100) # if we give n the value 5 the number of the operations will be 5 but if we put a bigger number like 100 the number of the operations will be more obviously.
#O(n^2): squared  operations are not as efficient as the so called previous operation types and the appereance of 
#this type of the operations look like this:
def num_printer2(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k) # no matter how many times we increment the loops we still show them by O(n^2) and the
                # number of the operations will increas like this poatters: n*n*n*......the number of the loops
# droping the non dominant o(n) if we have a function like this:
def num_printer3(n):
    for i in range(n):
        for j in range(n):    
            print(i,j)
    for k in range(n):
        print(k) # in this case the number of the operation is equal to O(n^2 + n) which in Big O we ignore that and we simply call it: o(n^2)

#O(logn) : it is very efficient way of approaching an issue lets assume that we are searching a sorted list to find an element
# with O(n) time complexity approach we have to search through all the list 1 by 1 and if our element is located ay the end of the list
# we have to wait a long time! but if we devide the list by 2 and filter out the other list that doesn't have our element and then do the same pattern till we find our elemnet the time that takes the computer to find it will be so much less and efficient.


#Space Complexity:
#till now we only talked about time complexity but the time is not the only thing which matters to us, but the memory that the programme takes also matters

#diffrent terms for input space cpmplexity: 
def print_items(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
# in the above example we have O(a+b) time complexity not O(n), because a may not be equal to b;
def print_items2(a,b):
    for i in range(a):
        print(i)
        for j in range(b):
             print(j)
#for this one we do have O(a*b) time complexity;

#how to measur rime complexity of codes using Big O:
#rule no 1: any assignment or statement that are being executed once takes O(1)
# rule no 2: a simple for loop that starts from 0 to n takes o(n) time complexity
#rule no 3: nested loop of the same type takes quadratic time complexity o(n^2)
#rule no 4: a loop at which the controling parameter gets devided by 2 at each step takes O(log n)
#rule no 5: when dealing with diffrent statements just add them up
