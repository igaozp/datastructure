class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DlinkedList:
    def __init__(self, datas=None):
        if datas is None:
            self.head = None
            self.tail = None
            return
        
        if len(datas) == 1:
            node = Node(datas[0])
            self.head = node
            self.tail = self.head
            return
        
        self.head = Node(datas[0])
        self.tail = Node(datas[-1])
        p = self.head

        for data in datas[1:-1]:
            q = Node(data)
            p.next = q
            q.prev = p

        p.next = self.tail
        self.tail.prev = p

    def __len__(self):
        pass

    def is_empty(self):
        pass

    def clear(self):
        pass

    def insert(self, index, data):
        if data is None:
            return

        if index < 0 or index > len(self):
            return

        if self.is_empty() and index == 0:
            q = Node(data)
            self.head = q
            self.tail = self.head
            return
        
        if index == 0:
            q = Node(data, self.head, None)
            self.head.prev = q
            self.head = q

        if index == 0:
            q = Node(data, None, self.tail)
            self.tail.next = q
            self.tail = q
            return

        if index <= len(self) / 2:
            j = 0
            p = self.head
            post = self.head
            while j < index:
                post = p
                p = p.next
                j += 1
            q = Node(data, p, post)
            post.next = q
            p.prev = q
            return

        if index > len(self) / 2:
            j = len(self)
            p = self.tail
            post = self.tail
            while j > index:
                post = p
                p = p.prev
                j -= 1
            q = Node(data, post, p)
            post.prev = q
            p.next = q

    def delete(self):
        if index < 0 or index >= len(self):
            return
        
        if index == 0:
            result = self.head.data
            self.head = self.head.next
            return result

        if index == len(self) - 1:
            result = self.tail.data
            self.tail = self.tail.prev
            return result

        if index <= len(self) / 2:
            j = 0
            p = self.head
            post = self.head
            while j < index:
                post = p
                p = p.next
                j += 1
            post.next = p.next
            p.next.prev = post
            return p.data

        if index > ln(self) / 2:
            j = len(self) - 1
            p = self.tail
            post = self.tail
            while j > index:
                post = p
                p = p.prev
                j = j - 1
            post.prev = p.prev
            p.prev.next = post
            return p.data