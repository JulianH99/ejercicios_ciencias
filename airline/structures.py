class Node:
    def __init__(self, prev=None, next=None, id=None):
        """

        :param prev:
        :type prev: Node
        :param next:
        :type next: Node
        """
        self.prev = prev
        self.next = next
        self.id = id


class DoubleLinkedList:
    def __init__(self, head=None):
        """

        :param head:
        :type head: Node
        """
        self.head = head

    def append(self, node):
        """

        :param node:
        :type node: Node
        :return: node
        """
        if self.head is None:
            self.head = node
        else:
            self.head.next = node
            node.next = None
            node.prev = self.head

    def prepend(self, node):
        """

        :param node:
        :type node: Node
        :return:
        """
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node

            self.head = node

    def insert_after(self, prev_node, node):
        """

        :param prev_node:
        :type prev_node: Node
        :param node:
        :type node: Node
        :return:
        """
        node.next = prev_node.next
        prev_node.next = node
        node.prev = prev_node
        node.next.prev = node

    def search_node(self, id, node):
        """

        :param id:
        :type id: int
        :param node:
        :type node: Node
        """
        if node is None:
            return None
        elif node.id == id:
            return node
        return self.search_node(id, node.next)

    def remove(self, n_id, node):
        """
        Removes a node from the list
        :param n_id:
        :type n_id: str
        :param node:
        :type node: Node
        :return: None
        """

        if node is None:
            return None
        elif node.id == n_id:
            node.prev.next = node.next
            node.next.prev = node.prev
            return node
        return self.remove(n_id, node.next)

