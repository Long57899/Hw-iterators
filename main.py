class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list.copy
        self.current = 0
        self.item = []
        self.number_circle_1 = 0
        self.number_circle_2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.number_circle_1 < len(self.list):
            if self.current == 0:
                object_list = self.list[self.number_circle_1]
                self.number_circle_1 += 1
                self.current += 1
                if self.number_circle_2 < len(object_list):
                    while self.number_circle_2 < len(object_list):
                        self.item.append(object_list[self.number_circle_2])
                        self.number_circle_2 += 1

            else:
                self.number_circle_2 = 0
                self.current = 0


        return self.item
        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

#####################################################################################

def flat_generator(list_of_lists):
    current = 0
    circle_1 = 0
    circle_2 = 0
    result = []
    while circle_1 < len(list_of_lists):
        if current == 0:
            object_list = list_of_lists[circle_1]
            circle_1 +=1
            current +=1
            if circle_2 < len (object_list):
                while circle_2 <len(object_list):
                    result.append(object_list[circle_2])
                    circle_2 +=1
        else:
            circle_2 = 0
            current = 0
    yield result

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()