import re
s1='Hello, this is Joey'
s2='The first price is $9.90 and the second price is $100'
print(re.findall('\d+\.?\d*',s2))
