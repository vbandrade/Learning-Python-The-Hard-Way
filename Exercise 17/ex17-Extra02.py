from sys import argv

script, from_file, to_file = argv

indata = open(from_file).read()

output = open(to_file, "w")
output.write(indata)

print "Copied %d bytes from %s to %s." %(len(indata), from_file, to_file)

output.close()