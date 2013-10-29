from numpy.linalg import norm

ji_intervals = np.array([-2400, -2289, -2197, -2085, -2014, -1902, -1791,
                          -1699, -1587, -1516, -1404, -1312, -1200, -1089,
                          -997, -885, -814, -702, -591, -499, -387, -316,
                          -204, -112, 0, 111, 203, 315, 386, 498, 609, 701,
                          813, 884, 996, 1088, 1200, 1311, 1403, 1515,
                          1586, 1698, 1809, 1901, 2013, 2084, 2196, 2288,
                          2400, 2511, 2603, 2715, 2786, 2898, 3009, 3101,
                          3213, 3284, 3396, 3488, 3600, 3711, 3803, 3915,
                          3986, 4098, 4209, 4301, 4413, 4484, 4596, 4688,
                          4800])

def fill_in(profile, _min=-2400, _max=4800]):
    #Fill zeros for features from intervals absent in the profile
    for interval in ji_intervals:
        if interval not in profile.keys():
            profile[interval] = {"position": 0,
                                 "mean": 0,
                                 "amplitude": 0,
                                 "variance": 0,
                                 "skew1": 0,
                                 "skew2": 0,
                                 "kurtosis": 0}

    #Remove intervals beyond the desirable range
    for interval in profile.keys():
        if _max < int(interval) < _min:
            profile.pop(interval)

    return profile

def distance(profile1, profile2):
    v1 = profile1.values()
    v2 = profile2.values()
    return norm(v1-v2)
