import unittest
class test_reverse(unittest.TestCase):
    def setUp(self):
        self.args = ("nba cchat gossiping")
    def test_reverse_no_split(self):
        ans = "gnipissog tahcc abn"
        self.assertEqual(ans,reverse(self.args))
    def test_reverse_split(self):
        ans = "abn tahcc gnipissog"
        self.assertEqual(ans,reverse_split(self.args))
        
def reverse(str):
    return str[::-1]
def reverse_split(str):
    s_split =  str.split(' ')
    str = ""
    for i in s_split:
        str+=i[::-1]
        str+=" "
    str=str[:len(str)-1]
    return str

if __name__ == '__main__':
    unittest.main()
    # str = input('input: ')
    # print(reverse(str))
    # print(reverse_split(str))
    