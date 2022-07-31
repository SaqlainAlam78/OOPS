class first:
    def __init__(self):
        self.lst1=1
    def func1(self,lst1):
        self.lst1=lst1
        print(self.lst1)

obj1=first()
lst1=[1,2,3]
obj1.func1(lst1)