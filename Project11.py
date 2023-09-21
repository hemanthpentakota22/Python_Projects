'''Python Assignment 11: (20th Feb)
A subsequence is a sequence of letters in a string, in order, but with any number of characters removed. Vowels in
order are the letters in the string aeiou.Given a string, determine the length of the longest subsequence
 that contains all of the vowels, in order, and no vowels out of order.
Examples
s = 'aeeiiouu'
All 5 vowels are present in the correct order, so the length of the entire string, 8, is returned.
s = 'aeeiiaouu' Again, all 5 vowels are present in the correct order, though they don't make the entire string. '
The 'a' at position 5 must be removed since it is out of order, leaving 'aeeiiouu' with length 8.
Function Description:-
Complete the function longestVowelSubsequence in the editor below.
longestVowelSubsequence has the following parameter(s):
s: the string to analyze
Returns:int: the length of the longest subsequence within the input string that contains all of the vowels in order;
if one does not occur, return 0Constraints5 < |s| < 5 × 105
Each character of string s ∈ {a, e, i, o, u}.
Input Format for Custom Testing Input from stdin will be processed as follows and passed to the function.
There is only one line containing the string s.
Sample Case 0
Sample InputSTDIN Function
aeiaaioooaauuaeiu → s = "aeiaaioooaauuaeiu"
Sample Output 10
Explanation:-The longest subsequence that contains all the vowels, in order, is aeiiooouuu , which contains 10 characters.
Sample Case 1
Sample InputSTDIN------Function----------
aeiaaiooaa → s = "aeiaaiooaa"
Sample Output 0
ExplanationThe string s does not contain all of the vowels, so return 0.'''



def longestVowelSubsequence(s):
    a = set(s)
    b = ""
    c = 0
    if ('a' not in a or 'e' not in a or 'i' not in a or 'o' not in a or 'u' not in a):
        return c
    else:
        for i in range(len(s)):
            if (s[i] == "a"):
                if (b == "" or b[-1] == "a"):
                    b += s[i]
                    c += 1
            if (s[i] == "e"):
                if (b[-1] == "a" or b[-1] == "e"):
                    b += s[i]
                    c += 1
            if (s[i] == "i"):
                if (b[-1] == "e" or b[-1] == "i"):
                    b += s[i]
                    c += 1
            if (s[i] == "o"):
                if (b[-1] == "i" or b[-1] == "o"):
                    b += s[i]
                    c += 1
            if (s[i] == "u"):
                if (b[-1] == "o" or b[-1] == "u"):
                    b += s[i]
                    c += 1
        return c


s=input()
print(longestVowelSubsequence(s))
