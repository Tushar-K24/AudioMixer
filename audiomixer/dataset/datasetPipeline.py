class DatasetPipeline:
    def __init__(self):
        self.batch_extractor = None
        self.feature_aggregator = None

    def process(self, dir, save_dir):
        """
        Generate embeddings for all audio files in given directory and stores feature vectors and their mappings as dataset.

        :param dir: (str) Source Directory
        :param save_dir: (str) Directory to save dataset
        """
        tracks_features = self.batch_extractor.extract(dir)
        tracks_aggregations = self.feature_aggregator.aggregate(tracks_features)
        print(tracks_aggregations)
