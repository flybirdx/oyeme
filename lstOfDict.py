
import random
import datetime # simple time cost calculating tool

# get randomized generator
class TestGen(object):
    """ test case generator """
    def __init__(self, count, itemNum, inversedPercent=2, chrRange=256):
        self.count = count
        self.itemNum = itemNum
        self.inversedPercent = inversedPercent
        self.chrRange = chrRange

    def generate(self):
        lst = []
        for _ in range(self.count):
            r = random.randrange(self.itemNum)
            items = [i for i in range(r)]
            random.shuffle(items)
            subDict = {}
            for item in items:  # 1/self.inversedPercent of total items include '_id', lets rock !
                if item % self.inversedPercent == 0:
                    subDict['_id'] = item
                else:
                    subDict[chr(item % self.chrRange)] = item
            lst.append(subDict)
        return lst


# test
def test():
    t0 = datetime.datetime.now()
    tg = TestGen(100, 90)
    lst = tg.generate()
    t1 = datetime.datetime.now()

    # a matter of algorithm
    lst = [{k: v for k, v in dct.items() if k != '_id'} for dct in lst]

    t2 = datetime.datetime.now()
    # in numpy we use npArray.size() to get (x,y,z,... ,n) axis
    print('lst(%d*%d) time cost = %s, %s' % (tg.count, tg.itemNum, str(t1 - t0), str(t2 - t1)))

if __name__ == '__main__':
    test()
