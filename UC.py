'''''''''
#testando função
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

if __name__=='__main__':
    unittest.main()
'''''''''
#testando classes
import unittest

class MyFun:
    def fun(self, n):
        return n + 1

class MyTest(unittest.TestCase):
    def testFun(self):
        obj = MyFun()
        self.assertEqual(obj.fun(3), 4)

if __name__=='__main__':
    unittest.main()







