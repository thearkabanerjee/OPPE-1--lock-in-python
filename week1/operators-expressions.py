# operators for python

# adding of 2 lists

l1 = [1, 2, 3, 4]
l2 = [4, 5, 6, 7, 8]

l3 = l1 + l2 # simple adding it is not union. in this example the value of 4 is taken twice


print (l3)

# union of the lists (sets)

set_l1 = set (l1)
set_l2 = set (l2)

union_of_l1_l2 = set_l1 | set_l2

print (union_of_l1_l2) # that is the set version 

print (list (union_of_l1_l2)) # that is the list of the set version []

# intersection of lists

intersection_of_lists = set (l1) & set (l2)

print (intersection_of_lists) # set version

print (list(intersection_of_lists)) # list version of the thing


# union - the common ones (symmetric difference operator)

l4 = set(l1) ^ set(l2)

print (l4)