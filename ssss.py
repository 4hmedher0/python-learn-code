class myclass :
    def __init__(self):
        print("Y R Welcom")
    def pr (self):
       print()
    def student (self,name):
        self.marks=[]
        #self.marks.append(Mark)
        self.name=name
        print("welcome %s in School"%(name))
    color="red"
    def add_mark(self,mark):
        self.marks.append(mark)
    def ave(self):
        return sum(self.marks)/len(self.marks)
'''      
x=myclass()
print(x.pr)
print(x)

s=myclass()
s.student(123,'medo')
print(s.name)
print(s.mark)
print(s.color)
s.color='green'
print(s.color)
del s.color  #  مسح الانستانس اللي هي اخضر   
print(s.color) # لم يجد  انستانس  فرجع للقيمة الافتراضية 
#del s.color  # مفيش قيمة انستانس تتمسح اصلا في هيعطي ايرور لانه ميقدرش يغير القيمة الافتراضية في الكلاس 
#print(s.color)
'''
s=myclass()
s.student("ali")
s.add_mark(40)    
s.add_mark(20)    
s.add_mark(30)
print(s.ave())
print(s.marks)
#s1=myclass
#s1.student('ahmed',30)
class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
         return self.a+self.b
    def mul(self):
         return self.a*self.b
    def sub(self):
         return self.a-self.b   
cal=calc(20,30)
print(cal.sub())
#print(s1.marks)
class advancedcalc(calc):
    def power (self):
        return pow(self.a,self.b)
c1=advancedcalc(9,6)
c1=advancedcalc
print(advancedcalc)
print(c1.power())
#print(c1.power())
#c1=advancedcalc(20,30)
#c1.sum()
print(c1)
#print(c1.add())
# cal.mul()
