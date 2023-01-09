import numpy as np

from test_env.settings import iterations
from test_env.cache_test import test_all


def test():
    eighty_pages = np.random.randint(0, 20, int(iterations * 0.8))
    twenty_pages = np.random.randint(20, 100, int(iterations * 0.2))
    test_cases = np.concatenate((eighty_pages, twenty_pages))
    np.random.shuffle(test_cases)
    test_all("Eighty vs twenty page requests with cache size 1 to 100", test_cases)


if __name__ == '__main__':
    test()
