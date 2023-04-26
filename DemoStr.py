# DemoStr.py
#print(dir(str))
strA = "파이썬은 강력해"
strB = "python is very powerful"
print(len(strA)) #글자 개수
print(len(strB))
print(strB.capitalize()) #첫글자를 대문자로 변경
print(strB.count("p")) #p라는 글자가 몇개인지
print(strB.startswith("pyt"))
print(strB.endswith("ful"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

data = "<<< spam and ham >>>"
result = data.strip("<> ") #<> 공백까지 제거, return을 받으려면 저장을 해야 함
print(data)
result = result.replace("spam","spam egg") #spam을 spam egg로 치환
print(result)
lst = result.split()
print(lst)
print("--- 다시 하나의 문자열---")
print("-".join(lst)) #구분자(-)로 나눠서 조인해라