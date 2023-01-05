import numpy as np

from cache_type import Cache
from page.page import Page


class RandomCache(Cache):
    def replace(self, page: Page):
        """
        Replace page in cache to given page.
        :param page: Page to replace
        :return: None
        """
        random_index = np.random.randint(0, len(self.page_nums))
        self.page_nums[random_index] = page.num

    def __str__(self):
        pass