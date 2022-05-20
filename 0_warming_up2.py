# ./0_warming_up2.py
## 상속, 인터페이스

import abc

class Base:
    def __init__(self):
        print("Base 생성자 호출")
    def hello(self):
        print("Base Hello")

class Derived(Base):
    # def __init__(self):
    #     print("Derived 생성자 호출")
    def hello(self):
        print("Derived Hello")

class IBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def hello(self):
        pass

class Derived2(IBase):
    def hello(self):
        print("Derived2 hi")


if __name__ == '__main__':
    Derived()
    # 결과는 ??
    # 1. => Base 생성자 호출
    #    => Derived 생성자 호출

    # 2. => 아무 것도 출력하지 않음

    # 3. => Base 생성자 호출

    d = Derived2()
    d.hello()

# 자식 클래스에 __init__이 생략되어 있다면
# 부모 클래스의 __init__이 호출 된다.

# interface, 추상 클래스를 만들고 싶다면 ABC, 또는 ABCMeta를 상속받아
# @abstractmethod 함수 데코레이터를 사용한다.

# class 멤버 변수, instance 멤버 변수 처럼
# method에도 classmethod, instance method가 있다.

# classmethod를 만드려면 @classmethod 함수 데코레이터를 사용한다.

# staticmethod를 만드려면 @staticmethod 함수 데코레이터를 사용한다.
