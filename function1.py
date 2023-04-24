# function1.py
# 1) 함수 정의
def times(a,b):
    return a*b

# 2) 함수 호출
result = times(3,4)
print(result)

def setValue(newValue):
    #지역변수
    x = newValue
    print("함수내부:", x)

#호출
retValue = setValue(5)    
print(retValue)

def swap(x,y):
    return y,x
#호출
print(swap(3,4)) #튜플로 묶어서 반환

#기본값
def times(a=10, b=20):
    return a*b

print(times())    
print(times(5)) 
print(times(5,6)) 

#키워드 인자 방식(인자, 파라미터명을 상세하게 기술)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

print(connectURI("credu.com","80"))
print(connectURI(port="8080", server="credu.com"))


#선택한 행들을 주석처리: ctrl + /
print(dir()) 
print(globals())