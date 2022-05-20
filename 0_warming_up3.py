# ./0_warming_up3.py
## duck typing

class Parrot:
    def fly(self):
        print("Parrot flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def lift_off(entity):
    entity.fly()
if __name__ == '__main__':
    parrot = Parrot()
    airplane = Airplane()
    whale = Whale()

    lift_off(parrot)    # prints `Parrot flying`
    lift_off(airplane)  # prints `Airplane flying`
    lift_off(whale)     # Throws the error `'Whale' object has no attribute 'fly'

# Duck Typing - 'If it walks like a duck and it quacks like a duck, then it must be a duck'
# 해석해보면 '오리처럼 걷고, 오리처럼 꽥꽥거리면, 그것은 틀림없이 오리다.' 라는 뜻입니다.

# 동적타입의 언어에서 본질적으로 다른클래스라도
# 객체의 적합성은 객체의 실제 유형이 아니라 특정 메소드와 속성의 존재에 의해 결정되는 것