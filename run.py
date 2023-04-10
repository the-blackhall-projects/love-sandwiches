# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

sales = SHEET.worksheet("sales")

data = sales.get_all_values()


print(data, "\n")
os.system('clear')


# Letter frequencies via
# http://www.norvig.com/mayzner.html
freq = [ 
  8.04, 1.48, 3.34, 3.82, 12.49,
  2.40, 1.87, 5.05, 7.57,  0.16,
  0.54, 4.07, 2.51, 7.23,  7.64,
  2.14, 0.12, 6.28, 6.51,  9.28,
  2.73, 1.05, 1.68, 0.23,  1.66,
  0.09,
]
m = max(freq)

for i in range(26):
    u = int(8*freq[i]/m)
    ch = chr(0x2580+u) if u > 0 else " "
    print(ch, end="")

print()
for i in range(26):
    print(chr(0x41+i), end="")



from itertools import chain, combinations
from functools import reduce

def product(lst):
    return reduce(lambda x,y: x*y, lst, 1)

def powerset(iterable):
    xs = list(iterable)
    return chain.from_iterable(
        combinations(xs,n) for n in range(len(xs)+1)
    )

N = 5
# The first N Fermat numbers
F = [2**(2**i)+1 for i in range(N)]

s = {product(x) for x in powerset(F)}
for f in sorted(s):
    print(format(f, 'b'))  

import sys

chars = {
    'a': '┌',
    'b': '┐',
    'c': '┘',
    'd': '└',
    'e': '─',
    'f': '│',
    'g': '┴',
    'h': '├',
    'i': '┬',
    'j': '┤',
    'k': '╷',
    'l': '┼',
}
 
logo = """
aeeb     aeeb
fabf     faec
fdcheiieejf aeeieeb
faejaljkkff fabfkkf
ff fffffffdejdcffff
dc dcdggggeegeegggc
"""
 
for c in logo:
        if c in chars:
            sys.stdout.write(chars[c])
        else:
            sys.stdout.write(c)

print("\n")
