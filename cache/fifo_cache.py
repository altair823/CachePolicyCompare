import random

from cache.cache_type import Cache
from page.page import Page
from test_env.swap_mem import SwapMemory


class FIFOCache(Cache):
    def __init__(self, size: int, swap_memory: SwapMemory):
        super().__init__(size, swap_memory)
        self.index = 0

    def replace(self, page: Page):
        self.page_nums[self.index] = page.num
        self.page_data[self.index] = page.data
        self.index = (self.index + 1) % len(self.page_nums)
        return self.index

    def __str__(self):
        return "FIFO Cache" + str(self.page_nums) + str(self.page_data) + str(self.hit_count)


if __name__ == '__main__':
    fifo_cache = FIFOCache(100, SwapMemory(100))
    for i in range(0, 10000):
        fifo_cache.get_page_data(random.randint(0, 99))
    print(fifo_cache)
