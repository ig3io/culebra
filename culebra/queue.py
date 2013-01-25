class Queue(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.file = None
        self._dof(self._init, 'a')

    def size(self):
        return self._dof(self._size)

    def top(self):
        return self._dof(self._top)

    def bottom(self):
        return self._dof(self._bottom)

    def append(self, elem):
        return self._dof(self._append, 'a', str(elem))

    def flush(self):
        self._dof(self._init, 'w')

    def __iter__(self):
        self._openf()
        for line in self.file.readlines():
            yield line.strip()
        self._closef()

    def _dof(self, func, mode='r', *args):
        self._openf(mode)
        result = func(*args)
        self._closef()
        return result

    def _init(self):
        return None

    def _size(self):
        return len(self.file.readline())

    def _top(self):
        return self.file.readline().strip()

    def _bottom(self):
        lines = self.file.readlines()
        if not lines:
            return ''
        else:
            return lines[-1].strip()

    def _append(self, text):
        return self.file.write(text + '\n')

    def _openf(self, mode='r'):
        self.file = open(self.path, mode)

    def _closef(self):
        self.file.close()

    def __repr__(self):
        return "<Queue({0}, {1})>".format(self.name, self.path)

    def __str__(self):
        return repr(self)