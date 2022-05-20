# ./1_도형만들기예제5.py

import abc
import copy

class Shape(metaclass=abc.ABCMeta):
    def draw(self):
        print("mutex lock")
        self.draw_imp()
        print("mutex unlock")
    
    @abc.abstractmethod
    def draw_imp(self):
        pass

    def clone(self):
        return copy.deepcopy(self)

class Rect(Shape):
    def draw_imp(self):
        print("draw rect")

class Circle(Shape):
    def draw_imp(self):
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
            
            group.append(group[idx].clone())