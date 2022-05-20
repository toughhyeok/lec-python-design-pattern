# ./1_도형만들기예제6.py

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

class ShapeFactory:
    __instance = None

    @classmethod
    def instance(cls):
        if cls.__instance == None:
            cls.__instance = cls()
        return cls.__instance
	
    # 도형의 생성이 한곳에서만 하고 있습니다.
	# 새로운 도형 추가시, 여기만 수정되면 됩니다
	# "코드 수정을 최소화 할수 있습니다."
    def create(self, shape_type):
        ret = None
        if shape_type == 1:
            ret = Rect()
        elif shape_type == 2:
            ret = Circle()
        return ret

        
    # 하지만 이마저도 완벽한 방법이라고 할 수 없습니다.

    # Rect, Circle, ... 에 static class method로 create 함수를 만든다.

    # dict 타입의 전역 변수에 미리 key: cmd, value: 생성 함수를 저장한다.
    # 전역 변수는 main 함수 보다 먼저 실행됩니다.
    # 사각형, 원, 등의 도형을 미리 공장에 등록하는 작업을 수행한다.

    # 이렇게 되면 도형이 추가되어도 factory 클래스는 변하지 않습니다.
    # return ret = map[cmd]() -- 예시 입니다.


class Rect(Shape):
    def draw_imp(self):
        print("draw rect")

class Circle(Shape):
    def draw_imp(self):
        print("draw circle")

if __name__ == '__main__':
    group = list()
    factory = ShapeFactory.instance()

    while(1):
        cmd = int(input("명령을 입력하세요 >> "))
        
        # 아래 코드는 새로운 도형이 추가 되어도 수정될 필요 없습니다.
        if cmd >=1 and cmd <= 7:
            s = factory.create(cmd)
            if s is not None:
                group.append(s)
        elif cmd == 9:
            for v in group:
                v.draw()
        elif cmd == 8:
            idx = int(input("몇 번째 도형을 복사할까요? 인덱스를 입력하세요 >> "))
            group.append(group[idx].clone())