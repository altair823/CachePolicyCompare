import random

import numpy as np

from cache.cache_type import Cache
from page.page import Page
from test_env.swap_mem import SwapMemory


class LFUCache(Cache):
    """
    LFU Cache

    LFU (Least Frequently Used) Cache is a cache replacement algorithm that replaces the least frequently used page.

    This means that when a page is requested, if it is not in the cache,
    the page that was least frequently used is replaced.
    """
    def __init__(self, size: int, swap_memory: SwapMemory):
        super().__init__(size, swap_memory)
        self.page_freq = np.zeros(size, dtype=np.uint32)

    def get_page_data(self, page_num: int):
        """
        Get page data from cache.
        :param page_num: Page number to get
        :return: Page data
        """
        index = np.where(self.page_nums == page_num)
        if index[0].size == 0:
            return self.page_data[self.insert(self.swap_memory.get_page(page_num))]
        else:
            self.hit_count += 1
            self.page_freq[index[0]] += 1
            return self.page_data[index[0]]

    def replace(self, page: Page):
        min_index = np.argmin(self.page_freq)
        self.page_nums[min_index] = page.num
        self.page_data[min_index] = page.data
        self.page_freq[min_index] = 0
        return min_index

    def __str__(self):
        return "LFU Cache" + str(self.page_nums) + str(self.page_data) + str(self.hit_count) + str(self.page_freq)


if __name__ == '__main__':
    lfu_cache = LFUCache(10, SwapMemory(100))
    for i in range(0, 10000):
        lfu_cache.get_page_data(random.randint(0, 99))
    print(lfu_cache)
