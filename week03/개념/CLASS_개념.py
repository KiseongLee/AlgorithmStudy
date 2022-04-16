'''
class 사용 이유 :
같은 기능을 하는 함수를 동시에 사용할 때, 결괏값을 따로 유지할 수가 없다.
그래서 똑같은 함수를 각각 만들어줘서 변수가 2개 이상이 되는 번거로움이 있는데

클래스를 생성해서 묶어 놓으면(과자틀)
찍어 낼 수가 있다(과자)(함수 개수 늘릴 필요 없고 변수도 분류 가능)
'''

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):       #  클래스 안에 구현된 함수는 다른말로 메서드(method)라 부른다.
        self.first = first                  #  메서드 만드는 방법
        self.second = second                #  def 함수명(매개변수): 수행할 문장

                                            # self에는 객체가 자동으로 전달된다                      
                                            
                                            # 클래스를 통해 메서드를 호출하는 것도 가능
                                            # a = FourCal()
                                            # FourCal.setdata(a, 4, 2)
                                            # 객체.메서드형태로 호출할 때는 self를 반드시 생략
                                            # a = FourCal()
                                            # a.setdata(4, 2)
    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first*self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result                                        
                                            
# a = FourCal()
# a.setdata(4, 2)

# a.first = 4
# a.second = 2
# a객체에 객체 변수 first가 생성되고 값 4가 저장
# a객체에 객체 변수 second가 생성되고 값 2가 저장

# a = FourCal()
# b = FourCal()

# a.setdata(4,2)
# print(a.first)
# b.setdata(3, 7)
# print(b.first)

# 중요 : 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.

# print(a.add())
# print(a.sub())
# print(a.div())
# print(a.mul())


# 생성자(Constructor)
# 객체에 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다
# 생성자를 구현하는 것이 안전한 방법이다. 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드이다.

# 파이썬 메서드 이름으로 __init__를 사용하면 이 메서드는 생성자가 된다.

# a = FourCal(4, 2)
# print(a.first)
# print(a.second)
# print(a.add())
# print(a.div())


# 클래스의 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result

a = MoreFourCal(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())
# 왜 상속을 해야할까?
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.

# "클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 굳이 상속을 받아서 처리?"
# 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야함


# 메서드 오버라이딩

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
    

# SafeFourCal 클래스는 FourCal 클래스에 있는 div 매서드를 동일한 이름으로 다시 작성
# 이렇게 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(메서드 덮어쓰기)라고 한다.
# 이렇게 메서드를 오버라이딩하면 부모 클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.

# SafeFourCal 클래스에 오버라이딩한 div 메서드는 나누는 값이 0인 경우에는 0을 돌려주도록 수정했다.
# 이제 다시 위에서 수행한 예제 FourCal 클래스 대신 SafeFourCal 클래스를 사용하여 수행해보자.

a = SafeFourCal(4, 0)
print(a.div())


# 클래스 변수
# 객체 변수는 다른 객체들에 영향 받지 않고 독립적으로 그 값을 유지한다는 점을 이미 알아보았다.
# 이 번에는 객체 변수와는 성격이 다른 클래스 변수에 대해 알아보자.

class Family:
    lastname = "김"
    
# Family 클래스에 선언한 lastname이 바로 클래스 변수이다. 클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로
# 클래스 안에 변수를 선언하여 생성한다.

print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)