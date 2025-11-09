# for loop multiplication tables


# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6

n = int(input())
number = int(input())
for i in range (1, number+1):
    product = (n * i)
    print (f' {n} x {i} = {product}')

