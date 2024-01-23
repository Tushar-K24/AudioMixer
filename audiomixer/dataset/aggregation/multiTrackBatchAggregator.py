class MultiTrackBatchAggregator:
    def __init__(self):
        self.batch_aggregator = None

    def aggregate(self, tracks_features):
        """
        Substitute features for each track with respective aggregations.

        :param track_features: (dict) Tracks with corresponding features:
            {
                "filepath1": {
                    "extractor1": np.ndarray([[], [], [], ...])
                    "extractor2": np.ndarray([[], [], [], ....])
                },
                "filepath2": {
                    "extractor1": np.ndarray([[], [], [], ...])
                    "extractor2": np.ndarray([[], [], [], ....])
                },
                ...
            }

        :returns: (dict) dictionary of tracks with aggregated features

        e.g.
            {
                "filepath1": {
                    "extractor1": {
                        "aggregator1": np.ndarray([[], [], [], ...]),
                        "aggregator2": np.ndarray([[], [], [], ...]),
                    },
                    "extractor2": {
                        "aggregator1": np.ndarray([[], [], [], ...]),
                        "aggregator2": np.ndarray([[], [], [], ...]),
                    },
                    ...
                },
                "filepath2": {
                    "extractor1": {
                        "aggregator1": np.ndarray([[], [], [], ...]),
                        "aggregator2": np.ndarray([[], [], [], ...]),
                    },
                    "extractor2": {
                        "aggregator1": np.ndarray([[], [], [], ...]),
                        "aggregator2": np.ndarray([[], [], [], ...]),
                    },
                    ...
                },
                ...
            }
        """
        features = {}
        for track, feature_dict in tracks_features.items():
            features[track] = self._aggregate_features_for_track(feature_dict)
        return features

    def _aggregate_features_for_track(self, track_features):
        features = {}
        for extractor, feature in track_features.items():
            features[extractor] = self.batch_aggregator.aggregate(feature)
        return features
