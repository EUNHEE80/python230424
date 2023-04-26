# DemoRandom.py
import random
from os.path import * #os 생략가능
from os import *      #os 생략가능
import glob           #glob 지정 사용

print(random.random())
print(random.random())
print(random.uniform(2.0,5.0))
#리스트 컴프리헨션(내장)
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 10)) #sample이 unique한 값을 출력해줘서 사용 권고
print(random.sample(range(20), 10))

print("---파일 정보---")
print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))
if exists("c:\\python310\\python.exe"):
    print(getsize("c:\\python310\\python.exe"))
else:
    print("파일 없음")

#특정 파일을 실행
#system("notepad.exe") #메모장 창 열림
print("운영체제이름:{0}".format(name))

lst = glob.glob("c:\\work\\*.py")
print(lst)
print(count(lst))