def collectList():
    list1 = [1, 2, 3, 4, 5]
    for li in list1:
        print(li, end=" ")

    print()

    # ιεΊιε
    list1.reverse()
    for e in list1:
        print(e, end=" ")

    print()

    for ee in reversed(list1):
        print(ee, end=" ")


class Demo03():
    def __init__(self, start):
        self.start = start

    def __reversed__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __iter__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


def iterZip():
    names = ["zx", "es", "hh"]
    ages = [20, 30, 40]
    for name, age in zip(names, ages):
        print(f"name=${name},age=${age}")


def keyValue():
    names = ["java", "python", "php", "go"]
    ages = [20, 30, 40, 50]
    for name, age in dict(zip(names, ages)):
        print("name=${name},age={age}")


# ----------------------------------------------
def testDemo03():
    for dd in Demo03(30):
        print(dd, end=" ")
    print()
    for res in reversed(Demo03(30)):
        print(res, end=" ")


if __name__ == '__main__':
    names = ["java", "python", "php", "go"]
    ages = [20, 30, 40, 50]
    for name, age in dict(zip(names, ages)):
        print("name=${name},age={age}")
