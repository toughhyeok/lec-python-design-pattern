## 0. Warming UP
### 1. `public`, `protected`, `private`

멤버 변수, 메소드 앞에 아무것도 없으면 `public`

멤버 변수, 메소드 앞에 '**언더바**'가 한 개 있으면 `protected`

멤버 변수, 메소드 앞에 '**언더바**'가 두 개 있으면 `private`

<br>

`accessor` 만드는 법 `propety decorator` 사용

- `getter` : `@property`

- `setter` : `@멤버변수명.setter`

ex) `@name.setter`

<br>

`private`: `private로` 선언된 `attribute`,

`method`는 해당 클래스에서만 접근 가능

<br>

`protected`: `protected로` 선언된 `attribute`, `method`는

해당 클래스 또는 해당 클래스를 상속받은 클래스에서만 접근 가능

<br>

`public`: `public으로` 선언된 `attribute`,

`method`는 어떤 클래스라도 접근 가능

<br>

`java`, `C++`언어 등의 객체지향 언어와 달리,

파이썬에서의 모든 `attribute`, `method는` 기본적으로 `public`

즉, 클래스 외부에서 `attribute`, `method` 접근 가능 (사용 가능)

<br>


`_`(single underscore), `__`(double underscore)를 붙여서 표시만 함

실제 제약되지는 않고 일종의 경고 표시로 사용됨

<br>

### 2. 상속

자식 클래스에 `__init__`이 생략되어 있다면

부모 클래스의 `__init__`이 호출 된다.

<br>

`interface`, 추상 클래스를 만들고 싶다면 `ABC`, 또는 `ABCMeta`를 상속받아

`@abstractmethod` 함수 데코레이터를 사용한다.

<br>

`class` 멤버 변수, `instance` 멤버 변수 처럼

`method`에도 `classmethod`, `instance method`가 있다.


`classmethod`를 만드려면 `@classmethod` 함수 데코레이터를 사용한다.


`staticmethod`를 만드려면 `@staticmethod` 함수 데코레이터를 사용한다.

<br>

### 3. Duck Typing

> Duck Typing - 'If it walks like a duck and it quacks like a duck, then it must be a duck'

<br>

해석해보면 '오리처럼 걷고, 오리처럼 꽥꽥거리면, 그것은 틀림없이 오리다.' 라는 뜻입니다.

<br>

동적타입의 언어에서 본질적으로 다른클래스라도

객체의 적합성은 객체의 실제 유형이 아니라 특정 메소드와 속성의 존재에 의해 결정되는 것

<br>

## 1. 도형 만들기 예제

### 0. 개요


디자인 패턴이란

1994년 4명의 C++ 개발자가 만든 책의 제목

> GOF's Design Pattern
>
> GOF : Gangs Of Four

당시 C++ 오픈 소스에서 유명한 코딩 스타일에 "이름"을 부여 한 것

<br>

### 1. Prototype


prototype 패턴 : 견본이 되는 객체를 만들고 견본 객체를 복사해서

새로운 객체를 만드는 패턴

`clone()`

<br>

> "Replace conditional with polymorphism"
>
>"제어문을 다형성으로 변경하라"

`if group[idx].type`의 제어문을 `clone()` 함수로 변경하라는

<br>

### 2. Template Method

기반클래스(부모클래스)가 가진 함수중, 
  
변하지 않은 코드 내의 변하는 부분만 파생 클래스(concrete class)에서 재정의 한다.

`mutex lock, unlock`

<br>

### 3. Singleton

싱글톤(Singleton) 패턴의 정의는 단순하다. 객체의 인스턴스가 오직 1개만 생성되는 패턴을 의미한다. 

싱글톤 패턴은 여러 장점 및 단점 주의할 점이 있으면서도 가장 많이 사용되는 패턴이다.

ex) `factory.instance()`


디자인 패턴은 `GOF's Design Patterns`에서 시작된 일종의 코딩 스타일 예시 입니다.

각각의 언어가 가진 패러다임에 따라 사용법이 다르기 때문에 `C++`의 경우에는 `C++` 만의 디자인 패턴이

[C++ Idioms](https://en.wikibooks.org/wiki/More_C%2B%2B_Idioms)에 기록되어 있습니다.

<br>

그렇다면 다들 즐코~

<br>

*(참고) `C++` 문법에 익숙하시다면 강사님이 강의한 내용이 담긴 github repository 주소를 알려드리겠습니다.*