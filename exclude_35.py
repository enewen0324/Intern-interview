import unittest
class test_exclude(unittest.TestCase):
    def setUp(self):
        self.args = (35)
    def test_exclude_35(self):
        ans = 0
        for i in range(1,self.args+1):
            if( (i%3==0 or i%5==0) ):
                if(i%15==0):
                    ans = ans + 1
            else:
                ans = ans + 1
        self.assertEqual(ans,exclude_35(self.args))

def exclude_35(num):
    return int(num - num/3 - num/5 + 2*(num/15))

if __name__ == '__main__':
    unittest.main()
    # num = input('num: ')
    # print(exclude_35(int(num)))
