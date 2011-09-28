print "I will now count my chickens:"

# Divides 30 / 6 (5) and adds 25
print "Hens", 25 + 30 / 6

# Multiply 25 by 3 (75) and subtracts the remainder of the division of 75 by 4 (3) of 100
print "Hoosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

# Operations will be done in the following order:
# 1 / 4 => 0
# 4 % 2 => 0
# After theses steps, the expression is reduced to:
# 3  + 2 + 1 - 5 + 0 - 0 + 6 => 7
print 3  + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true thar 3 + 2 < 5 - 7?"

# Both sides of the 'less than' operator are calculated, and then a comparison is made
# 5 < -2 => False
print 3 + 2 < 5 - 7

# Simple subtraction
print "What is 3 + 2?", 3 + 2

# Simple sum
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

# Simple comparison
print "Is it greater?", 5 > -2

# Simple comparison
print "Is it greater or equal?", 5 >= -2

# Simple comparison
print "Is it less or equal?", 5 <= -2