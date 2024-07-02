class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        list1 = []
        while x>0:
            rem = x % 10
            list1.append(rem)
            x = x//10
        list2 = list1[::-1]
        if list2 == list1:
            return True
        else:
            return False

#return str(x) == str(x)[::-1]