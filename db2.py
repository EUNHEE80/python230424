# db2.py
import sqlite3

#연결객체를 생성(물리적인 파일에 저장)
con = sqlite3.connect("c:\\work\\sample.db")
#SQL 구문을 실행할 커서객체
cur = con.cursor()
#테이블 구조(스키마) 생성
cur.execute("create table if not exists PhoneBook " +
    " (id integer primary key autoincrement, name text, phoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values " +
    " ('홍길동', '010-111-1234');")
#입력 파라미터 처리
name = "이순신"
phoneNumber = "010-222-1234"
cur.execute("insert into PhoneBook (name, phoneNum) values " +
    " (?, ?);", (name,phoneNumber) )

#다중의 데이터를 입력(2차원 배열)
datalist = (("전우치","010-333-1234"),("박문수","010-123-5678"))
cur.executemany("insert into PhoneBook (name, phoneNum) values " +
    " (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
print("---fetchone()---")
print(cur.fetchone())
cur.execute("select * from PhoneBook;")
print("---fetchmany(2)---") # cur.execute를 하지 않으면 앞 실행 수행으로 홍길동이 보여지고 사라지므로 이순신, 전우치가 출력된다
print(cur.fetchmany(2))
cur.execute("select * from PhoneBook;")
print("---fetchall()---")
print(cur.fetchall())
#작업 정상 종료
con.commit()