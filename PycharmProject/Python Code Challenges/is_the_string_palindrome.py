# Solution 1

string = input()

final_string = ""

for str in string:
    if str.isalpha():
        final_string += str.lower()

if final_string == final_string[::-1]:
    print(True)
else:
    print(False)

# Solution 2
import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

print(is_palindrome("Stop_watch_my_code"))