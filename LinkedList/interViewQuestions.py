from linkedlist import LinkedList

def sumList(LLA, LLB):
    n1 = LLA.head
    n2 = LLB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result%10))
        carry = result / 10
    return ll

LLA = LinkedList()
LLA.add(7)
LLA.add(1)
LLA.add(6)

LLB = LinkedList()
LLB.add(5)
LLB.add(9)
LLB.add(2)
print(LLA)
print(LLB)
print(sumList(LLA,LLB))