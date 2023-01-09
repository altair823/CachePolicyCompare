import random

import numpy as np

from cache.cache_type import Cache
from page.page import Page
from test_env.swap_mem import SwapMemory


class RandomCache(Cache):
    def replace(self, page: Page):
        random_index = np.random.randint(0, len(self.page_nums))
        self.page_nums[random_index] = page.num
        self.page_data[random_index] = page.data
        return random_index

    def __str__(self):
        return "Random Cache" + str(self.page_nums) + str(self.page_data) + str(self.hit_count)


if __name__ == '__main__':
    random_cache = RandomCache(100, SwapMemory(100))
    for i in range(0, 10000):
        random_cache.get_page_data(random.randint(0, 99))
    print(random_cache)
