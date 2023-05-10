# bucket (ведро, лист) - цепочка записей, при коллизии
class Node:
    def __init__(self, key, value, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, _capacity, debug=False) -> None:
        self.__size = 0
        self.__taken = 0
        self.__capacity = _capacity
        self.__buckets = [None] * self.__capacity
        self.debug = debug

    # 2.1
    def __setitem__(self, key, value) -> None:

        self.rehash()

        self.__size += 1
        index = hash(key) % self.__capacity

        if self.debug:
            print(f"for {key} index is {index}")

        node: Node = self.__buckets[index]
        # No collision: put in empty bucket
        if node is None:
            self.__buckets[index] = Node(key, value)
            self.__taken += 1
            return

        # Collision: iterate bucket
        else:
            prev = node
            while node is not None:
                if node.key == key:
                    node.value = value
                    return
                prev = node
                node = node.next
            prev.next = Node(key, value)

    # 2.1
    def __getitem__(self, key):
        index = hash(key) % self.__capacity
        node: Node = self.__buckets[index]
        # Iterate bucket until key is found
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        return node.value

    # 2.1
    def __len__(self):
        return self.__size

    # 2.2
    def __str__(self):
        pairs = list()
        for bucket in self.__buckets:
            node = bucket
            while node is not None:
                k = node.key
                v = node.value
                k = f"\'{k}\'" if type(k) is str else k
                v = f"\'{v}\'" if type(v) is str else v
                pairs.append(f"{k}: {v}")
                node = node.next
        return f"\u007b{', '.join(pairs)}\u007d"
    # 2.3
    def __iter__(self):
        self.index = 0
        self.node = self.__buckets[self.index]
        return self

    # 2.3
    def __next__(self):
        while self.node is None:
            self.index += 1
            if self.index >= self.__capacity:
                raise StopIteration
            self.node = self.__buckets[self.index]

        # Получаем пару и переходим к след узлу
        k, v = self.node.key, self.node.value
        self.node = self.node.next
        return k, v

    def rehash(self):
        if self.__taken / self.__capacity < 0.5:
            return

        newHashTable = HashTable(2 * self.__capacity, self.debug)

        for key, val in self:
            newHashTable[key] = val
        self = newHashTable



def test():
    table = HashTable(2)
    table["aidar"] = 5
    table["NeAidar"] = 4
    table["VSE_TAKIAIDAR"] = 4
    table["VSE_TAKINE"] = 5
    table[123] = "= 100+20+3"
    print(table)

test()