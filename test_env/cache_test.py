import tqdm

from cache.optimal_cache import OptimalCache
from cache.random_cache import RandomCache
from cache.fifo_cache import FIFOCache
from cache.lfu_cache import LFUCache
from cache.lru_cache import LRUCache

from test_env.swap_mem import SwapMemory

import numpy as np
import matplotlib.pyplot as plt

from test_env.settings import iterations, cache_min_value, cache_max_value


def test_all(test_name: str, test_cases: np.ndarray):
    optimal_cache_hit_count = []
    random_cache_hit_count = []
    fifo_cache_hit_count = []
    lfu_cache_hit_count = []
    lru_cache_hit_count = []

    for cache_size in tqdm.trange(cache_min_value, cache_max_value):
        optimal_cache = OptimalCache(cache_size, SwapMemory(100), test_cases)
        random_cache = RandomCache(cache_size, SwapMemory(100))
        fifo_cache = FIFOCache(cache_size, SwapMemory(100))
        # lfu_cache = LFUCache(cache_size, SwapMemory(100))
        lru_cache = LRUCache(cache_size, SwapMemory(100))

        for i in test_cases:
            optimal_cache.get_page_data(i)
            random_cache.get_page_data(i)
            fifo_cache.get_page_data(i)
            # lfu_cache.get_page_data(i)
            lru_cache.get_page_data(i)

        optimal_cache_hit_count.append(optimal_cache.hit_count)
        random_cache_hit_count.append(random_cache.hit_count)
        fifo_cache_hit_count.append(fifo_cache.hit_count)
        # lfu_cache_hit_count.append(lfu_cache.hit_count)
        lru_cache_hit_count.append(lru_cache.hit_count)

    # Comparing the relationship between cache size and cache hits by cache type
    # Creating
    plt.title(test_name)
    plt.plot(optimal_cache_hit_count, label="Optimal Cache", linestyle='--', linewidth=3)
    plt.plot(random_cache_hit_count, label="Random Cache", linestyle='--', linewidth=3)
    plt.plot(fifo_cache_hit_count, label="FIFO Cache", linewidth=4, alpha=0.5)
    # plt.plot(lfu_cache_hit_count, label="LFU Cache")
    plt.plot(lru_cache_hit_count, label="LRU Cache", linestyle='--', linewidth=3)
    plt.legend()
    plt.xlabel("Cache Size")
    plt.ylabel("Cache Hits")
    # plt.show()
    test_name = test_name.replace(" ", "_")
    plt.savefig(test_name + ".png", dpi=800)
    plt.close()

    # Print all the cache hit counts
    # print("Optimal Cache Hit Count: " + str(optimal_cache_hit_count))
    # print("Random Cache Hit Count: " + str(random_cache_hit_count))
    # print("FIFO Cache Hit Count: " + str(fifo_cache_hit_count))
    # print("LFU Cache Hit Count: " + str(lfu_cache_hit_count))
    # print("LRU Cache Hit Count: " + str(lru_cache_hit_count))
