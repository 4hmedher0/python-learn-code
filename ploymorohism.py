class shape ():
    def __init__(self,name,length=None):
        self.name=name
        self.length=length
        print("my name is : {name}".format(name=self.name))

class squ(shape):
    def area(self):
        return(self.length*self.length)
class tri(shape):
    def __init__(self,name,base,height):
        super(tri,self).__init__(name)
        self.base=base
        self.height=height
    def area(self):
        return (self.base*self.height*0.5)
#s1=shape("square",3) مفيش كونستكر في السكورير فهتروح علطول  تجيب كونتسكر الاب شيب
s2=squ("squareee",4) 
#s3=shape("triangle")
s3=tri('triangle###',10,5) # لاحظ استخدام السوبر  موجود كونستكر في المثلت فا مش هتروح لكونتسر الاب شيب 
print(s2.area())
print(s3.area())
class medo ():
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
        print('''my name is : %s  and my age is %d  years 
, my number phone is  %s'''%(self.name,self.age,self.phone))

class tiger (medo):
    def __init__(self,name,grade):
        super(tiger,self).__init__(name)
        self.grade=grade
#x1=medo('ahmed',20,'0120')
#x2=test("medo$$",12)        
x=medo('medo',21,'0120')
xx=tiger('pool',12)
