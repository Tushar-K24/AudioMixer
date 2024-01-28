import numpy as np


class FeatureMerger:
    """
    Feature Merger is responsible for merging all features of a track into a single feature vector
    """

    def __init__(self):
        pass

    def merge(self, tracks_features, feature_aggregation="mean"):
        """
        merges all features for a list of tracks

        :param tracks_features: (dict) Track with corresponding features:
            {
                "filepath1": {
                    "extractor1": {
                        "mean": np.ndarray([[], [], [], ...]),
                        "std": np.ndarray([[], [], [], ...]),
                    },
                    "extractor2": {
                        "mean": np.ndarray([[], [], [], ...]),
                        "std": np.ndarray([[], [], [], ...]),
                    },
                    ...
                },
                ...
            }
        """
        merged_features = {}
        for track_path, track_features in tracks_features.items():
            track_merged_features = self._merge_features_for_track(
                track_features, feature_aggregation
            )
            merged_features[track_path] = track_merged_features
        return merged_features

    def _merge_features_for_track(self, track_features, feature_aggregation):
        features = [feature[feature_aggregation] for feature in track_features.values()]
        return np.hstack(features)
