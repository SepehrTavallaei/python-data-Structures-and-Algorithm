# whats a liked list?
# Linked List is a form of a sequential collection and it does not have to be in order. 
#  A Linked list is made up of independent nodes that may contain any type of data and each node has a 
# reference to the next node in the link. 

# linked list vs array

#arrays have indexes but linked list does not
# in arrays elements are located contigiously but in linked list elements are not next to each other
# linked list has a head (the first element) and in the middle other elements but at the end we should have tail element
#elements in the linked lists are located in many diffrent memory sluts but at the end of each node (element) we have the next nodes location in the memory


# types of linked list:
# - Singly Linked List
    # the first element has the address of the second and the third has the address of second as we move on the tail has the address of one to the last (tail) element;
# - Circular Singly Linked List
    #it is like singly linked list but the one to the last (the one which comes before tail) has the address of the first element (the one which comes after the head element)
# - Doubly Linked List
    # the same as the singly linked list but it has two refrences at each elements (nodes that are in between the head and tail) and one of the refrences has the memory address of next note anf the other one has the previous nod's addres
# - Circular Doubly Linked List
    # its concatination of properties of circular linked list and doubly linked list and as we have refrences to next and previous element we can moe from last to first and vice versa!
    

# Node class:
#node is composed from value and pointer like : { "value": 10,"next":None}

class Node:
    def __init__(self,value): # space and time complexity is O(1)
        self.value = value
        self.next = None

new_node = Node(10)
# print(new_node) # location of node in the memory

# insetion to linked list in memory:
#1. at the beginning of the linked list : we remove the pointer of head to the previous forat element and poin it to the new node and the new node also points to the previous node
#2. in the middle of the linked  : we remove th pointer of the previous node to the next element and we instantioate a new node in a randomly place of memory and point it to the next element and the privous elemnt should also poin to the new element which we created but to get there (adding a new element and updating the refrences) first we have to travers through the head
#3. at the end of the linked list ; the same as the middle but we travers through the end of the linekd list

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def set_value(self,index, value):
        temp = self.get (index)
        if temp:
            temp.value = value
    
    def append(self,value): # in colnclusion : O(1) time complexity
        new_node = Node(value) # ----> O(1)
        if self.head == None: # ----> O(1)
            self.head = new_node# ----> O(1)
            self.tail = new_node# ----> O(1)
        else:
            self.tail.next = new_node# ----> O(1)
            self.tail = new_node# ----> O(1)
        self.length += 1# ----> O(1)
    def prepend(self,value):
        new_node= Node(value)
        if self.head == None:
            self.head = new_node# ----> O(1)
            self.tail = new_node# ----> O(1)
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    
    def insert(self,value,index):
        new_node= Node(value)
        if self.head == None:
            self.head = new_node# ----> O(1)
            self.tail = new_node# ----> O(1)
        elif index>0:
            temp_node = self.head
            for _ in range( index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length +=1
        else:
            new_node.next = self.head
            self.head = new_node
    
    def travers(self):
        current = self.head
        while current:# ----> O(n) time complexity
            print(current.value)
            current = current.next
    
    def search(self,value):
        current = self.head
        while current:
            if current.value == value:
                return 'yes'
            current = current.next
        return "no"
    
    def get(self,index):
        current = self.head
        if index<self.length:
            for _ in range(index):
                current = current.next
            return current
    def pop_first(self):
        if self.length == 1:
            self.head = None
            self.tail == None
            self.length = 0
        else: 
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -=1
        return temp
    def pop(self):
        temp = self.get(self.length-1)
        self.tail = temp
        temp.next = None
        self.length-=1
    def remove(self,index):
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        else:
            temp = self.get(index-1)
            popped_node = temp.next
            temp.next = popped_node.next
            popped_node.next = None
            self.length-=1
    def del_all(self):
        self.head = None
        self.tail = None

            
 

    
    

new_linked_list = LinkedList()
new_linked_list.insert(330,0)
new_linked_list.prepend(10)
new_linked_list.prepend(20)
new_linked_list.append(30)
new_linked_list.insert(330,2)
print(new_linked_list)
# new_linked_list.travers()
print(new_linked_list.search(30))
new_linked_list.set_value(2,20)
print(new_linked_list.get(2).value)
print(new_linked_list)
new_linked_list.pop_first()
print(new_linked_list)
new_linked_list.pop()
print(new_linked_list)
new_linked_list.remove(1)
print(new_linked_list)
new_linked_list.del_all()
print(f" new linked list : {new_linked_list}" )