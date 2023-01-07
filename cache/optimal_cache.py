import numpy as np

from cache.cache_type import Cache
from page.page import Page
from swap_mem import SwapMemory


class OptimalCache(Cache):
    """
    Optimal Cache

    This cache always replaces the page that will be used last.
    So to use this cache, we need to know the future page numbers.
    This is why we need to pass the future page numbers to the constructor.
    And, This is also why it is not realistic but imaginary and only used in benchmark.
    """
    def __str__(self):
        return "Optimal Cache" + str(self.page_nums) + str(self.page_data) + str(self.hit_count)

    def __init__(self, size: int, swap_memory: SwapMemory, future_page_nums: np.ndarray):
        super().__init__(size, swap_memory)
        self.future_page_nums = future_page_nums

    def replace(self, page: Page):
        """
        Find the page that will not be used for the longest time and replace it.
        :param page: Page to replace
        :return: Index of replaced page
        """
        # Find the page that will not be used for the longest time
        max_index = 0
        max_distance = 0
        for i in range(len(self.page_nums)):
            distance = self.find_distance(i)
            if distance > max_distance:
                max_distance = distance
                max_index = i
        # Replace the page
        self.page_nums[max_index] = page.num
        self.page_data[max_index] = page.data
        return max_index

    def find_distance(self, page_num: int):
        """
        Find the distance between the given page and the next time it will be used.
        :param page_num: Page number to find distance for
        :return: Distance between the given page and the next time it will be used
        """
        return np.where(self.future_page_nums == page_num)[0][0]
        # for i in range(len(self.future_page_nums)):
        #     if self.future_page_nums[i] == page_num:
        #         return i
        # return len(self.future_page_nums) + 1


if __name__ == '__main__':
    # Get the future page numbers
    future_pages = np.random.randint(0, 99, 10000)
    # Create the cache
    optimal_cache = OptimalCache(10, SwapMemory(100), future_pages)
    # Get the page data
    for i in range(0, 10000):
        optimal_cache.get_page_data(future_pages[i])
    # Print the cache
    print(optimal_cache)
