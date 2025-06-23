from typing import Optional


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Optional["Node"] = None


class OneLinked:
    def __init__(self):
        self.head: Optional[Node] = None

    def create(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head: Optional[Node]) -> Optional[Node]:
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head: Node) -> Node:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result


def merge_two_sorted_lists(l1: OneLinked, l2: OneLinked) -> OneLinked:
    merged = OneLinked()
    merged.head = merge_sorted_nodes(l1.head, l2.head)
    return merged


def merge_sorted_nodes(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    if a is None:
        return b
    if b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = merge_sorted_nodes(a.next, b)
    else:
        result = b
        result.next = merge_sorted_nodes(a, b.next)
    return result


first_list = OneLinked()
for value in [5, 8, 2, 4]:
    first_list.create(value)

print("Original list:")
first_list.print_list()

first_list.reverse()
print("Reversed polarity:")
first_list.print_list()

first_list.sort()
print("Aftersort:")
first_list.print_list()


second_list = OneLinked()
for value in [7, 3, 6]:
    second_list.create(value)
second_list.sort()

print("Second sorted:")
second_list.print_list()


merged_list = merge_two_sorted_lists(first_list, second_list)
print("MergedSorted:")
merged_list.print_list()
