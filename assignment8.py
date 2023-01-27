'''Programming Assignment : 25th JanRoman numerals are represented by seven different symbols:I, V, X, L, C, D and M.
Symbol     Value
I           1
V           5
X           10
L           50
C           100
D           500
M           1000
For example,2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
which is XX + V + II.Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
Example 1:Input: num = 3Output: "III"Explanation: 3 is represented as 3 ones.Example 2:Input: num = 58Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.Example 3:Input: num = 1994Output: "MCMXCIV"Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
Constraints:1 <= num <= 3999'''
roman_num={1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
num=int(input())
if(1<=num<=3999):
    a = 1
    b = []
    for i in range(len(str(num))):
        b.append(num % 10 * a)
        a *= 10
        num = num // 10
    b.sort(reverse=True)
    c = ""
    for i in range(0, len(b)):
        if b[i] in roman_num:
            c += roman_num[b[i]]
        if (1 <= b[i] < 4):
            c += roman_num[1] * b[i]
        if (5 < b[i] < 9):
            c += roman_num[5] + (roman_num[1] * (b[i] - 5))
        if (10 < b[i] < 40):
            c += roman_num[10] * (b[i]//10)
        if (50 < b[i] < 90):
            c += roman_num[50] * (roman_num[10] * ((b[i]//10) - 5))
        if (100 < b[i] < 400):
            c += roman_num[100] * (b[i]//100)
        if (500 < b[i] < 900):
            c += roman_num[500] * (roman_num[100] * ((b[i]//100) - 5))
        if (1000 < b[i] < 4000):
            c += roman_num[1000] * (b[i]//1000)
    print(c)
else:
    print("number out of range")





