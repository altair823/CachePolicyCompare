from page.page import Page


class SwapMemory:
    def __init__(self, size: int):
        self.swapped_pages = [Page(i) for i in range(size)]

    def get_page(self, page_num: int):
        return self.swapped_pages[page_num]


if __name__ == '__main__':
    print(SwapMemory(100).swapped_pages)
