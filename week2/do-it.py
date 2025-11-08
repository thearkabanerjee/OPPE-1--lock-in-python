# print next characters

name = "arka"
new_name = ''

for ch in name:
    new_name += chr(ord(ch) + 1)
print (new_name)