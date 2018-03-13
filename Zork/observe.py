from abc import ABCMeta, abstractmethod

class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass

class Observable(object):

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def remove_all_observers(self):
        self.observers = []
