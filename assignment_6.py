'''Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:Input: x = 121Output: trueExplanation: 121 reads as 121 from left to right and from right to left.
Example 2:Input: x = -121Output: falseExplanation: From left to right, it reads -121.
From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:Input: x = 10Output: falseExplanation: Reads 01 from right to left.
Therefore it is not a palindrome.
Constraints:-231<= x <= 231- 1
NOTE: solve it without converting the integer.'''

def solution(n):
    a=0
    b=n
    if(b>9):
        while(1<=b<231):
            a+=(b%10)
            if(b>10):
                a=a*10
            b=b//10
        return a==n
    elif(b<-10):
        while (-231 <= b <= -1):
            a += (b % -10)
            if (b < -10):
                a = a * 10
            b = b // 10 + 1
        return a == n
    else:
        return True

n=int(input())
if(-231<= n <= 231-1):
    print(solution(n))
else:
    print("Input out of range")
