class SinglyListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self, iterator):
        nodes = [SinglyListNode(i) for i in iterator]
        current_node = nodes[0]
        self.head = current_node
        i = 1
        while current_node != None and len(nodes) != i:
            current_node.next = nodes[i]
            current_node = current_node.next
            i += 1
        self.tail = current_node