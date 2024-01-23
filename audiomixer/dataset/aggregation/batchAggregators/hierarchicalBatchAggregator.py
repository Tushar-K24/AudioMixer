from audiomixer.dataset.aggregation.batchAggregator import BatchAggregator


class HierarchicalBatchAggregator(BatchAggregator):
    def __init__(self):
        super().__init__()

    def aggregate(self, array):
        """
        Performs aggregation on 2d array

        :param array: (np.ndarray)

        :return: Dictionary with performed aggregations
        e.g.
            {
                "aggregator1": np.ndarray([1,2,3,...]),
                "aggregator2": np.ndarray([1,2,3,...]),
                ...
            }

        """
        aggregations = {}
        for aggregator in self.aggregators:
            aggregations[aggregator.name] = aggregator.aggregate(array)
        return aggregations
