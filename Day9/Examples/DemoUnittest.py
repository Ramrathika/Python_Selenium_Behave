import unittest

def setUpModule():
    print("Setup Module")

class sample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setup class")

    def setUp(self):
        print("Setup Step")

    def test1(self):
        print("Test 1")

    def test2(self):
        print("Test 2")

    #@unittest.skipUnless(3 == 2 ,"2 is equal than 2")
    def test3(self):
        print("Test 3")
        self.skipTest("Not needed")

    def tearDown(self):
        print("Teardown step")

    @classmethod
    def tearDownClass(cls):
        print("Teardown class")


def tearDownModule():
    print("TearDown module")

    if __name__ == '__main__':
        unittest.main()