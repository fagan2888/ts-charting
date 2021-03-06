import numpy as np

def process_signal(series, source):
    """
        Take any non 0/na value and changes it to corresponding value of source
    """
    temp = series.astype(float).copy()
    temp[temp == 0] = np.nan
    temp, source = temp.align(source, join='left')
    temp *= source
    return temp
