# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #인스턴스 멤버 변수
        #클래스 내부에 변수명 숨김 (__ 추가)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
#account1.balance = 15000000 #사고가 발생하는 코드
print(account1)
#print(account1.__balance) # 에러남
print(account1._BankAccount__balance) # 정상 수행
