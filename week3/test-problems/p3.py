# find entered number is palindroome or not 


num = int (input ('enter the number to check: '))
new_num = str(num)

if (num >= 0):
    palindromed = new_num [::-1]

else:
    very_new_num = new_num[1:]
    palindromed = '-' + very_new_num [::-1]

if (int(palindromed) == num):
    print ('Palindrome')
else:
    print ('not a palindrome')