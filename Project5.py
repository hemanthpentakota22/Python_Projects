'''Write a function solution that, given two integers A and B, returns a string containing exactly A
letters 'a' and exactly B letters 'b' with no three consecutive letters being the same
(in other words, neither "aaa" nor "bbb" may occur in the returned string).

Examples:

1. Given A = 5 and B = 3, your function may return "aabaabab". Note that "abaabbaa" would also be a correct answer.
 Your function may return any correct answer.

2. Given A = 3 and B = 3, your function should return "ababab", "aababb", "abaabb" or any of several other strings.

3. Given A = 1 and B = 4, your function should return "bbabb", which is the only correct answer in this case.

Assume that:

A and B are integers within the range [0..100];
at least one solution exists for the given A and B. '''


a=""
b=""
S=""
A=int(input())
if(0<=A<=100):
    for i in range(A):
        a+="a"
B=int(input())
if(0<=B<=100):
    for i in range(B):
        b+="b"
#print(a)
#print(b)
k=j=0
if(0<=len(a)-len(b)<3 or 0<=len(b)-len(a)<3):
    while k < len(a) and j < len(b):
        S+=a[k]+b[j]
        k+=1
        j+=1
    while k < len(a):
        S+=a[k]
        k += 1
    while j < len(b):
        S+=b[j]
        j += 1
    print(S)
elif(len(a)-len(b)==3 or len(a)-len(b)==-3):
    if(len(a)>len(b)):
        while k < len(a) and j < len(b):
            S+=a[k:k+2]+b[j:j+2]
            k+=2
            j+=2
        while k < len(a):
            S+=a[k:k+2]
            k += 2
        while j < len(b):
            S+=b[j:j+2]
            j += 2
    elif(len(b)>len(a)):
        while k < len(a) and j < len(b):
            S+=b[j:j+2]+a[k:k+2]
            k+=2
            j+=2
        while j < len(b):
            S+=b[j:j+2]
            j += 2
        while k < len(a):
            S+=a[k:k+2]
            k += 2
    print(S)
