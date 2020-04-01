try:
    with open(r'data\text.txt', 'r') as f:
        lines = f.readlines()
except IOError as err:
    print(err)
    lines = []


print('Read from file:\n', lines)

newlines = list(map(lambda x: x.rstrip(), lines))
newlines = list(map(lambda x: x.lower(), newlines))
newlines = ''.join(newlines)
newlines = list(newlines)
newlines = list(filter(lambda x: x.isalpha(), newlines))

setlines = set(newlines)
ret = []

for sym in setlines:
    ret.append((sym,newlines.count(sym)))

ret = sorted(ret, key=lambda t: t[1], reverse=True)    

print('Read from file:\n', ret)

