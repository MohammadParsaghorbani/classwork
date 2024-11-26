class BinarySearch:
    def __init__(self, item_num):
        self.item_num = item_num
    def create(self):
        self.l = []
        a = self.item_num
        for count in range(0 , int(a)):
            user_item = input("enter your item: ")
            self.l.append(user_item)
        self.l.sort()
        return self.l
    def sort(self):
        userlist= self.l
        helper = []
        num_1 = len(userlist)

        for i in userlist:
            num = num_1 - 1
            if i > userlist[num_1 - num]:
                helper.append(i)
            else :
                continue
        print(helper)

            
    
num = input("how many item do you want to enter? ")
x = BinarySearch(num)
x.create
a = x.create()
a.sort()