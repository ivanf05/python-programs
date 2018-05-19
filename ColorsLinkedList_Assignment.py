#Ivan Fonseca
#Assignment 10
class Node:
    def __init__(self, info=None, next=None):#Default constructor 
        self.info = info
        self.next  = next

    def __str__(self):#String function
        return str(self.info)

node1 = Node (1)#sets node1 to 1
print ("\nnode1 is ", node1)

node2 = Node ("RED")#sets node2 "RED"
print ("\nnode2 is ", node2)



node1.next = node2 #Sets the next node of node1 linked list to RED 

node2.next = node1#Sets the nexts node of node2 linked list to 1

print ("\nnode1.next is ", node1.next)#prints both 


print ("\nnode2.next is ", node2.next)


node2.next = None#sets node2.next to null value and deletes 1.

def print_list(node):
    print ("\n< ", end=" ")
    while node:
        print (node, end=" ")
        node = node.next #prints linked list
           
    print (" >")
    return

node3 = Node("BLUE", node1)#appends "BLUE" to the beginning of the list(Node 1)

print_list(node3)#prints linked list. Node 3 with Node 1

print_list(node1)#prints linked list. Node 1

print_list(node2)#prints linked list. Node 2
