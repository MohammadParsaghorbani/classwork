class BinarySearch:
    def __init__(self, item_num):
        self.item_num = item_num
    def create(self):
        l = []
        a = self.item_num
        for count in range(0 , int(a)):
            user_item = input("enter your item: ")
            l.append(user_item)
        l.sort()
        return l
    def sort(self):
        userlist= self.create()
        
    
num = input("how many item do you want to enter? ")
x = BinarySearch(num)
x.create()