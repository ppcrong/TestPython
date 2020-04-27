a = dict({1: 2, 2: 4, 3: 6})  # key: value
print(a[1])
print(a[2])
print(a[3])

b = dict()

b[1] = 2
b[2] = 4
b[3] = 6

print(b[1])
print(b[2])
print(b[3])

print(a.items())
print(a.keys())
print(a.values())

text = 'This is a very big and red apple.'
statistic = {}

for word in text:
    statistic[word] = statistic.get(word, 0) + 1

for key in statistic:
    print(key, statistic[key])

print(statistic)

