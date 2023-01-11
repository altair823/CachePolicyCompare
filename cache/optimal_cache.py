import numpy as np
from tqdm import trange

from cache.cache_type import Cache
from page.page import Page
from test_env.swap_mem import SwapMemory

from unittest import TestCase

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
        self.counter = 0

    def get_page_data(self, _page_num: int):
        """
        Get page data from cache.
        :param _page_num: Dummy page number. This is not used.
        :return: Page data
        """
        page_num = self.future_page_nums[self.counter]
        index = np.where(self.page_nums == page_num)
        if index[0].size == 0:
            data = self.page_data[self.insert(self.swap_memory.get_page(page_num))]
            self.counter += 1
        else:
            self.hit_count += 1
            data = self.page_data[index[0]][0]
            self.counter += 1
        return data

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
            found_index = np.where(self.future_page_nums == self.page_nums[i])[0][0]
            distance = found_index - self.counter
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
        found_index = np.where(self.future_page_nums == page_num)[0][0]

        # for i in range(len(self.future_page_nums)):
        #     if self.future_page_nums[i] == page_num:
        #         return i
        # return len(self.future_page_nums) + 1


class SingleTest(TestCase):
    # Single Cache Test
    def test_single(self):
        # Get the future page numbers
        future_pages = np.random.randint(0, 99, 1000)
        # Create the cache
        optimal_cache = OptimalCache(10, SwapMemory(100), future_pages)
        # Get the page data
        for i in future_pages:
            a = optimal_cache.get_page_data(i)
            # Check data
            assert a == "h" + chr(i)
        # Print the cache
        print(optimal_cache)

    # Multiple Cache Test
    def test_multiple(self):
        optimal_cache_hit_count = []
        for cache_size in trange(1, 100):
            # Get the future page numbers
            future_pages = np.random.randint(0, 99, 1000)
            # Create the cache
            optimal_cache = OptimalCache(cache_size, SwapMemory(100), future_pages)
            # Get the page data
            for i in future_pages:
                a = optimal_cache.get_page_data(i)
                # Check data
                assert a == "h" + chr(i)
            # Print the cache
            # Save the hit count
            optimal_cache_hit_count.append(optimal_cache.hit_count)

        # Show matplotlib graph
        import matplotlib.pyplot as plt
        plt.plot(optimal_cache_hit_count)
        plt.show()
