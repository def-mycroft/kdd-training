def make_odds(size, start):
    """Makes a SIZE length list of odd numbers, starting with START"""
    # TODO Returns a "not callable" error.
    return ([x for x in range(start, (size + 1)) if x % 2])
