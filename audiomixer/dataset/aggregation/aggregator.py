from abc import ABC, abstractclassmethod


# Abstract class that provides an interface for aggregators
class Aggregator(ABC):
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def aggregate(self, array):
        raise Exception("Aggregate method not implemented")
