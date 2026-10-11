class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        left = 0
        rigth = len(s) - 1        

        while(left < rigth):
            if s[left] != s[rigth]:
                return False

            left += 1
            rigth -= 1

        return True        