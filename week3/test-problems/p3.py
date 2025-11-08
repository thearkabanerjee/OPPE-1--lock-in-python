# find entered number is palindroome or not 


num = int (input ('enter the number to check: '))
new_num = str(num)

# if (num >= 0):
#     palindromed = new_num [::-1]

# else:
#     very_new_num = new_num[1:]
#     palindromed = '-' + very_new_num [::-1]

# if (int(palindromed) == num):
#     print ('Palindrome')
# else:
#     print ('not a palindrome')



if (num >= 0):
    new_number = new_num

else:
    new_number = new_num[1:]

palindromed = new_number [::-1]

if (new_number == (palindromed)):
    print ('Palindrome')
else:
    print ('not a palindrome')


print (new_number)