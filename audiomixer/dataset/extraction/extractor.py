from abc import ABC, abstractclassmethod


# Base class for extractors
class Extractor(ABC):
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def extract(self, signal, sample_rate):
        raise Exception("Extract method not implemented")
