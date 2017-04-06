'''
Convenient data selection, iteration and loading
'''

import numpy as np
from scipy.io import loadmat


#====================================================================================================
def load_data(filename):
    struct = loadmat(str(filename))
    data, *stuff = struct['dataStruct'][0][0]
    sampling_frq, length, chnls, *timestamp = \
        (a.squeeze() if a.size > 1 else np.asscalar(a) for a in stuff)
    duration = length / sampling_frq
    Nch = len(chnls)
    timestamp = int(timestamp[0]) if len(timestamp) else None
    return data.T, duration, sampling_frq, Nch, timestamp

