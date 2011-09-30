# 
x = "There are %d type of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r" % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Places 'hilarious' on the '%r' in the 'joke_evaluation' string. %r converts any python object using repr()
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Concat strings 'w' and 'e'
print w + e