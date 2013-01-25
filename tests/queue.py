import unittest
from culebra.queue import Queue
import random
import os


class QueueTest(unittest.TestCase):
    def test_top_existing_file(self):
        name = 'test'
        path = 'files/test.clbr'
        queue = Queue(name, path)
        self.assertEqual('hola', queue.top())

    def test_top_new_file(self):
        name = 'test4'
        path = 'files/test4.clbr'
        queue = Queue(name, path)
        elems = ['hola', 'como', 'estas', 'ciao']
        for el in elems:
            queue.append(el)
        self.assertEqual('hola', queue.top())


    def test_bottom_existing_file(self):
        name = 'test'
        path = 'files/test.clbr'
        queue = Queue(name, path)
        self.assertEqual('ciao', queue.bottom())

    def test_bottom_new_file(self):
        name = 'test4'
        path = 'files/test4.clbr'
        queue = Queue(name, path)
        elems = ['hola', 'como', 'estas', 'ciao']
        for el in elems:
            queue.append(el)
        self.assertEqual('ciao', queue.bottom())


    def test_iter_existing_file(self):
        name = 'test'
        path = 'files/test.clbr'
        queue = Queue(name, path)
        elems = ['hola', 'como', 'estas', 'ciao']
        for a, b in zip(elems, queue):
            self.assertEqual(a, b)

    def test_iter_new_file(self):
        name = 'test4'
        path = 'files/test4.clbr'
        queue = Queue(name, path)
        elems = ['hola', 'como', 'estas', 'ciao']
        for el in elems:
            queue.append(el)
        for a, b in zip(elems, queue):
            self.assertEqual(a, b)

    def test_bottom_not_empty_new_file(self):
        name = 'test2'
        path = 'files/test2.clbr'
        queue = Queue(name, path)
        thing = str(random.random())
        queue.append(thing)
        self.assertNotEqual('', queue.bottom())
        self.assertNotEqual('\n', queue.bottom())


    def test_append_new_file(self):
        name = 'test3'
        path = 'files/test3.clbr'
        queue = Queue(name, path)
        thing = str(random.random())
        queue.append(thing)
        self.assertEqual(thing, queue.bottom())

    @classmethod
    def tearDownClass(cls):
        # Only the 'new' related files
        filenames = ['test2', 'test3', 'test4']
        ext = '.clbr'
        root = 'files'
        paths = [os.path.join(root, fn + ext) for fn in filenames]
        for p in paths:
            try:
                os.remove(p)
            except IOError:
                pass

if __name__ == '__main__':
    unittest.main()