class Stack():

    def __init__(self):
        self.data = []

    def pop(self):

        self.data.remove([-1])

        return

    def push(self):

        self.data.append([-1])

        return

    def read(self):

        return self.data[-1]


class Queue():

    def __init__(self):

        self.data = []

    def enqueue(self):

        self.data.append([-1])

        return

    def dequeue(self):

        self.data.remove([0])

        return

    def read(self):

        return self.data[0]






