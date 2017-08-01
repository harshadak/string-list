# Find and replace
words = "It's thanksgiving day. It's my birthday,too!"
words.find("day")
words.replace("day", "month")

# Min and Max
x = [2,54,-2,7,12,98]
min(x)
max(x)

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
a = x[0]
b = x[len(x) - 1]
z = []
z.append(a)
z.append(b)
z = [a, b]

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
a = x[:len(x) / 2]
b = x[len(x) / 2:]
b.insert(0, a)
x = b
print x