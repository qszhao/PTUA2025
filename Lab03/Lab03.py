import math
from datetime import datetime, timedelta
#Chapter 2 Exercise 1
# 1. We’ve seen that n = 42 is legal. What about 42 = n?
# Answer: 42 = n is illegal.
# 2. How about x = y = 1?
# Answer: x = y = 1 is legal.
x = y = 1
print(x, y)
# 3. In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?
# Answer: This code will not throw an error and the semi-colon will be ignored such as the following code.
print(x);
# 4. What if you put a period at the end of a statement?
# Answer:This code will throw an error.
# 5. In math notation you can multiply x and y like this: x y. What happens if you try that in Python?
# Answer: This code will throw an error. Multiplying x and y should be: x * y.

# Chapter 2 Exercise 2
# 1. The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?
volume = math.pi * 4 * 5 * 5 * 5 / 3
print("The volume of a sphere with radius 5 is: " + str(volume))
# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
total = 24.95 * 60 * 0.6 + 3 + 59 * 0.75
print("The total wholesale for 60 copies is: " + str(total))
# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
easy = timedelta(minutes=8, seconds=15)
tempo = timedelta(minutes=7, seconds=12)
time_total = 2 * easy + 3 * tempo
start = datetime.strptime("6:52", "%H:%M")
finish = start + time_total
print("I get home for breakfast at: " + finish.strftime("%H:%M:%S %p"))

# Chapter 8 Exercise 1
string_1 = "   she's dreaming."
print(string_1.strip())
print(string_1.replace("she's", "She's"))
print(string_1.find("dreaming"))

# Chapter 8 Exercise 2
string_2 = "banana"
print(string_2.count("a"))

# Chapter 8 Exercise 3
def is_palindrome(s):
    return s == s[::-1]

# Chapter 8 Exercise 4
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# This just can check the first letter.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# "c"is always lower. Not check the status of the input string.
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# It only returns the status of the last letter.
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
# Correct.
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
# Correct.

# Chapter 8 Exercise 5
def rotate_word(string, int):
    result = ""
    for i in string:
        if i.isupper():
            start = ord('A')
        else:
            start = ord('a')
        new_char = chr(start + (ord(i) - start + int) % 26)
        result += new_char
    return result
