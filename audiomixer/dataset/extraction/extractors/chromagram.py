from librosa.feature import chroma_stft

from audiomixer.dataset.extraction.extractor import Extractor
from audiomixer.constants import FRAME_SIZE, HOP_LENGTH


class ChromagramExtractor(Extractor):
    def __init__(self, frame_size=FRAME_SIZE, hop_length=HOP_LENGTH):
        super().__init__("Chromagram")
        self.frame_size = frame_size
        self.hop_length = hop_length

    def extract(self, signal, sample_rate):
        """
        Extract chromogram from time series using librosa.

        :param signal: (np.ndarray) Audio time series
        :param sr: (int) Sample rate

        :return: (np.ndarray) Chromogram
        """
        return chroma_stft(
            y=signal, n_fft=self.frame_size, hop_length=self.hop_length, sr=sample_rate
        )
