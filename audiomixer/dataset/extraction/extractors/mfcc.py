from librosa.feature import mfcc

from audiomixer.dataset.extraction.extractor import Extractor
from audiomixer.constants import FRAME_SIZE, HOP_LENGTH, NUM_COEFFICIENTS


class MFCCExtractor(Extractor):
    def __init__(
        self,
        frame_size=FRAME_SIZE,
        hop_length=HOP_LENGTH,
        num_coefficients=NUM_COEFFICIENTS,
    ):
        super().__init__("MFCC")
        self.frame_size = frame_size
        self.hop_length = hop_length
        self.num_coefficients = num_coefficients

    def extract(self, signal, sample_rate):
        """
        Extract MFCC from time series using librosa.

        :param signal: (np.ndarray) Audio time series
        :param sr: (int) Sample rate

        :return: (np.ndarray) MFCC sequence
        """
        return mfcc(
            y=signal,
            n_mfcc=self.num_coefficients,
            n_fft=self.frame_size,
            hop_length=self.hop_length,
            sr=sample_rate,
        )
