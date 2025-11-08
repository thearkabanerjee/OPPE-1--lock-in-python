# for loop factorial 

n = int(input ('enter the number: '))
factorial = 1
i = 1

for i in range (1, n+1): # keep in mind the for loop range
    factorial = factorial * i
    i += 1

print (factorial)
