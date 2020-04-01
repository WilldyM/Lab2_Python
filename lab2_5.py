import re

print('Введите текст:')
text = []
for _ in range(4):
    text.append(input())

res = []
for i,line in enumerate(text):
    res += re.findall(r'\b[A-Z]\w+\d{2}',line)
    res += re.findall(r'\b[A-Z]\w+\d{4}',line)
    
print(res)
