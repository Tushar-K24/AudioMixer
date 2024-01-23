from audiomixer.dataset.datasetPipeline import DatasetPipeline

from audiomixer.dataset.extraction.batchExtractor import BatchExtractor
from audiomixer.dataset.extraction.extractors.chromagram import ChromagramExtractor
from audiomixer.dataset.extraction.extractors.mfcc import MFCCExtractor

from audiomixer.dataset.aggregation.aggregators.meanAggregator import MeanAggregator
from audiomixer.dataset.aggregation.batchAggregators.heirarchicalBatchAggregator import (
    HeirarchicalBatchAggregator,
)
from audiomixer.dataset.aggregation.multiTrackBatchAggregator import (
    MultiTrackBatchAggregator,
)

from audiomixer.constants import DEFAULT_SAMPLE_RATE


def create_dataset(dir, save_dir, sample_rate=DEFAULT_SAMPLE_RATE):
    batch_extractor = BatchExtractor(sample_rate)
    extractors = [ChromagramExtractor(), MFCCExtractor()]
    for extractor in extractors:
        batch_extractor.add_extractor(extractor)

    hba = HeirarchicalBatchAggregator()
    mtba = MultiTrackBatchAggregator()
    mtba.batch_aggregator = hba
    aggregators = [MeanAggregator(1)]
    for aggregator in aggregators:
        hba.add_aggregator(aggregator)

    dataset_pipeline = DatasetPipeline()
    dataset_pipeline.batch_extractor = batch_extractor
    dataset_pipeline.feature_aggregator = mtba

    dataset_pipeline.process(dir, save_dir)
