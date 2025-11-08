

# string concatination, repetation and substring check

# Solve all the below tasks related to string concatenation, repeatition and substring check in strings.

# problem statement 


# template code 

# output1 = ... # str: join word1 and word2 with space in between

# output2 = ... # str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between

# output3 = ... # str: join the word3 and n1 with a space in between

# output4 = ... # str: just the hypen "-" repeated 50 times

# output5 = ... # str: just the hypen "-" repeated n2 times

# output6 = ... # str: repeat the number n1, n2 times

# are_all_words_equal = ... # bool: True if all three words are equal

# is_word1_comes_before_other_two = ... # bool: True if word1 comes before word2 and word3 assume all words are different

# has_h = ... # bool: True if word1 has the letter h

# ends_with_a = ... # bool: True if word1 ends with letter a or A

# has_the_word_python = ... # bool: True if the sentence has the word python

# sample code 

# Sample inputs (# note: The values given in the prefix code(grey) will be changed by the autograder according to the testcase while running them.
word1 = "Wingardium" # str
word2 = "Leviyosa" # str
word3 = "Silver" # str
sentence = "Learning python is fun"
n1 = 6 # int
n2 = 4 # int
# <eoi>


output1 = (word1 +' ' + word2)
print (output1)

output2 = word1[0:4] +'-' + word2[-4:]
print (output2)

output3 = (f'{word3} {n1}')
print (output3)

output4 = (str('-') * 50)
print (output4)

output5 = (str('-')* n2)
print (output5)

output6 = (str(n1) * n2)
print (output6)

are_all_words_equal = (word1 == word2 == word3)
print (are_all_words_equal)

is_word1_comes_before_other_two = (word1 < word2 and word1 < word3 )
print (is_word1_comes_before_other_two)

has_h =  ('h' in word1)
print (has_h)

ends_with_a = (word1[-1] == 'a' or word1[-1] == 'A')
print (ends_with_a)


has_the_word_python = ('python' in sentence)
print ('the word python is there:', has_the_word_python)