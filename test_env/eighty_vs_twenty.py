import numpy as np

from test_settings import iterations
from cache_test import test_all


def eighty_vs_twenty_test():
    eighty_pages = np.random.randint(0, 20, int(iterations * 0.8))
    twenty_pages = np.random.randint(20, 100, int(iterations * 0.2))
    test_cases = np.concatenate((eighty_pages, twenty_pages))
    np.random.shuffle(test_cases)
    test_all(str(iterations) + "_eighty_vs_twenty_test", test_cases)


if __name__ == '__main__':
    eighty_vs_twenty_test()
