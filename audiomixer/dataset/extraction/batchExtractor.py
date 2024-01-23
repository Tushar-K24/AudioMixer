import os

from audiomixer.dataset.extraction.extractor import Extractor
from audiomixer.utils.io import load_audio


class BatchExtractor:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.extractors = []

    def add_extractor(self, extractor):
        """
        Adds an Extractor to the extractors.

        :param extractor: (Extractor) Extractor (e.g., MFCCExtractor)
        """
        assert isinstance(extractor, Extractor)
        self.extractors.append(extractor)

    def extract(self, dir):
        """
        Returns Extracted features for all audio files in the directory

        :param dir: (string) directory storing audio files

        :returns: (dict) dictionary with audio file paths as keys and extracted feature dictionaries as their values:
        e.g.
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
        """
        features = {}
        for root, _, files in os.walk(dir):
            for file in files:
                file_path = os.path.join(root, file)
                features[file_path] = self._extract_features_for_file(file_path)
        return features

    def _extract_features_for_file(self, file_path):
        signal = load_audio(file_path, self.sample_rate)
        features = {}
        for extractor in self.extractors:
            features[extractor.name] = extractor.extract(signal, self.sample_rate)
        return features
