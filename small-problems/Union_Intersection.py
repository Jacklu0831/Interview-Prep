"""

Get union and intersection of two linked lists

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    curr1 = llist_1.head
    curr2 = llist_2.head
    union = set()

    while curr1:
    	union.add(curr1.value)
    	curr1 = curr1.next
    while curr2:
    	union.add(curr2.value)
    	curr2 = curr2.next

    union_list = LinkedList()
    for item in union:
    	union_list.append(item)

    return union_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    curr1 = llist_1.head
    curr2 = llist_2.head
    set1 = set()
    set2 = set()

    while curr1:
    	set1.add(curr1.value)
    	curr1 = curr1.next
    while curr2:
    	set2.add(curr2.value)
    	curr2 = curr2.next

    intersection = set1.intersection(set2)

    inter_list = LinkedList()
    for item in intersection:
    	inter_list.append(item)

    return inter_list

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print()
print(union(linked_list_1,linked_list_2))
print()
print(intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print()
print(union(linked_list_3,linked_list_4))
print()
print(intersection(linked_list_3,linked_list_4))
