# ./0_warming_up1.py
## public, protected, private

class Student:
    schoolName = 'XYZ School'               # class attribute

    def __init__(self, name, age):
        self.name = name                    # instance attribute
        self.age = age                      # instance attribute

# class 멤버 변수는 객체를 생성하지 않고도 접근할 수 있다.
#       ex) Student.schoolName
# instance 멤버 변수는 객체를 생성해야만 접근할 수 있다.

class Student1:
    _schoolName = 'XYZ School'             # protected class attribute
    def __init__(self, name, age):
        self._name = name                   # protected class attribute
        self._age = age                     # protected class attribute

class Student2:
    __schoolName = 'XYZ School'            # private class attribute
    def __init__(self, name, age):
        self.__name = name                  # private class attribute
        self.__age = age                    # private class attribute

    #  @property
    #  def name(self):
    #      return self._name

    #  @name.setter
    #  def name(self, newname):
    #      self._name = newname   

if __name__ == '__main__':
    std = Student("Steve", 25)
    print("std schoolName : " + std.schoolName)
    print("std name : " + std.name)
    print("std age : " + str(std.age))

    std1 = Student1("Swati", 20)
    print("std1 schoolName : " + std1._schoolName)
    print("std1 name : " + std1._name)
    print("std1 age : " + str(std1._age))
    std1._name = "Chali"
    print("std1 name : " + std1._name)

    std2 = Student2("Dipa", 21)
    # print("std2 name : " + std2._Student2__name)
    print("std2 schoolName : " + std2.__schoolName)     # error
    print("std2 name : " + std2.__name)                 # error
    print("std2 age : " + str(std2.__age))              # error


# 멤버 변수, 메소드 앞에 아무것도 없으면 public
# 멤버 변수, 메소드 앞에 '언더바'가 한 개 있으면 protected
# 멤버 변수, 메소드 앞에 '언더바'가 두 개 있으면 private

# accessor 만드는 법 propety decorator 사용
# - getter : @property
# - setter : @멤버변수명.setter
#            ex) @name.setter

# private: private로 선언된 attribute,
#          method는 해당 클래스에서만 접근 가능
# protected: protected로 선언된 attribute, method는
#            해당 클래스 또는 해당 클래스를 상속받은 클래스에서만 접근 가능
# public: public으로 선언된 attribute,
#         method는 어떤 클래스라도 접근 가능

# java, C++언어 등의 객체지향 언어와 달리,
# 파이썬에서의 모든 attribute, method는 기본적으로 public
# 즉, 클래스 외부에서 attribute, method 접근 가능 (사용 가능)

# _(single underscore), __(double underscore)를 붙여서 표시만 함
# 실제 제약되지는 않고 일종의 경고 표시로 사용됨