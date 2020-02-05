address_space = []


def _get_pointer(value):
    if value not in address_space:
        address_space.append(value)

    return address_space.index(value)


def _dereference_pointer(ptr):
    return address_space[ptr]


class _Node:
    __termination_address = -1

    def __init__(self, value, prev_node=None, next_node=None):
        self.__both = (self.__termination_address if prev_node is None else _get_pointer(prev_node)) ^ \
                      (self.__termination_address if next_node is None else _get_pointer(next_node))
        self.value = value

    def get_prev(self, next_node):
        address = self.__both ^ (self.__termination_address if next_node is None else _get_pointer(next_node))
        return None if address == self.__termination_address else _dereference_pointer(address)

    def get_next(self, prev_node):
        address = self.__both ^ (self.__termination_address if prev_node is None else _get_pointer(prev_node))
        return None if address == self.__termination_address else _dereference_pointer(address)

    def append_element(self, value):
        last_prev_address = self.__both ^ _Node.__termination_address
        if last_prev_address < -1:  # -1 if this was very first node in the list both=0 (-1 ^ -1)
            raise Exception("Operation applicable only to node without next sibling")

        new_node = _Node(value, self)
        self.__both = last_prev_address ^ _get_pointer(new_node)

        return new_node


class XorLinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def add(self, element):
        if self.last_node is None:
            address = _get_pointer(_Node(element))

            self.first_node = address
            self.last_node = address
        else:
            node = _dereference_pointer(self.last_node).append_element(element)
            self.last_node = _get_pointer(node)

    def get(self, index):
        current_index = 0
        current_node = None if self.first_node is None else _dereference_pointer(self.first_node)
        prev_node = None

        while current_node is not None:
            next_node = current_node.get_next(prev_node)
            current_index += 1

            if current_index == index:
                return None if next_node is None else next_node.value
            else:
                prev_node = current_node
                current_node = next_node

        return None
