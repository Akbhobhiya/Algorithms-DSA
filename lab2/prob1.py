import math
class Fraction:
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def inverse(self):
        return Fraction(self.den,self.num)
    def add(self,otherfraction):
        newnum=self.num*otherfraction.den+self.den*otherfraction.num
        newden=self.den*otherfraction.den
        common=math.gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def mul(self,otherfraction):
        newnum=self.num*otherfraction.num
        newden=self.den*otherfraction.den
        common=math.gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def equal(self,otherfraction):
        k1=self.num/self.den
        k2=otherfraction.num/otherfraction.den
        if k1==k2:
            return "Ture"
        else: 
            return "False"
def main():
    print("enter two number")
    a=int(input())
    b=int(input())
    f1=Fraction(a,b)
    f2=f1.inverse()
    print("Fraction of two number is:",f1)
    print("inverse representation is:",f2)
    print("enter two more number for fraction:")
    c=int(input())
    d=int(input())
    f3=Fraction(c,d)
    print("Fraction of these two number is:",f3)
    f4=f1.add(f3)
    print("after add",f4)
    f5=f1.mul(f3)
    print("after multiplication:",f5)
    print("they are equal:",f1.equal(f3))
main()
