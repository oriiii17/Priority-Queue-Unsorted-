def add(self, data, priority):
    baru = Node(data, priority)
    if self.is_empty():
        self._head = baru
        self._tail = baru
    else:
    # kosong
    # insert belakang
        self._tail._next = baru
        self._tail = baru
    self._size = self._size + 1