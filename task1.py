""""Implementation of a singly linked list with various operations."""


class Node:
    """A class for a node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """A class for singly linked list with various operations."""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        """Insert a new node after the given prev_node."""
        if prev_node is None:
            print("Previous node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        """Delete the first occurrence of key in the linked list."""
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        """Search for an element in the linked list."""
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        """Print all elements in the linked list."""
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        """Reverse the linked list in place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        """Sort the linked list using insertion sort algorithm."""
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head
        while current:
            next_node = current.next

            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

            current = next_node

        self.head = sorted_head


def merge_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    """Merge two sorted linked lists into a single sorted linked list."""
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        if current1.data < current2.data:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        else:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next
    while current1:
        merged_list.insert_at_end(current1.data)
        current1 = current1.next
    while current2:
        merged_list.insert_at_end(current2.data)
        current2 = current2.next

    return merged_list


def main():
    """Main function to demonstrate linked list operations."""
    list1 = LinkedList()
    list2 = LinkedList()
    list1.insert_at_end(5)
    list1.insert_at_end(-10)
    list1.insert_at_end(151)
    list1.insert_at_end(32)
    print("List 1 before sorting:")
    list1.print_list()
    list1.insertion_sort()
    print("List 1 after sorting:")
    list1.print_list()

    print("List 2 before sorting:")
    list2.insert_at_end(222)
    list2.insert_at_end(12)
    list2.insert_at_end(-99)
    list2.insert_at_end(123)
    list2.print_list()
    list2.insertion_sort()
    print("List 2 after sorting:")
    list2.print_list()

    print("Merged sorted list:")
    merged_list = merge_lists(list1, list2)
    merged_list.print_list()


if __name__ == "__main__":
    main()
