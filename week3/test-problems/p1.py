# find the number of digits in the given number 

number = abs(int(input("enter the number: ")))

if (number >=0):
    number_of_digits = len (str( number))
else:
    number_of_digits = len (str(number)) -1

print (number_of_digits)
