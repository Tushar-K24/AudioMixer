from audiomixer.utils.io import save_to_pickle


class DatasetPipeline:
    def __init__(self):
        self.batch_extractor = None
        self.feature_aggregator = None
        self.feature_merger = None

    def process(self, dir, save_dir):
        """
        Generate embeddings for all audio files in given directory and stores feature vectors and their mappings as dataset.

        :param dir: (str) Source Directory
        :param save_dir: (str) Directory to save dataset
        """
        print("Extracting track features")
        tracks_features = self.batch_extractor.extract(dir)
        print("Generating track aggregations")
        tracks_aggregations = self.feature_aggregator.aggregate(tracks_features)
        print("Merging features")
        merged_features = self.feature_merger.merge(tracks_aggregations)
        print("Saving final features")
        # save
        save_to_pickle(save_dir + "dataset.pkl", merged_features)
