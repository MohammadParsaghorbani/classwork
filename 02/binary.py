class BinarySearch:
    def __init__(self, item):
        self.item = item
        self.list = []
    def create_list(self):
        print("Please enter the elements of the list:")
        for i in range(self.item):
            element = int(input())
            self.list.append(element)
    def bubble_sort(self):
        for i in range(len(self.list)):
            for z in range(0, len(self.list)-i-1):
                if self.list[z] > self.list[z+1]:
                    self.list[z], self.list[z+1] = self.list[z+1], self.list[z]
        print(self.list)
size = int(input("Enter the size of the list: "))
binary_search = BinarySearch(size)
binary_search.create_list()
binary_search.bubble_sort()