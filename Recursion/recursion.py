# a way of solving a problem by using a function calling itself
# its like : Performing the same operation multiple times with different inputs

# when to use / avoid recursion :
# in terms of time and space complexity iteration works better that recursion in comparison to recursion

# when to use recursion?
# - when we can easily break down a problem into similar subproblem
# - when we are fine with extra overhead (both time and space) that comes with it;
# - when we want a quick solution instead of efficient one;
# when traverse a tree recursion is very advisable
# when we use memoization in recursion

# when we should avoid recusion ?
# prety much all the reverse of all the reason's that indicate why we should use it we should do them in this case;

#Factorial :

def fact(n):
    assert n>=0 and int(n) == n, "the number must be positive integer only!"
    if n in [0,1]:
        return 1
    else :
        return n * fact(n-1)

# print(fact(10))



def fib(n):
    assert n>=0 and int(n)== n, "fibonancci number must be possitive and integer!"
    if n in [0,1]:
        return n
    else:
        return fib(n-1) + fib(n-2)

# print(fib(30))
 

def sum(n):
    assert n>=0 and int(n) == n, "the number must be integer positive only!"
    if n==0:
        return 0
    return n%10 + sum(int(n//10))

# print(sum(101))
def pow(x,n):
    assert int(n) == n, "the exponent must be integer number only"
    if n == 0:
        return 1
    elif n < 0:
        return 1/x*pow(x,n+1)
    while n!=0:
        return x * pow(x,n-1)

#print(pow(2,-2))

def decimalTbinary(x):
    assert int(x) == x, "the parameter must be integer only!"
    if x==0:
        return 0
    else:
        return x%2+10*decimalTbinary(int(x/2))

print(decimalTbinary(13.2))
