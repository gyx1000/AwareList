# -*- coding: utf-8 -*-

class AwareList(list):
    def __init__(self, *args, **kwargs):
        super(AwareList, self).__init__(*args, **kwargs)
        self.added = []
        self.removed = []

    def append(self, value):
        if value in self.removed:
            self.removed.remove(value)
        else:
            self.added.append(value)

        return super(AwareList, self).append(value)

    def remove(self, value):
        if value in self.added:
            self.added.remove(value)
        else:
            self.removed.append(value)

        return super(AwareList, self).remove(value)

    def insert(self, index, value):
        if value in self.removed:
            self.removed.remove(value)
        else:
            self.added.append(value)

        return super(AwareList, self).insert(index, value)

    def extend(self, ex_list):
        for en in ex_list:
            if en in self.removed:
                self.removed.remove(en)
            else:
                self.added.append(en)
        
        return super(AwareList, self).extend(ex_list)

    def pop(self, index=-1):
        value = super(AwareList, self).pop(index)
        if value in self.added:
            self.added.remove(value)
        else:
            self.removed.append(value)

        return value