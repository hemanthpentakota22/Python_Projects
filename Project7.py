'''Programming Assignment 24th JanGiven an input string (s) and a pattern (p),
implement wildcard pattern matching with support for '?' and '*' where:'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
Example 1:Input: s = "aa", p = "a"Output: falseExplanation: "a" does not match the entire string "aa".
Example 2:Input: s = "aa", p = "*"Output: trueExplanation:'*' matches any sequence.
Example 3:Input: s = "cb", p = "?a"Output: falseExplanation:'?' matches 'c', but the second letter is 'a',
which does not match 'b'.Constraints:0 <= s.length, p.length <= 2000s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'. '''


s=input().lower()
p=input().lower()
if(0<=len(s)<=2000 and 0<=len(p)<=2000):
    if(s==p):
        print('true')
    elif('*' in p or '*' in s):
        print('true')
    elif(len(s)==len(p)):
        a=''
        if '?' in s:
            for i in range(len(s)):
                if(s[i] != '?'):
                    a+=s[i]
                elif(s[i] == '?'):
                    a+=p[i]
        else:
            a=s
        b=''
        if '?' in p:
            for i in range(len(p)):
                if(p[i] != '?'):
                    b+=p[i]
                elif(p[i]=='?'):
                    b+=s[i]
        else:
            b=p
        if(a==b):
            print('true')
        else:
            print('false')
    else:
        print('false')
