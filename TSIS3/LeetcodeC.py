class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x = str(x)
        # return x == x[::-1]
        a = str(x)
        b = a[::-1]
        if a==b:
            return True
        else:
            return False