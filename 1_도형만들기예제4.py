# ./1_도형만들기예제4.py

import abc
import copy

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass
    
    def clone(self):
        return copy.deepcopy(self)

class Rect(Shape):
    def draw(self):
        print("mutex lock")
        print("draw rect")
        print("mutex unlock")

class Circle(Shape):
    def draw(self):
        print("mutex lock")
        print("draw circle")
        print("mutex unlock")

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
            
            group.append(group[idx].clone())


# 7. template method 패턴 
#	 기반클래스(부모클래스)가 가진 함수중, 
#    변하지 않은 코드 내의 변하는 부분만 파생 클래스에서 재정의 한다.