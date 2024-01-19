import librosa
import pickle
from scipy.io.wavfile import write


def load_audio(path, sr):
    """
    Loads an audio file using librosa

    :param path: (str) Path of the input audio file
    :param sr: (int) sampling rate

    :return: (np.ndarray) Audio Signal
    :return: (int) sample rate
    """
    audio, sr = librosa.load(path, sr=sr)
    return audio, sr


def save_to_pickle(path, data):
    """
    Saves the data as pickle dump

    :param path: (str) Destination path
    :param data: (obj) Data to store
    """
    with open(path, "wb") as file:
        pickle.dump(data, file)


def load_from_pickle(path):
    """
    Saves the data as pickle dump

    :param path: (str) Source path

    :return: (obj) Loaded Python Object
    """
    with open(path, "rb") as file:
        data = pickle.load(file)
    return data


def write_wav(path, signal, sr):
    """Write a time series to wav.

    :param path: (str) Path of file to be saved
    :param signal: (np.ndarray) Time series to be saved
    :param sr: (int) Sample rate
    """
    write(path, sr, signal)
