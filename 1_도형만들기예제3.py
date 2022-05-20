# ./1_도형만들기예제3.py

import abc
import copy

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

class Rect(Shape):
    def draw(self):
        print("draw rect")

class Circle(Shape):
    def draw(self):
        print("draw circle")

if __name__ == '__main__':
    group = list()

    while(1):
        cmd = int(input("명령을 입력하세요 >> "))

        if cmd == 1:
            group.append(Rect()) 
        elif cmd == 2:
            group.append(Circle())
        elif cmd == 9:
            for v in group:
                v.draw()
        elif cmd == 8:
            idx = int(input("몇 번째 도형을 복사할까요? 인덱스를 입력하세요 >> "))
            # idx가 유효한 값이라고 가정하자
            #######################################
            # 한 줄로 해결할 수 있다.
            #######################################



# 디자인 패턴이란
# 1994년 4명의 C++ 개발자가 만든 책의 제목
# GOF's Design Pattern

# GOF : Gangs Of Four

# 당시 C++ 오픈 소스에서 유명한 코딩 스타일에 "이름"을 부여 한 것

# prototype 패턴 : 견본이 되는 객체를 만들고 견본 객체를 복사해서
#                 새로운 객체를 만드는 패턴
#                 clone()

# "Replace conditional with polymorphism"
# "제어문을 다형성으로 변경하라"
#  if group[idx].type의 제어문을 clone() 함수로 변경하라는