# DemoRE.py
import re

#result = re.search("[0-9]*th", "35th") #숫자 출현횟수 상관없이 
result = re.search("[0-9]*th", " 35th") #숫자 출현횟수 상관없이 
print(result)
print(result.group()) #찾은 결과만 보여준다

result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.search("apple", "this is apple") #apple 패턴 찾기
print(result.group())
result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())
result = re.search("\d{5}", "우리 동네는 52300")
print(result.group())