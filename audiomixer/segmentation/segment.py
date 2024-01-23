from audiomixer.segmentation.segmentExtractor import SegmentExtractor
from audiomixer.constants import DEFAULT_SAMPLE_RATE


def segment(src_dir, dest_dir, sample_rate=DEFAULT_SAMPLE_RATE):
    """
    Entrypoint for audio segmentation

    Creates segments for audio present in source directory and saves them to destination directory

    :param src_dir: (str) source directory
    :param dest_dir: (str) destination directory
    :param sample_rate: (int) sample rate (default - 22050)
    """
    segment_extractor = SegmentExtractor(sample_rate)
    segment_extractor.create_and_save_segments(src_dir, dest_dir)
