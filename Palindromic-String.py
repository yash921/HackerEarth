# Write your code here
s = input()
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    def toCheck(s):
        if s == True:
            print("YES")
        else:
            print("NO")
    return toCheck(isPal(toChars(s)))
isPalindrome(s)
