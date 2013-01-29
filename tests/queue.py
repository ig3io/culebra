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

    def test_empty_top_new_file(self):
        queue = Queue('test', 'files/test5.clbr')
        self.assertEqual('', queue.top())

    def test_empty_bottom_new_file(self):
        queue = Queue('test', 'files/test6.clbr')
        self.assertEqual('', queue.bottom())

    def test_bottom_equals_top_empty_new_file(self):
        queue = Queue('test', 'files/test7.clbr')
        self.assertEqual(queue.bottom(), queue.top())

    def test_bottom_equals_top_new_file(self):
        queue = Queue('test', 'files/test8.clbr')
        thing = str(random.random())
        queue.append(thing)
        self.assertEqual(queue.bottom(), queue.top())

    def test_size_empty_new_file(self):
        q = Queue('test', 'files/test9.clbr')
        self.assertEqual(0, q.size())

    def test_size_existing_file(self):
        q = Queue('test', 'files/test.clbr')
        self.assertEqual(5, q.size())

    def test_size_new_file(self):
        q = Queue('test', 'files/test11.clbr')
        things = ['hola', 'como', 'estas', 'ciao']
        for t in things:
            q.append(t)
        self.assertEqual(5, q.size())

    def test_flush_new_file(self):
        q = Queue('test', 'files/test10.clbr')
        things = []
        for i in xrange(0, 5):
            things.append(str(random.random()))
        for t in things:
            q.append(t)
            self.assertEqual(t, q.bottom())
        # Refactor with size and stuff
        q.flush()
        self.assertEqual('', q.top())
        self.assertEqual('', q.bottom())
        self.assertEqual(0, q.size())

    def test_remove_has_effect(self):
        q = Queue('test', 'files/remove_has_effect.clbr')
        elements = ['hola', 'como', 'estas', 'loco']
        for e in elements:
            q.append(e)
        q.remove('como')
        for e in elements:
            if e == 'como':
                self.assertFalse(e in q)
            else:
                self.assertTrue(e in q)

    @classmethod
    def tearDownClass(cls):
        # Only the 'new' related files
        filenames = ['test2', 'test3', 'test4', 'test5', 'test6', 'test7',
                     'test8', 'test9', 'test10', 'test11', 'remove_has_effect']
        ext = '.clbr'
        root = 'files'
        paths = [os.path.join(root, fn + ext) for fn in filenames]
        for p in paths:
            try:
                os.remove(p)
            except (IOError, WindowsError):
                pass

if __name__ == '__main__':
    unittest.main()