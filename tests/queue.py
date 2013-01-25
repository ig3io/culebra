import unittest
from culebra.queue import Queue
import random


class QueueTest(unittest.TestCase):
    def test_queue_existing_file_top(self):
        name = 'test'
        path = 'C:/Users/Ignacio/Desktop/test.clbr'
        queue = Queue(name, path)
        self.assertEqual('hola', queue.top())

    def test_queue_existing_file_bottom(self):
        name = 'test'
        path = 'C:/Users/Ignacio/Desktop/test.clbr'
        queue = Queue(name, path)
        self.assertEqual('ciao', queue.bottom())

    def test_queue_existing_file_iter(self):
        name = 'test'
        path = 'files/test.clbr'
        queue = Queue(name, path)
        elems = ['hola', 'como', 'estas', 'ciao']
        for a, b in zip(elems, queue):
            self.assertEqual(a, b)

    def test_queue_append_new_file(self):
        name = 'test2'
        path = 'files/test2.clbr'
        queue = Queue(name, path)
        thing = str(random.random())
        queue.append(thing)
        self.assertEqual(thing, queue.bottom())


if __name__ == '__main__':
    unittest.main()