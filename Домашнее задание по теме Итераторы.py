class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        if self.start % 2 == 0:
            self.start -= 2
            return self
        else:
            self.start -= 1
            return self

    def __next__(self):
        self.start += 2
        if self.start >= self.end:
            raise StopIteration()
        else:
            return self.start


en = EvenNumbers(10, 25)
for i in en:
    print(i)

