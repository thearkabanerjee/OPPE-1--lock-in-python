# # # a = int(input ())

# # # f = 1
# # # for i in range (1, a+1):
# # #     f = f* i
# # #     i +=1

# # # print (f)

# # # a = int(input())

# # # sum = 0

# # # for i in range (a+1):
# # #     sum += i
# # #     i += 1

# # # print (sum)

# # # for i in range (a):
# # #     for j in range (a):
# # #         print ("*")
# # #         j+-1
# # # i += 1

# # n = 5

# # # for i in range (n):

# # # print ('*'* n)
# # for i in range (n): # rows
# #     for j in range (i , n): # columns
# #         print ("*", end=' ')   
# #     print() 



# # a = 5

# # for i in range (a):
# #     for j in range(i,a):
# #         print (" ", end =' ')
# #     print("*", end =' ')


# # find all prime numbers less than the entered number

# # a = int(input())

# n = int(input("Enter a number: "))

# # for num in range(2, n):
# #     for i in range(2, num):
# #         if num % i == 0:
# #             break
# #     else:
# #         print(num, end =' ')

# for i in range (1, n+1):
#     # for j in range (i):
#         print (i)

#     # print ()



# a = int(input ())

# a_new = a. split(' ')
# print(a_new)
# if (a_new == ('O-O' or 'O-O-O')):
#     print ("King \n Rook")






# a:str = 'hello world'
# l:list = []

# for i in range (1,a):
#     if (a% i == 0):
#         print (i)
#         l.append(i)

# print (l)


# import this as this

# print (this)


# def expand_sum_of_products(expr: str) -> str:
#     '''
#     Given a string expression of the form "(a+b)(c+d)", expand it into
#     a sum of products string "a*c + a*d + b*c + b*d".

#     Examples:
#     >>> expand_sum_of_products("(a+b)(c+d)")
#     "a*c + a*d + b*c + b*d"
#     >>> expand_sum_of_products("(x+y)(z+w)")
#     "x*z + x*w + y*z + y*w"
#     >>> expand_sum_of_products("(1+5)(10+12)")
#     "1*10 + 1*12 + 5*10 + 5*12"

#     Args:
#         expr (str): A string representation of a polynomial expression.

#     Returns:
#         str: A formatted string with expanded sum of products.
#     '''
    

#     new-list = list(expr)
#     return (expr[0])
    

expr = '(a+b)(c+d)'

new_expr = expr.strip ('()')

print (new_expr)

print (f"{new_expr[0]}*{new_expr[5]} + {new_expr[0]}*{new_expr[7]} + {new_expr[2]}*{new_expr[5]} + {new_expr[2]}*{new_expr[7]}")