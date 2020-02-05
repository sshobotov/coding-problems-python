import random


class RandomDict:
    # Thread unsafe implementation
    def __init__(self, randomizer = lambda size: random.randint(0, size - 1)):
        self.__index = []
        self.__index_size = 0
        self.__kv = {}
        self.__random = randomizer

    def put(self, key, value):
        stored_value = self.__kv.get(key)
        self.__kv[key] = (self.__index_size, value)

        if stored_value is None:
            self.__index.append((key, value))
            self.__index_size += 1
        else:
            (index, _) = stored_value
            self.__index[index] = (key, value)

    def get(self, key):
        stored_value = self.__kv.get(key)
        return stored_value[1] if stored_value is not None else None

    def remove(self, key):
        stored_value = self.__kv.pop(key, None)

        if stored_value is not None:
            (index, _) = stored_value
            self.__index_size -= 1

            if index != self.__index_size:
                (last_key, last_value) = self.__index[self.__index_size]
                self.__index[index] = (last_key, last_value)
                self.__kv[last_key] = (index, last_value)

            self.__index = self.__index[:self.__index_size]

    def get_random(self):
        if self.__index_size == 0:
            return None

        random_position = self.__random(self.__index_size)
        return self.__index[random_position][1]
