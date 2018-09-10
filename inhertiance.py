from datetime import *
class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
class supercal(cal):
    pass
c1=cal(2,10)
c2=supercal(90,10)
print(c1,c2)
print(c1.add())
print(c2.add())
day=datetime.now()
print(day.now())
      
class Date:
    def get_date(self):
        return day.now()
        
class Time(Date):
    def get_Time(self):
        return day.month
d1=Date()
d2=Time()
print(d2.get_Time())
print(d1.get_date())
print(d2.get_date())

