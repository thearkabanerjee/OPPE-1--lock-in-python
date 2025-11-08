# reverse the digits in the given number 


a = int (input ('the digit entered: '))

if (a >=0):

    a_new = str (a)
    reversed_a = a_new[::-1]

else:
    a_new = str(a)
    a_more_new = a_new[1:]
    reversed_a = "-" + a_more_new[::-1]


print (reversed_a)