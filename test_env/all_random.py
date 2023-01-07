from cache.optimal_cache import OptimalCache
from cache.random_cache import RandomCache
from cache.fifo_cache import FIFOCache
from cache.lfu_cache import LFUCache
from cache.lru_cache import LRUCache

from swap_mem import SwapMemory

import random

import numpy as np
import matplotlib.pyplot as plt

from test_env.test_settings import iterations, cache_min_value, cache_max_value

if __name__ == '__main__':
    optimal_cache_hit_count = []
    random_cache_hit_count = []
    fifo_cache_hit_count = []
    lfu_cache_hit_count = []
    lru_cache_hit_count = []

    test_cases = np.random.randint(0, 100, iterations)

    for cache_size in range(cache_min_value, cache_max_value):
        optimal_cache = OptimalCache(cache_size, SwapMemory(100), test_cases)
        random_cache = RandomCache(cache_size, SwapMemory(100))
        fifo_cache = FIFOCache(cache_size, SwapMemory(100))
        lfu_cache = LFUCache(cache_size, SwapMemory(100))
        lru_cache = LRUCache(cache_size, SwapMemory(100))

        for i in test_cases:
            optimal_cache.get_page_data(i)
            random_cache.get_page_data(i)
            fifo_cache.get_page_data(i)
            lfu_cache.get_page_data(i)
            lru_cache.get_page_data(i)

        optimal_cache_hit_count.append(optimal_cache.hit_count)
        random_cache_hit_count.append(random_cache.hit_count)
        fifo_cache_hit_count.append(fifo_cache.hit_count)
        lfu_cache_hit_count.append(lfu_cache.hit_count)
        lru_cache_hit_count.append(lru_cache.hit_count)

    # Comparing the relationship between cache size and cache hits by cache type
    plt.title("Random 10000 page requests with cache size 1-100")
    plt.plot(optimal_cache_hit_count, label="Optimal Cache")
    plt.plot(random_cache_hit_count, label="Random Cache")
    plt.plot(fifo_cache_hit_count, label="FIFO Cache")
    plt.plot(lfu_cache_hit_count, label="LFU Cache")
    plt.plot(lru_cache_hit_count, label="LRU Cache")
    plt.legend()
    plt.xlabel("Cache Size")
    plt.ylabel("Cache Hits")
    #plt.show()
    plt.savefig(str(iterations) + "_all_random.png", dpi=800)

    # Print all the cache hit counts
    print("Optimal Cache Hit Count: " + str(optimal_cache_hit_count))
    print("Random Cache Hit Count: " + str(random_cache_hit_count))
    print("FIFO Cache Hit Count: " + str(fifo_cache_hit_count))
    print("LFU Cache Hit Count: " + str(lfu_cache_hit_count))
    print("LRU Cache Hit Count: " + str(lru_cache_hit_count))



