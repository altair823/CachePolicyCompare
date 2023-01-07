import collections
import random

import numpy as np

from cache_type import Cache
from page.page import Page
from swap_mem import SwapMemory


"""
LRU Cache

This cache uses a Least Recently Used (LRU) replacement policy. 
This means that when a page is requested, if it is not in the cache, 
the page that was least recently used is replaced.
"""
class LRUCache(Cache):
    def __init__(self, size: int, swap_memory: SwapMemory):
        super().__init__(size, swap_memory)
        self.recent_page_queue = collections.deque()

    def get_page_data(self, page_num: int):
        """
        Get page data from cache.
        :param page_num: Page number to get
        :return: Page data
        """
        index = np.where(self.page_nums == page_num)
        if index[0].size == 0:
            index = self.insert(self.swap_memory.get_page(page_num))
            self.recent_page_queue.append(index)
            return self.page_data[index]
        else:
            self.hit_count += 1
            self.recent_page_queue.remove(index[0][0])
            self.recent_page_queue.append(index[0][0])
            return self.page_data[index[0]]

    def replace(self, page: Page):
        min_index = self.recent_page_queue.popleft()
        self.page_nums[min_index] = page.num
        self.page_data[min_index] = page.data
        return min_index

    def __str__(self):
        return "LRU Cache" + str(self.page_nums) + str(self.page_data) + str(self.hit_count) + \
            str(self.recent_page_queue)


if __name__ == '__main__':
    lru_cache = LRUCache(10, SwapMemory(100))
    for i in range(0, 10000):
        lru_cache.get_page_data(random.randint(0, 99))
    print(lru_cache)