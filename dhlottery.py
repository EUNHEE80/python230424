# dhlottery.py

import random

print("---로또6/45---")
result = []
while len(result) < 6:
    num = random.randint(1,45)
    if num not in result:
        result.append(num)
print(result)
print("---연금복권---")
num = random.randint(1,5)
print(num,"조")
num = random.randrange(0,999999)
print(num)
print()
print("<<로또6/45>> (5회 수행)")
for i in range(5):
    result = []
    while len(result) < 6:
        num = random.randint(1,45)
        if num not in result:
            result.append(num)
    print(result)