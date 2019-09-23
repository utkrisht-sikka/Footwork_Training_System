'''
def gcd(m,n):
    if m%n ==0:
        return n
    else:
        return gcd(n,m%n)

class Fractions:
    def __init__(self,num,denom=1):
        g=gcd(num,denom)
        self.num=num/g
        self.denom=denom/g
    def __add__(self,other):
        if isinstance(other,int):
            other=Fraction(other)
        return Fraction(self.num*other.denom+self.denom*self.num,self.num*self.de
    #def __mul__(self,other):
     #   if isinstance(other,int):
      #      other=Fraction(other)
       # return Fraction(self.num*other.num,self.denom*other.denom)
    #def __sub__(self,other):
     #   if isinstance(other,int):
      #      other=Fraction(other)
       # return Fraction(self.num*other.denom-self.denom*other.num,self.denom*other.denom)
    #def __rsub__(self,other):
     #   if isinstance(other,int):
      #      other=Fraction(other)
       # return Fraction((other.num*self.denom-other.denom*self.num,other.denom*self.denom)
f1=Fractions(3,4)
f2=Fractions(4,5)
'''
look="
