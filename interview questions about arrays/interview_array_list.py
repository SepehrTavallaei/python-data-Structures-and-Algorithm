#number = input("enter a number: ")
#for i in range((abs(int(int(number)/2)))+1):
 #   print((i,int(number)-i))

# my_array = [0,5,4,7,10,15,14,3]

# def match_maker(list1,target):
#     for i in list1:
#         for j in list1:
#             if i + j == target:
#                 if(i !=j):
#                     print(i,j)

# match_maker(my_array,14)


def permutation_finder(list1, list2):
    if len(list1) == len(list2):
        s='these two lists are permutated'
        c=1
        for i in range(len(list1)):
            e1=list1[i]
            e2=list2[len(list2)-c]
            c+=1
            print(f'e1: {e1}')
            print(f'e2: {e2}')
            if(e1!=e2):
                s='these lists are not permutated.'
    print(s)

permutation_finder([1,2,3,4],[4,3 ,2,1])
            




