import os
from tqdm import tqdm

from audiomixer.utils.io import load_audio, write_wav
from audiomixer.segmentation.constants import HOP_LENGTH
from audiomixer.segmentation.beattracker import track_beat_and_tempo
from audiomixer.segmentation.cuttrack import cut


class SegmentExtractor:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self._audio_format = "wav"

    def create_and_save_segments(self, dir, save_dir):
        """
        Performs the following steps for each audio file in a
        directory:
            1- load audio file
            2- extract beat locations
            3- segment signal into as many chunks as beats we have
            4- save audio segments to wav

        :param dir: (str) Directory containing audio files to be preprocessed
        :param save_dir: (str) Directory where to save segments
        """
        for root, _, files in tqdm(os.walk(dir)):
            for file in files:
                self._create_and_save_segments_for_file(root, file, save_dir)

    def _create_and_save_segments_for_file(self, root, file, save_dir):
        file_path = os.path.join(root, file)
        audio, _ = load_audio(file_path, self.sample_rate)
        beats, _ = track_beat_and_tempo(audio, self.sample_rate)
        segments = cut(audio, beats * HOP_LENGTH)
        self._write_segments_to_wav(file, save_dir, segments)

    def _write_segments_to_wav(self, file, save_dir, segments):
        for i, segment in enumerate(segments):
            save_path = self._generate_save_path(file, save_dir, i)
            write_wav(save_path, segment, self.sample_rate)

    def _generate_save_path(self, file, save_dir, segment_index):
        file_name = f"{file}_{segment_index}.{self._audio_format}"
        return os.path.join(save_dir, file_name)
