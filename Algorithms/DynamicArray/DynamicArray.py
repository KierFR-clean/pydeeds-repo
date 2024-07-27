
class DynamicArray:

    def __init__(self):
        self.capacity = 2
        self.array = [0] * 2
        self.length = 0

    def get(self, index):
        if index < self.length:
            return self.array[index]

    def full(self):
        return self.length == self.capacity

    #resizing an array by simply allocating it to temporary array and mutating it back
    def resize(self):
        self.capacity *= 2
        tempArr = [0] * self.capacity

        for i in range(self.length):
            tempArr[i] = self.array[i]

        self.array = tempArr

    def push(self, value):
        if self.full():
            self.resize()

        self.array[self.length] = value
        self.length += 1

    #removes an element by simply decrementing the length but not actually removing its reference to memory
    def pop(self):
        if self.length > 0:
            self.length -= 1

    # print the array along with proper formatting of commas
    def print(self):
        for i in range(self.length):
            if i < self.length - 1:
                print(self.array[i], end= ',')
            else:
                print(self.array[i])

    def insert(self, index, value):
        if index < self.length:
            self.array[index] = value
            return

dynamicArr = DynamicArray()
print('''
        ---------------------------------
        |   WELCOME TO JAVA             |
        |        ARRAY IMPLEMENTATION   |
        ---------------------------------
''')

dynamicArr.push(1)
dynamicArr.push(2)
dynamicArr.push(3)
dynamicArr.push(4)
dynamicArr.push(5)

dynamicArr.print()
print('')
print(dynamicArr.get(8))

dynamicArr.pop()
dynamicArr.print()
