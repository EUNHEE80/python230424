import re 

f=open('c:\\work\\PV3.txt','rt')
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''): #EOF가 아니면 읽어라
    if (re.search("error", line)): #error를 찾아서
    #if (re.search("\d{4}", line)): #숫자 네자리(연도)가 있는 라인을 찾아서
        g.write(line + "\n")       #복사 파일에 써
    line = f.readline()

f.close() 
g.close()








