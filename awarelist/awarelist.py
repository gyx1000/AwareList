# -*- coding: utf-8 -*-

class AwareList(list):
    def _removed(self, v):
        if v in self.added:
            self.added.remove(v)
        else:
            self.removed.append(v)

    def _added(self, v):
        if v in self.removed:
            self.removed.remove(v)
        else:
            self.added.append(v)

    def __init__(self, *args, **kwargs):
        super(AwareList, self).__init__(*args, **kwargs)
        self.added = []
        self.removed = []

    def append(self, value):
        self._added(value)

        return super(AwareList, self).append(value)

    def remove(self, value):
        self._removed(value)

        return super(AwareList, self).remove(value)

    def insert(self, index, value):
        self._added(value)

        return super(AwareList, self).insert(index, value)

    def extend(self, ex_list):
        for en in ex_list:
            self._added(en)
        
        return super(AwareList, self).extend(ex_list)

    def pop(self, index=-1):
        value = super(AwareList, self).pop(index)
        self._removed(value)

        return value

    def __delitem__(self, key):
        old_value = self.__getitem__(key)
        self._removed(old_value)

        super(AwareList, self).__delitem__(key)

    def __setitem__(self, key, value):
        old_value = self.__getitem__(key)
        self._removed(old_value)
        self._added(value)

        super(AwareList, self).__setitem__(key, value)

    def __setslice__(self, i, j, sequence):
        for v in self.__getslice__(i, j):
            self._removed(v)

        for v in sequence:
           self._added(v)

        super(AwareList, self).__setslice__(i, j, sequence)

    def __delslice__(self, i, j):
        for v in self.__getslice__(i, j):
            self._removed(v)

        super(AwareList, self).__delslice__(i, j)


    def __iadd__(self, other):
        super(AwareList, self).__iadd__(other)

        for v in other:
            self._added(v)

        return self
