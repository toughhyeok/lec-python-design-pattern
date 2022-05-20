# ./1_도형만들기예제1.py

# 1. 도형은 위치 (x, y), 크기, 색 등 다양한 정보를
#    가지고 있어야 하므로
#    클래스로 설계하는 것이 좋다.
#    => 모든 도형을 타입으로 설계하면 편리하다!!

class Rect:
    def draw(self):
        print("draw rect")

class Circle:
    def draw(self):
        print("draw circle")

# duck typing
# 만약 정적 타입 언어였다면 Rect, Circle을 하나의
# group에 담기 위해서는 기반 클래스가 필요 하다. (타입이 다르기 때문)
# ex) vector<Rect*> v;  // 사각형만 담을 수 있음
# ex) vector<Shape*> v; // Rect, Circle이 Shape을 상속 받는다면 
#                       // 모두 담을 수 있음

if __name__ == '__main__':
    group = list()
    