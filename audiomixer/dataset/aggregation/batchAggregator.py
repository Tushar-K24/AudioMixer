from abc import ABC, abstractclassmethod

from audiomixer.dataset.aggregation.aggregator import Aggregator


class BatchAggregator(ABC):
    """
    BatchAggregator is an abstract class that provides an interface
    to apply multiple aggregations on 2D numpy arrays
    """

    def __init__(self):
        self.aggregators = []

    def add_aggregator(self, aggregator):
        """
        Adds an Aggregator to the aggregators.

        :param aggregator: (Aggregator) Aggregator (e.g., MeanAggregator)
        """
        assert isinstance(aggregator, Aggregator)
        self.aggregators.append(aggregator)

    @abstractclassmethod
    def aggregate(self, array):
        raise Exception("Batch Aggregate method not implemented")
