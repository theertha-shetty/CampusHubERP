class NumberIterator:

    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration

        value = self.numbers[self.index]
        self.index += 1
        return value


def number_generator(numbers):
    for number in numbers:
        yield number


def student_id_generator(start, count):
    for number in range(start, start + count):
        yield f"ST{number}"


def even_number_generator(limit):
    for number in range(2, limit + 1, 2):
        yield number