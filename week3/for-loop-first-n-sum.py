# for loop to add n numbers


n = (int (input('enter the number: ')))

sum = 0
for i in range (n+1):
    sum += i

print (f'sum is equal to {sum}')