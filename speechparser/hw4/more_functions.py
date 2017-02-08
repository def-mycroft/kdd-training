""" Solution to HW4 more_functions module"""

def odd_even_merge(list1, list2):
    """Merges odd values from L1 and even from L2"""
    list1_odd = []
    for item in list1:
        if item in [x for x in range(10000) if x % 2]:
            list1_odd.append(item)

    list2_even = []
    for item in list2:
        if item in [x for x in range(10000) if not x % 2]:
            list2_even.append(item)

    return list1_odd + list2_even


def make_dict(a_list):
    """ Returns a dict from values of a_list."""
    made_dict = {}

    for item in a_list:
        made_dict["key%s" % a_list.index(item)] = item

    return made_dict


def transpose_matrix(matrix):
    """Takes a square matrix and returns a transposed version"""
    def zipper(*args):
        return args

    return map(zipper, *matrix)


def merge_dicts(dict1, dict2):
    """Returns a merged dictionary"""
    return dict(dict1.items() + dict2.items())


def squares(start, qty):
    """Generates a qty-long list of squared numbers from start"""
    return list(map(lambda x: x ** 2, range(start, (start+qty))))
