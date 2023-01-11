import numpy as np

from test_env.swap_mem import SwapMemory
from page.page import Page


class Cache:
    def __init__(self, size: int, swap_memory: SwapMemory):
        self.swap_memory = swap_memory
        self.page_nums = np.full(size, -1, dtype=np.int32)
        self.page_data = np.full(size, "", dtype=object)
        self.hit_count = np.uint32(0)
        self.is_full = False

    def __str__(self):
        raise NotImplementedError()

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
            return self.page_data[index[0]][0]

    def replace(self, page: Page):
        """
        Replace page in cache to given page.
        :param page: Page to replace
        :return: Index of replaced page
        """
        raise NotImplementedError()

    def insert(self, page: Page):
        """
        Insert page to cache.
        :param page: Page to insert
        :return: Index of inserted page
        """
        if self.is_full is True:
            return self.replace(page)
        else:
            empty_index = np.where(self.page_nums == -1)
            if empty_index[0].size == 0:
                self.is_full = True
                return self.replace(page)
            else:
                self.page_nums[empty_index[0][0]] = page.num
                self.page_data[empty_index[0][0]] = page.data
                return empty_index[0][0]
