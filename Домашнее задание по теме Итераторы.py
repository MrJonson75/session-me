class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.step = 0

    def __iter__(self):
        self.step = self.start - 1
        return self

    def __next__(self):
        self.step +=1
        if self.step > self.start:
            if self.step >= self.end:
                raise StopIteration()
        if self.step % 2 == 0:
            return self.step
        else:
            self.step +=1
            return self.step





en = EvenNumbers(10, 25)
for i in en:
    print(i)
