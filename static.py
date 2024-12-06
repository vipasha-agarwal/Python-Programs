class math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num+n
# static method is used in constructor to ship the method within class and use without the self argument
    @staticmethod
    def add (a, b):
        return a + b

# result = math.add(1, 2)
# print(result)
a = math(8)
print(a.num)
a.addtonum(7)
print(a.num)