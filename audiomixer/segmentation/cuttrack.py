def cut(signal, delimiters):
    """
    Cuts the signal into chunks as per the delimiters given

    :param signal: (np.ndarray) input signal to be cut
    :param delimiters: (np.ndarray) frame indices where cut is to be made

    :return: list (np.ndarray) list of signal chunks
    """
    start, signal_chunks = 0, []
    for end in delimiters:
        signal_chunks.append(signal[start:end])
        start = end
    signal_chunks.append(signal[start:])
    return signal_chunks
