import numpy as np

from test_env.settings import iterations
from test_env.cache_test import test_all


def test():
    fifty_pages = np.empty(0, dtype=int)
    print(fifty_pages)
    for i in range(0, int(iterations / 50)):
        fifty_pages = np.concatenate((fifty_pages, np.arange(0, 50)))
    test_cases = fifty_pages
    print(test_cases)
    test_all(str(iterations) + "_fifty_serial_test.png", test_cases)


if __name__ == '__main__':
    test()
