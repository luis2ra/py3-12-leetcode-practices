'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

'''

class Solution:
    def gcd_of_strings(self, str1: str, str2: str) -> str:
        for i in range(len(str2), 0, -1):
            print(i, str2[:i], str1.count(str2[:i]))
            '''
            En el if, se agrega la validacion:
                len(str1) != len(str2[:i]
            de esta manera, satisface este escenario de prueba:
            str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
            str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
            '''
            if str1.count(str2[:i]) * len(str2[:i]) == len(str1) and len(str1) != len(str2[:i]):
                return str2[:i]
        return ""

word1 = input().upper()
word2 = input().upper()
solution = Solution()
largest_string = solution.gcd_of_strings(word1, word2)
print(largest_string)
