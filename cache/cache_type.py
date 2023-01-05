import numpy as np

from swap_mem import SwapMemory
from page.page import Page


class Cache:
    def __init__(self, size, swap_memory: SwapMemory):
        self.swap_memory = swap_memory
        self.page_nums = np.full(size, -1, dtype=np.uint32)
        self.page_data = np.full(size, "", dtype=np.str)
        self.hit_count = np.zeros(size, dtype=np.uint32)
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
        if len(index) == 0:
            self.insert(self.swap_memory.get_page(page_num))
        else:
            self.hit_count[index[0]] += 1
            return self.page_data[index[0]]

    def replace(self, page: Page):
        """
        Replace page in cache to given page.
        :param page: Page to replace
        :return: None
        """
        raise NotImplementedError()

    def insert(self, page: Page):
        """
        Insert page to cache.
        :param page: Page to insert
        :return: None
        """
        if self.is_full is True:
            self.replace(page)
        else:
            empty_index = np.where(self.page_nums == -1)
            if len(empty_index) == 0:
                self.is_full = True
                self.replace(page)
            else:
                self.page_nums[empty_index[0]] = page.num
                self.page_data[empty_index[0]] = page.data

