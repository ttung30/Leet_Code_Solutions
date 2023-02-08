class Solution:
    def isPalindrome(self, x: int) -> bool:
        clone =0
        z = x
        while x>0:
            clone = clone +  x % 10
            clone = clone * 10
            x = int(x/10)
           
        if int(clone/10) == z:
            return True
        else:
            return False
