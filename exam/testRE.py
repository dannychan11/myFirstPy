import re
s1='Hello, this is Joey'
s2='The first price is $9.90 and the second price is $100'
print(re.findall('\d+\.?\d*',s2))

def gen():
    value1= yield 1
    value2 = yield 9
gen1=gen()
print(next(gen1))
print(gen1.send(8))
