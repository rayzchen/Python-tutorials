# Quotes

x = "Ray" # Good
x = 'Ray' # Good
x = 'Ray # Bad
x = "Ray # Bad
x = 'Ray's things' #Bad

# Backslash

print("\"Hi!\", he said.")
print("This is a\nnew line")
print("This is a tab -> \t <- this is a tab")
print("No\b\bYes") # Overwrites No witn Yes
print("Raaaaay\rRay") # Overwrites whole line

# String representation

print(repr('"Ray\'s shoes"'))

# Booleans

a = True # True
b = False # False
c = True or False # True
d = True and False # False
e = not False # True

# XOR Gate

input1 = False
input2 = True
out = (input1 and not input2) or (input2 and not input1)
print(out)