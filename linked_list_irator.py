class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index == 0:
            return self.head.val
        if index < 0 or index >= self.length:
            return -1
        elif index == self.length:
            return self.tail.val
        else:
            node = self.head
            c = 0
            while node is not None:
                if c == index:
                    return node.val
                node = node.next
                c += 1
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node_1 = Node(val)
        if self.head is None:
            self.head = node_1
        else:
            node_1.next = self.head
            self.head = node_1
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node_1 = Node(val)
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = node_1
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index == (self.length):
            self.addAtTail(val)
        else:
            c = 0
            prev = None
            node = self.head
            node_1 = Node(val)
            while c != index and node.next != None:
                prev = node
                node = node.next
                c += 1
            if c == index:
                prev.next = node_1
                node_1.next = node
                self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            cur_node = self.head.val
            new_head = self.head.next
            self.head = new_head
            self.length -= 1
            return cur_node
        else:
            node = self.head
            c = 0
            prev = None
            while c != index and node.next != None:
                prev = node
                node = node.next
                c += 1
            if c == index:
                prev.next = node.next
                self.length -= 1

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.val, end='')
            current_node = current_node.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next