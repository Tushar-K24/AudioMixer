import librosa

from audiomixer.segmentation.constants import HOP_LENGTH


def track_beat_and_tempo(signal, sr):
    """
    Beat tracker using librosa

    :param signal: (np.ndarray) Audio signal to analyze
    :param sr: (int) sampling rate

    :return: (np.ndarray) Estimated beat events measured in samples
    :return: (float) Estimated global tempo (in beats per minute)
    """
    tempo, beat_frames = librosa.beat.beat_track(y=signal, sr=sr, hop_length=HOP_LENGTH)
    return beat_frames, tempo
