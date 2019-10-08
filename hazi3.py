
class Vrendszer:

    orix, oriy = 0, 0

    def __init__(self, p1, p2):
        self.x=p1
        self.y=p2

    def __str__(self):
        return '({},{})'.format(self.x,self.y)


    def Gethossz(self):
        return ((self.x**2)+(self.y**2))**0.5

    def __add__(self, other):
        if isinstance(other,Vrendszer):
            X=self.x+other.x
            Y=self.y+other.y

        if isinstance(other, int) or isinstance(other,float):
            X=self.x+other
            Y=self.y+other

        return self.__class__(X,Y)

    def __sub__(self, other):
        if isinstance(other,Vrendszer):
            X=self.x-other.x
            Y=self.y-other.y

        if isinstance(other, int) or isinstance(other,float):
            X=self.x-other
            Y=self.y-other

    def __mul__(self, other):
        if isinstance(other,Vrendszer):
            X=self.x*other.x
            Y=self.y*other.y

        if isinstance(other, int) or isinstance(other,float):
            X=self.x*other
            Y=self.y*other

        return self.__class__(X,Y)

    def __lt__(self, other):
        return self.Gethossz() < other.Gethossz()

    def __le__(self, other):
        return self.Gethossz() <= other.Gethossz()

    def __eq__(self, other):
        return self.Gethossz() == other.Gethossz()

    def __iadd__(self, other):

        if isinstance(other,Vrendszer):

            X = self.x + other.x
            Y = self.y + other.y

        if isinstance(other,int) or isinstance(other,float):

            X = self.x + other
            Y = self.y + other

        self.x = X
        self.y = Y
        return self


v1 = Vrendszer(8,2)

v2 = Vrendszer(2,4)

# print(v1.Gethossz())
# print(v1+v2)
# print(v1<v2)
# print(v1>v2)
# print(v1==v2)
# print(v1*v2)
# print(isinstance(v1+5,Vrendszer))

#####################################################################
import math

class KomplexSzamok:

    def __init__(self, p1, p2):
        self.kszam = p1
        self.imagin = p2

    def __str__(self):
        return "({}+{}i)".format(self.kszam, self.imagin)

    def parosit(self):
        return self.__class__(self.kszam, -self.imagin)

    #algebrai alak

    def __abs__(self):
        return (self.kszam**2 + self.imagin**2)**0.5

    def __add__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            kszam2= self.kszam+other
            imagin2=self.imagin
        if isinstance(other, KomplexSzamok):
            kszam2= self.kszam+other.kszam
            imagin2=self.imagin+other.imagin

        return self.__class__(kszam2,imagin2)

    def __sub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            kszam2= self.kszam-other
            imagin2=self.imagin
        if isinstance(other, KomplexSzamok):
            kszam2= self.kszam-other.kszam
            imagin2=self.imagin-other.imagin
        return self.__class__(kszam2,imagin2)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            kszam2= self.kszam*other
            imagin2=self.imagin*other
        if isinstance(other, KomplexSzamok):
            kszam2= (self.kszam*other.kszam)-(self.kszam*other.kszam)
            imagin2=(self.imagin*other.imagin)+(self.imagin*other.imagin)
        return self.__class__(kszam2,imagin2)

    def __eq__(self, other):
        return (self.kszam == other.kszam) and (self.imagin == other.imagin)

    def __ne__(self, other):
        return (self.kszam != other.kszam) or (self.imagin != other.imagin)


    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rsub__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            kszam2 = other - self.kszam
            imagin2 = -self.imagin
        return self.__class__(kszam2, imagin2)


    #trigonometrikus

    def arkusz(self):
        return math.atan(self.kszam / self.imagin)

C1 = KomplexSzamok(4.3, 3.5)
C2 = KomplexSzamok(2.4, 6.11)
print(C1)
print(C1.__abs__())
print(C1.parosit())
print(C1+5)
print(C1+C2)
print(C1-5)
print(C1-C2)
print(C1*5)
print(C1*C2)
print(C1 == C2)
print(C1 != C2)
print(C1.arkusz())
