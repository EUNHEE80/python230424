# DemoFile.py
#쓰기(유니코드 방식으로 쓰기)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#읽기(경로 앞 r은 raw string을 의미)
f = open(r"c:\\work\\demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
f.close()