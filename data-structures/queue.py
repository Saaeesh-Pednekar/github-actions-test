'''Module with queue implementation'''
from math import inf


class Queue:
    '''This is a custom queue implementation'''
    def __init__(self, max_size):
        self.max_size = max_size
        self.q1 = []
        self.q2 = []

    def enqueue(self, val):
        '''To add an item to the end of the queue'''
        if self.is_full():
            print('Queue is full. Cannot enqueue an element')
        else:
            self.q2.append(val)

    def dequeue(self):
        '''To remove an item from the front of the queue'''
        if self.is_empty():
            print('Queue is empty. Cannot dequeue an element')
        else:
            if not self.q1:
                while self.q2:
                    self.q1.append(self.q2.pop())
            print(self.q1.pop())

    def is_empty(self):
        '''To check whether the queue is empty or not'''
        return not self.q1 and not self.q2

    def is_full(self):
        '''To check whether the queue is full or not'''
        return len(self.q1) + len(self.q2) >= self.max_size

    def __str__(self):
        return f'{self.q1[::-1] + self.q2}'

    def __repr__(self):
        return f'Queue (queue={self.q1[::-1] + self.q2} max_size={self.max_size})'


queue_size = input('Enter the max size of queue(Leave default for dynamic size): ')
obj = Queue(int(queue_size) if queue_size != '' else inf)
print(obj)
print([obj])
print('------------------------------------ Queue Operations -------------------------------------')
while True:
    print('1. Enqueue\t 2. Dequeue\t 3. Is Empty\t 4. Is Full\t 5. Display Queue\t 6. Exit')
    choice = input('Enter the choice: ')

    match choice:
        case '1':
            ele = int(input('Enter the element to be pushed: '))
            obj.enqueue(ele)

        case '2':
            obj.dequeue()

        case '3':
            if obj.is_empty():
                print('Queue is empty')
            else:
                print('Queue is not empty')

        case '4':
            if obj.is_full():
                print('Queue is Full')
            else:
                print('Queue is not Full')

        case '5':
            print(obj)

        case '6':
            print('Exited')
            break

        case _:
            print('Invalid Choice')
