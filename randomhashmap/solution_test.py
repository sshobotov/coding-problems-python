import unittest
from .solution import RandomDict


class MyTestCase(unittest.TestCase):
    def test_basic_functionality(self):
        instance = RandomDict()

        instance.put("test", 1)
        self.assertEqual(1, instance.get("test"))
        self.assertEqual(1, instance.get_random())
        instance.remove("test")
        self.assertIsNone(instance.get("test"))
        self.assertIsNone(instance.get_random())

    def test_get_random(self):
        instance = RandomDict(lambda size: 0)

        instance.put("one", 1)
        instance.put("two", 2)
        self.assertEqual(1, instance.get_random())
        self.assertEqual(1, instance.get_random())

        instance = RandomDict(lambda size: 1)

        instance.put("one", 1)
        instance.put("two", 2)
        self.assertEqual(2, instance.get_random())
        self.assertEqual(2, instance.get_random())

        self.__count = 0

        def inc_count():
            self.__count += 1
            return self.__count
        instance = RandomDict(lambda size: inc_count() % 2)

        instance.put("one", 1)
        instance.put("two", 2)
        self.assertEqual(2, instance.get_random())
        self.assertEqual(1, instance.get_random())


if __name__ == '__main__':
    unittest.main()
