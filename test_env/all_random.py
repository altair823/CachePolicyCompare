"""Test case 1: All random page requests
    This test case will generate 10000 random page requests and test the cache hit rate for each cache type.
    The cache size will be 1-100.

    The optimal cache is just for reference with the other cache types.
    It needs to know all the page requests in advance, so it is not a realistic cache type.
"""
import numpy as np

from test_settings import iterations
from cache_test import test_all


def all_random_test():
    test_cases = np.random.randint(0, 100, iterations)
    test_all(str(iterations) + "_all_random_test.png", test_cases)


if __name__ == '__main__':
    all_random_test()
