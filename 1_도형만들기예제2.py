# ./1_도형만들기예제2.py

import abc

class IShape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

class Rect(IShape):
    def __init__(self):
        self.type = 1
    def draw(self):
        print("draw rect")

class Circle(IShape):
    def __init__(self):
        self.type = 2
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

            # 절차 지향적으로 코드를 오래 작성한 사람들은
            # 아래 처럼 만들곤 합니다
            # 이 코드는 새로운 도형이 추가 되면
            # 한 줄 더 추가되어야 합니다. 즉 OCP를 만족하지 못합니다.
            # OCP (Open Closed Principle) : 확장에는 열려있고 수정에는 닫혀있어야 함
            #                               SOLID
            # 그리고 실제로 "복사"가 이루어지지 않습니다.

            if group[idx].type == 1:
                group.append(Rect())
            elif group[idx].type == 2:
                group.append(Circle())

    