class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ''.join(char for char in s if char.isalnum()).lower()
        a, b = 0, len(alphanumeric) - 1
        while a <= b:
            if alphanumeric[a] != alphanumeric[b]:
                return False
            a += 1
            b -= 1
        return True


        