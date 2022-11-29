# PracticalWork2.
# Working with data

# Working with strings
# 1.
string1 = 'This is a string.     '
string2 = '     This is another string.'
# 2.
print('Concatenation: ' + string1 + ' ' + string2)
# 3.
print('String1 length: ', len(string1))
print('lower(): ' + string2.lower())
print('title(): ' + string2.title())
print('upper(): ' + string1.upper())
print('rstrip(): ' + string1.rstrip())
print('lstrip(): ' + string2.lstrip())
print('strip()' + string1.strip())
print('strip("0")' + string2.strip('T, g.'))
# Extracting characters and substrings
# 4.
d = 'qwertyuiop[]'

ch = d[2]
print(d[4] + ' ' + ch)
# 5. Slicing
chm = d[1: 3]
print(chm)
