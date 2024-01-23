import numpy as np
from audiomixer.dataset.aggregation.aggregator import Aggregator


class MeanAggregator(Aggregator):
    def __init__(self, aggregation_axis):
        super().__init__("mean")
        self.aggregation_axis = aggregation_axis

    def aggregate(self, array):
        """
        Mean aggregator across given axis

        :param array: (np.ndarray)

        :return: (np.ndarray) aggregated array
        """
        return np.mean(array, axis=self.aggregation_axis)
